<?php
// Reçoit les demandes du simulateur et du formulaire.
// Si le chantier se chiffre en ligne : crée un vrai devis PDF, l'envoie au client
// avec un lien « Bon pour accord », et prévient Jean Ferret avec les photos.
require __DIR__ . '/lib/devis-lib.php';
const MAX_PHOTOS = 5;
const MAX_OCTETS = 8 * 1024 * 1024;

if ($_SERVER['REQUEST_METHOD'] !== 'POST') { header('Location: /'); exit; }
if (!empty($_POST['site_web'])) { header('Location: /merci.html'); exit; } // piège à robots

function champ($k, $max = 500) {
  $v = trim((string)($_POST[$k] ?? ''));
  return mb_substr(strip_tags(str_replace(["\r", "\n"], ' ', $v)), 0, $max);
}
$r = [];
foreach (['nom'=>120,'telephone'=>30,'email'=>160,'adresse'=>200,'commune'=>120,'travaux'=>80,'dechets'=>80,'acces'=>80,'source'=>60,'taille'=>120,
  'hauteur_arbre'=>10,'pres_maison'=>5,'haie_longueur'=>10,'haie_hauteur'=>10,'haie_faces'=>10,'souche_circ'=>10,'souche_nb'=>10,'souche_racines'=>10,
  'surface'=>10,'cloture_ml'=>10,'cloture_type'=>20,'terrain_surface'=>10] as $k => $max) $r[$k] = champ($k, $max);
$r['email'] = filter_var($r['email'], FILTER_VALIDATE_EMAIL) ? $r['email'] : '';
$message = mb_substr(strip_tags(trim((string)($_POST['message'] ?? ''))), 0, 3000);

if ($r['nom'] === '' || $r['telephone'] === '' || !preg_match('/^[0-9 +().-]{6,30}$/', $r['telephone'])) {
  header('Location: /?erreur=1#estimer'); exit;
}

$calc = $r['travaux'] !== '' ? calculer($r) : ['postes' => [], 'total' => null, 'fourchette' => '', 'note' => ''];
$numero = 'JF-' . date('Ymd-His') . '-' . bin2hex(random_bytes(2));
$avecDevis = $calc['total'] !== null && $r['email'] !== '';
$d = [
  'numero' => $numero, 'date' => date('d/m/Y'), 'validite' => date('d/m/Y', strtotime('+' . VALIDITE_JOURS . ' days')),
  'client' => ['nom' => $r['nom'], 'telephone' => $r['telephone'], 'email' => $r['email'], 'adresse' => $r['adresse'], 'commune' => $r['commune']],
  'travaux' => $r['travaux'], 'acces' => $r['acces'], 'postes' => $calc['postes'], 'total' => $calc['total'],
  'reponses' => $r, 'message' => $message, 'statut' => $avecDevis ? 'envoyé' : 'à chiffrer',
];
enregistrer_devis($d);

// Photos
$photos = [];
$types_ok = ['image/jpeg' => 'jpg', 'image/png' => 'png', 'image/webp' => 'webp', 'image/heic' => 'heic', 'image/heif' => 'heif'];
if (!empty($_FILES['photos']['name']) && is_array($_FILES['photos']['name'])) {
  $finfo = new finfo(FILEINFO_MIME_TYPE);
  foreach ($_FILES['photos']['tmp_name'] as $i => $tmp) {
    if (count($photos) >= MAX_PHOTOS) break;
    if ($_FILES['photos']['error'][$i] !== UPLOAD_ERR_OK || !is_uploaded_file($tmp) || $_FILES['photos']['size'][$i] > MAX_OCTETS) continue;
    $mime = $finfo->file($tmp);
    if (isset($types_ok[$mime])) $photos[] = ['photo-' . (count($photos) + 1) . '.' . $types_ok[$mime], $mime, file_get_contents($tmp)];
  }
}
$pdf = $avecDevis ? devis_pdf($d) : null;

// 1. E-mail à Jean
$lignes = array_map(function ($p) { return '- ' . $p[0] . ' : ' . ($p[2] === null ? 'à la visite' : ($p[2] == 0 ? 'laissés sur place' : eur($p[2]))); }, $calc['postes']);
$details = [];
foreach (['hauteur_arbre','pres_maison','haie_longueur','haie_hauteur','haie_faces','souche_circ','souche_nb','souche_racines','surface','cloture_ml','cloture_type','terrain_surface','dechets','taille'] as $k) if ($r[$k] !== '') $details[] = "$k : {$r[$k]}";
$txt = "Nouvelle demande n° $numero (" . $r['source'] . ")\n\n"
     . "Client : {$r['nom']}\nTéléphone : {$r['telephone']}\nE-mail : " . ($r['email'] ?: 'non donné') . "\nAdresse : {$r['adresse']}, {$r['commune']}\nAccès : {$r['acces']}\n\n"
     . "Travaux : {$r['travaux']}\n" . implode("\n", $lignes) . "\n"
     . ($calc['total'] !== null ? 'TOTAL DU DEVIS : ' . eur($calc['total']) . " (fourchette du simulateur : {$calc['fourchette']})\n" : "Pas de prix automatique : à chiffrer après visite.\n")
     . ($calc['note'] ? "Remarque : {$calc['note']}\n" : '') . "\nRéponses : " . implode(' · ', $details) . "\n\nMessage du client :\n$message\n\n"
     . ($avecDevis ? "Le devis PDF ci-joint a été envoyé au client avec un bouton « Bon pour accord ». Vous recevrez un e-mail s'il l'accepte.\n" : "Aucun devis automatique envoyé : rappelez le client.\n")
     . "Pour écrire au client, répondez simplement à cet e-mail.\n";
$pj = $photos; if ($pdf) array_unshift($pj, ["devis-$numero.pdf", 'application/pdf', $pdf]);
$ok = envoyer(DESTINATAIRE, ($avecDevis ? 'Devis envoyé ' : 'Demande ') . "$numero : {$r['travaux']} à {$r['commune']} ({$r['nom']})", $txt, null, $pj, $r['email'] ?: null, 'Site Jean Ferret');

// 2. Devis au client
if ($ok && $avecDevis) {
  $lien = lien_accord($numero);
  $li = '';
  foreach ($calc['postes'] as $p) $li .= '<tr><td style="padding:8px 0;border-bottom:1px solid #dde3dc">' . h($p[0]) . '</td><td align="right" style="padding:8px 0;border-bottom:1px solid #dde3dc;white-space:nowrap">' . ($p[2] === null ? 'à la visite' : ($p[2] == 0 ? '—' : eur($p[2]))) . '</td></tr>';
  $html = email_html('Bonjour ' . h($r['nom']) . ',',
      '<p>Merci pour votre demande. Votre devis n° ' . h($numero) . ' est joint à cet e-mail en PDF.</p>'
    . '<table width="100%" cellpadding="0" cellspacing="0" style="margin:16px 0">' . $li
    . '<tr><td style="padding:12px 0;font-weight:bold">Total net</td><td align="right" style="padding:12px 0;font-weight:bold;font-size:20px;color:#1f4d2e">' . eur($calc['total']) . '</td></tr></table>'
    . '<p style="font-size:13px;color:#5b6b5e">TVA non applicable, article 293 B du CGI. Prix confirmé lors d\'une visite gratuite avant les travaux. Devis valable ' . VALIDITE_JOURS . ' jours.</p>'
    . '<p><strong>Le prix vous convient ?</strong> Acceptez le devis en un clic :</p>' . bouton($lien, 'Bon pour accord')
    . '<p>Jean Ferret vous appelle ensuite pour la visite et la date des travaux. Une question ? Répondez à cet e-mail ou appelez le <a href="tel:+33610641947" style="color:#1f4d2e">' . TEL . '</a>.</p>');
  $t = "Bonjour {$r['nom']},\n\nVotre devis n° $numero est joint en PDF.\n\n" . implode("\n", $lignes) . "\nTotal net : " . eur($calc['total'])
     . "\nTVA non applicable, art. 293 B du CGI. Prix confirmé lors d'une visite gratuite. Devis valable " . VALIDITE_JOURS . " jours.\n\nPour accepter le devis en un clic : $lien\n\nJean Ferret · " . TEL;
  envoyer($r['email'], "Votre devis $numero – Jean Ferret Paysage", $t, $html, [["devis-$numero.pdf", 'application/pdf', $pdf]], DESTINATAIRE);
}

header('Location: ' . ($ok ? ($avecDevis ? '/merci.html?devis=1' : '/merci.html') : '/?erreur=1#estimer'));
exit;
