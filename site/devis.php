<?php
// Reçoit les demandes du simulateur et du formulaire.
// 1. Envoie la demande complète (avec photos) à Jean Ferret.
// 2. Envoie au client son devis estimatif par e-mail.
// Seul réglage : l'adresse où Jean reçoit les demandes.
const DESTINATAIRE = 'jeanferretpaysage@gmail.com'; // boîte Gmail de Jean
const EXPEDITEUR   = 'site@jeanferretpaysage.fr';    // adresse du domaine, sert seulement à envoyer (Ionos l'exige)
const MAX_PHOTOS   = 5;
const MAX_OCTETS   = 8 * 1024 * 1024; // 8 Mo par photo

const ENTREPRISE = 'Jean Ferret Paysage';
const ADRESSE    = '4 le Gendre Moreau, 44360 Saint-Étienne-de-Montluc';
const TEL        = '06 10 64 19 47';
const SIREN      = '403 446 602';

date_default_timezone_set('Europe/Paris');
if ($_SERVER['REQUEST_METHOD'] !== 'POST') { header('Location: /'); exit; }
if (!empty($_POST['site_web'])) { header('Location: /merci.html'); exit; } // piège à robots

function champ($k, $max = 500) {
  $v = trim((string)($_POST[$k] ?? ''));
  $v = str_replace(["\r", "\n"], ' ', $v);
  return mb_substr(strip_tags($v), 0, $max);
}
function nombre($k) { return (float)str_replace(',', '.', champ($k, 20)); }
function eur($n) { return number_format(round($n / 10) * 10, 0, ',', ' ') . ' €'; }
function h($s) { return htmlspecialchars($s, ENT_QUOTES, 'UTF-8'); }
function entete($s) { return '=?UTF-8?B?' . base64_encode($s) . '?='; }

$nom = champ('nom', 120);
$tel = champ('telephone', 30);
$email = champ('email', 160);
$email = filter_var($email, FILTER_VALIDATE_EMAIL) ? $email : '';
$commune = champ('commune', 120);
$travaux = champ('travaux', 80);
$dechets = champ('dechets', 80);
$acces = champ('acces', 80);
$source = champ('source', 60);
$message = mb_substr(strip_tags(trim((string)($_POST['message'] ?? ''))), 0, 3000);

if ($nom === '' || $tel === '' || !preg_match('/^[0-9 +().-]{6,30}$/', $tel)) {
  header('Location: /?erreur=1#estimer'); exit;
}

// ---- Barème : identique au simulateur du site, évacuation des déchets verts comprise ----
$garde = ($dechets === 'Le client garde les déchets');
$k = $garde ? 0.77 : 1;
$presMaison = champ('pres_maison', 5) === 'oui';
$hauteurs = ['lt5' => 'moins de 5 m', '5-10' => '5 à 10 m', '10-15' => '10 à 15 m', 'gt15' => 'plus de 15 m'];
$faces = ['2c+d' => [1, '2 côtés et le dessus'], '1c+d' => [0.6, '1 côté et le dessus'], '2c' => [0.8, '2 côtés sans le dessus'], 'd' => [0.35, 'le dessus seulement']];
$racines = ['peu' => [1, 'peu visibles'], 'grosses' => [1.2, 'grosses racines'], 'etendues' => [1.5, 'très étendues']];

$lignes = [];
$bas = null; $haut = null; $note = '';
$ha = champ('hauteur_arbre', 10);

switch ($travaux) {
  case 'Élagage':
    $e = ['lt5' => [200, 650], '5-10' => [460, 1170], '10-15' => [910, 1560], 'gt15' => [1560, 4550]][$ha] ?? null;
    $lignes[] = "Élagage d'un arbre de " . ($hauteurs[$ha] ?? '?');
    if ($e) { $bas = $e[0] * $k; $haut = $e[1] * $k; if ($presMaison) { $bas = ($bas + $haut) / 2; $note = "Arbre proche d'une maison, d'un toit ou d'une ligne : travail par rétention."; } }
    break;
  case 'Abattage':
    $a = ['lt5' => 260, '5-10' => 650, '10-15' => 1040, 'gt15' => 1040][$ha] ?? null;
    $lignes[] = "Abattage d'un arbre de " . ($hauteurs[$ha] ?? '?');
    if ($a) { $bas = $a * $k; if ($presMaison) { $haut = 4550 * $k; $note = "Arbre proche d'une maison : démontage par rétention si nécessaire."; } }
    break;
  case 'Haie':
    $L = nombre('haie_longueur'); $H = nombre('haie_hauteur'); $fa = $faces[champ('haie_faces', 10)] ?? null;
    $lignes[] = "Taille de haie : $L m de long, $H m de haut" . ($fa ? ', ' . $fa[1] : '');
    if ($L > 0 && $H > 0 && $fa) {
      $hh = $H <= 1.5 ? 0.8 : ($H <= 2.5 ? 1 : ($H <= 3.5 ? 1.3 : 1.6));
      $p = max($L * (500 / 30) * $fa[0] * $hh * $k, 100);
      $bas = $p * 0.85; $haut = $p * 1.15;
    }
    break;
  case 'Souche':
    $C = nombre('souche_circ'); $N = max(1, (int)nombre('souche_nb')); $rc = $racines[champ('souche_racines', 10)] ?? null;
    $lignes[] = "Enlèvement de $N souche(s), tour du tronc $C cm" . ($rc ? ', racines ' . $rc[1] : '');
    if ($C > 0 && $rc) {
      $b = $C < 60 ? [260, 500] : ($C < 150 ? [500, 1200] : [1200, 2600]);
      $bas = min($b[0] * $rc[0], 2600) * $N * $k; $haut = min($b[1] * $rc[0], 2600) * $N * $k;
      $note = 'Hors location de la rogneuse si elle est nécessaire.';
    }
    break;
  case 'Tonte':
    $S = nombre('surface');
    $lignes[] = "Tonte de $S m² (tonte, bordures, ramassage)";
    if ($S > 0) { $q = max($S * 0.6 * $k, 100); $bas = $q * 0.9; $haut = $q * 1.1; $note = 'Prix par passage.'; }
    break;
  case 'Création de pelouse':
    $lignes[] = 'Création de pelouse sur ' . nombre('surface') . ' m²';
    break;
  case 'Clôture':
    $ml = nombre('cloture_ml');
    $lignes[] = 'Pose de clôture ' . mb_strtolower(champ('cloture_type', 20)) . " : $ml mètres linéaires";
    if ($ml > 0) { $bas = $ml * 40; $note = 'Pose seule, fourniture du matériel en plus.'; }
    break;
  case 'Terrassement':
    $lignes[] = 'Mise à niveau de terrain sur ' . nombre('terrain_surface') . ' m²';
    break;
  default:
    if ($travaux !== '') $lignes[] = $travaux;
}
if ($dechets !== '' && in_array($travaux, ['Élagage', 'Abattage', 'Haie', 'Souche', 'Tonte'])) {
  $lignes[] = $garde ? 'Déchets verts laissés sur place (prix réduit)' : 'Ramassage et évacuation des déchets verts compris';
}
if ($bas === null)      $prix = 'Prix sur devis après visite';
elseif ($haut === null) $prix = 'À partir de ' . eur($bas);
else                    $prix = 'Entre ' . eur($bas) . ' et ' . eur($haut);

$numero = 'JF-' . date('Ymd-Hi');
$date = date('d/m/Y');

// ---- 1. E-mail à Jean : texte + photos ----
$details = [];
foreach (['hauteur_arbre'=>'Hauteur arbre','pres_maison'=>'Près maison','haie_longueur'=>'Haie longueur (m)','haie_hauteur'=>'Haie hauteur (m)','haie_faces'=>'Haie faces','souche_circ'=>'Tour du tronc (cm)','souche_nb'=>'Nombre de souches','souche_racines'=>'Racines','surface'=>'Surface (m²)','cloture_ml'=>'Clôture (ml)','cloture_type'=>'Type de clôture','terrain_surface'=>'Terrain (m²)','taille'=>'Taille'] as $c=>$lib) {
  $v = champ($c, 60); if ($v !== '') $details[] = "$lib : $v";
}
$texte = "Nouvelle demande de devis n° $numero ($source)\n\n"
       . "Nom : $nom\nTéléphone : $tel\nE-mail : " . ($email ?: 'non donné') . "\nCommune : $commune\n\n"
       . "Travaux : $travaux\n" . implode("\n", $lignes) . "\n\nPrix envoyé au client : $prix\n"
       . ($note ? "Remarque : $note\n" : '') . "Accès : $acces\n\n" . implode("\n", $details) . "\n\nMessage :\n$message\n\n"
       . ($email ? "Le client a reçu son devis estimatif par e-mail. Répondez simplement à cet e-mail pour lui écrire.\n" : "Pas d'e-mail : le client attend votre appel.\n");

$limite = 'jf' . bin2hex(random_bytes(8));
$corps = "--$limite\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Transfer-Encoding: base64\r\n\r\n"
       . chunk_split(base64_encode($texte)) . "\r\n";
$types_ok = ['image/jpeg' => 'jpg', 'image/png' => 'png', 'image/webp' => 'webp', 'image/heic' => 'heic', 'image/heif' => 'heif'];
if (!empty($_FILES['photos']['name']) && is_array($_FILES['photos']['name'])) {
  $finfo = new finfo(FILEINFO_MIME_TYPE);
  $n = 0;
  foreach ($_FILES['photos']['tmp_name'] as $i => $tmp) {
    if ($n >= MAX_PHOTOS) break;
    if ($_FILES['photos']['error'][$i] !== UPLOAD_ERR_OK || !is_uploaded_file($tmp)) continue;
    if ($_FILES['photos']['size'][$i] > MAX_OCTETS) continue;
    $mime = $finfo->file($tmp);
    if (!isset($types_ok[$mime])) continue;
    $n++;
    $f = "photo-$n." . $types_ok[$mime];
    $corps .= "--$limite\r\nContent-Type: $mime; name=\"$f\"\r\nContent-Transfer-Encoding: base64\r\nContent-Disposition: attachment; filename=\"$f\"\r\n\r\n"
            . chunk_split(base64_encode(file_get_contents($tmp))) . "\r\n";
  }
}
$corps .= "--$limite--";
$entetes = "From: " . entete('Site Jean Ferret') . " <" . EXPEDITEUR . ">\r\n"
         . ($email ? "Reply-To: $email\r\n" : '')
         . "MIME-Version: 1.0\r\nContent-Type: multipart/mixed; boundary=\"$limite\"";
$ok = mail(DESTINATAIRE, entete("Devis $numero : $travaux à $commune ($nom)"), $corps, $entetes, '-f' . EXPEDITEUR);

// ---- 2. Devis estimatif envoyé au client ----
if ($ok && $email) {
  $li = '';
  foreach ($lignes as $l) $li .= '<tr><td style="padding:8px 0;border-bottom:1px solid #dde3dc">' . h($l) . '</td></tr>';
  $html = '<!doctype html><html lang="fr"><body style="margin:0;background:#f2f4f1;font-family:Arial,sans-serif;color:#1d2a1f">'
   . '<table width="100%" cellpadding="0" cellspacing="0"><tr><td align="center" style="padding:24px 12px">'
   . '<table width="600" cellpadding="0" cellspacing="0" style="max-width:600px;background:#fff;border-radius:8px">'
   . '<tr><td style="background:#1f4d2e;color:#fff;padding:20px 24px;border-radius:8px 8px 0 0"><strong style="font-size:20px">Jean Ferret</strong><br><span style="font-size:12px;letter-spacing:1px">PAYSAGE · ÉLAGAGE</span></td></tr>'
   . '<tr><td style="padding:24px">'
   . '<p style="margin:0 0 4px;font-size:13px;color:#5b6b5e">Devis estimatif n° ' . h($numero) . ' du ' . $date . '</p>'
   . '<h1 style="margin:0 0 16px;font-size:22px">Bonjour ' . h($nom) . ',</h1>'
   . '<p>Merci pour votre demande. Voici votre devis estimatif, établi à partir de vos réponses.</p>'
   . '<table width="100%" cellpadding="0" cellspacing="0" style="margin:16px 0">'
   . '<tr><td style="padding:8px 0;border-bottom:2px solid #1f4d2e;font-weight:bold">Prestation' . ($commune ? ' à ' . h($commune) : '') . '</td></tr>' . $li . '</table>'
   . '<table width="100%" cellpadding="0" cellspacing="0"><tr><td style="background:#eef5e4;border-left:4px solid #7fae3e;padding:14px 16px">'
   . '<span style="font-size:13px;color:#5b6b5e">Prix estimé</span><br><strong style="font-size:22px">' . h($prix) . '</strong>'
   . ($note ? '<br><span style="font-size:13px">' . h($note) . '</span>' : '') . '</td></tr></table>'
   . '<p style="font-size:13px;color:#5b6b5e">Prix nets : TVA non applicable, article 293 B du CGI. Ce devis est estimatif : le prix définitif est fixé au forfait après une visite gratuite ou l\'étude de vos photos, selon l\'accès et l\'état réel du chantier.</p>'
   . '<p><strong>Et maintenant ?</strong> Jean Ferret vous recontacte pour confirmer le prix et fixer une date. Vous pouvez aussi répondre directement à cet e-mail ou appeler le <a href="tel:+33610641947" style="color:#1f4d2e">' . TEL . '</a>.</p>'
   . '</td></tr>'
   . '<tr><td style="padding:16px 24px;background:#f2f4f1;font-size:12px;color:#5b6b5e;border-radius:0 0 8px 8px">'
   . ENTREPRISE . ' · Jean Ferret EI · ' . ADRESSE . ' · SIREN ' . SIREN . ' · ' . TEL . ' · <a href="https://jeanferretpaysage.fr/" style="color:#1f4d2e">jeanferretpaysage.fr</a></td></tr>'
   . '</table></td></tr></table></body></html>';
  $txt = "Bonjour $nom,\n\nVoici votre devis estimatif n° $numero du $date.\n\n" . implode("\n", $lignes) . "\n\nPrix estimé : $prix\n" . ($note ? "$note\n" : '')
       . "\nPrix nets : TVA non applicable, art. 293 B du CGI. Prix définitif au forfait après visite gratuite ou étude de vos photos.\n\n"
       . "Jean Ferret vous recontacte pour confirmer. Vous pouvez répondre à cet e-mail ou appeler le " . TEL . ".\n\n"
       . ENTREPRISE . ' · ' . ADRESSE . ' · SIREN ' . SIREN;
  $lim2 = 'jfc' . bin2hex(random_bytes(8));
  $c2 = "--$lim2\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Transfer-Encoding: base64\r\n\r\n" . chunk_split(base64_encode($txt))
      . "\r\n--$lim2\r\nContent-Type: text/html; charset=UTF-8\r\nContent-Transfer-Encoding: base64\r\n\r\n" . chunk_split(base64_encode($html)) . "\r\n--$lim2--";
  $e2 = "From: " . entete('Jean Ferret Paysage') . " <" . EXPEDITEUR . ">\r\n"
      . "Reply-To: " . DESTINATAIRE . "\r\n"
      . "MIME-Version: 1.0\r\nContent-Type: multipart/alternative; boundary=\"$lim2\"";
  mail($email, entete("Votre devis estimatif $numero – Jean Ferret Paysage"), $c2, $e2, '-f' . EXPEDITEUR);
}

header('Location: ' . ($ok ? '/merci.html' : '/?erreur=1#estimer'));
exit;
