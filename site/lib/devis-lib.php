<?php
// Fonctions communes : barème, devis PDF, enregistrement, e-mails.
date_default_timezone_set('Europe/Paris');
require __DIR__ . '/pdf.php';

const DESTINATAIRE = 'jeanferretpaysage@gmail.com'; // boîte Gmail de Jean
const EXPEDITEUR   = 'site@jeanferretpaysage.fr';   // adresse du domaine, sert seulement à envoyer (Ionos l'exige)
const SITE_URL     = 'https://jeanferretpaysage.fr';
const ENTREPRISE   = 'Jean Ferret Paysage';
const ADRESSE      = '4 le Gendre Moreau, 44360 Saint-Étienne-de-Montluc';
const TEL          = '06 10 64 19 47';
const SIREN        = '403 446 602';
const VALIDITE_JOURS = 30;
// Prix unique du devis à partir de la fourchette : 'milieu', 'haut' ou 'bas'.
const PRIX_MODE = 'milieu';

// Dossier des devis enregistrés, hors du dossier public du site.
function dossier_devis() {
  $d = dirname(__DIR__, 2) . '/donnees-devis';
  if (!is_dir($d)) { mkdir($d, 0700, true); file_put_contents("$d/.htaccess", "Require all denied\n"); }
  return $d;
}
function cle_secrete() {
  $f = dossier_devis() . '/cle.txt';
  if (!is_file($f)) file_put_contents($f, bin2hex(random_bytes(32)));
  return trim(file_get_contents($f));
}
function jeton($numero) { return substr(hash_hmac('sha256', $numero, cle_secrete()), 0, 32); }
function lien_accord($numero) { return SITE_URL . '/accord.php?d=' . rawurlencode($numero) . '&t=' . jeton($numero); }
function enregistrer_devis($d) { file_put_contents(dossier_devis() . '/' . $d['numero'] . '.json', json_encode($d, JSON_UNESCAPED_UNICODE | JSON_PRETTY_PRINT)); }
function charger_devis($numero) {
  if (!preg_match('/^JF-\d{8}-\d{6}-[0-9a-f]{4}$/', $numero)) return null;
  $f = dossier_devis() . "/$numero.json";
  return is_file($f) ? json_decode(file_get_contents($f), true) : null;
}

function eur($n) { return number_format(round($n / 10) * 10, 0, ',', ' ') . ' €'; }
function arrondi($n) { return round($n / 10) * 10; }
function choisir($bas, $haut) {
  if ($haut === null) return $bas;
  return PRIX_MODE === 'haut' ? $haut : (PRIX_MODE === 'bas' ? $bas : ($bas + $haut) / 2);
}

// Calcule les postes du devis à partir des réponses du simulateur.
// Renvoie ['postes'=>[[désignation, détail, montant|null]], 'total'=>float|null, 'fourchette'=>texte, 'note'=>texte]
function calculer($r) {
  $garde = ($r['dechets'] ?? '') === 'Le client garde les déchets';
  $k = $garde ? 0.77 : 1;
  $pres = ($r['pres_maison'] ?? '') === 'oui';
  $ha = $r['hauteur_arbre'] ?? '';
  $haut_txt = ['lt5' => 'moins de 5 m', '5-10' => '5 à 10 m', '10-15' => '10 à 15 m', 'gt15' => 'plus de 15 m'][$ha] ?? '';
  $num = function ($k2) use ($r) { return (float)str_replace(',', '.', $r[$k2] ?? ''); };
  $bas = null; $haut = null; $titre = ''; $detail = ''; $note = ''; $evac = !$garde; $evacInclus = false; $extra = [];
  switch ($r['travaux'] ?? '') {
    case 'Élagage':
      $e = ['lt5' => [200, 650], '5-10' => [460, 1170], '10-15' => [910, 1560], 'gt15' => [1560, 4550]][$ha] ?? null;
      $titre = "Élagage d'un arbre de $haut_txt";
      $detail = 'Taille de réduction et d\'éclaircie, retrait du bois mort, à la nacelle ou en grimpe.' . ($pres ? ' Arbre proche d\'une construction : branches descendues par rétention.' : '');
      if ($e) { $bas = $e[0] * $k; $haut = $e[1] * $k; if ($pres) $bas = ($bas + $haut) / 2; }
      break;
    case 'Abattage':
      $a = ['lt5' => 260, '5-10' => 650, '10-15' => 1040, 'gt15' => 1040][$ha] ?? null;
      $titre = "Abattage d'un arbre de $haut_txt";
      $detail = 'Abattage, découpe du tronc et des branches.';
      if ($a && !$pres) $bas = $a * $k;
      if ($pres) $note = 'Arbre proche d\'une construction : démontage par rétention, prix fixé après visite.';
      break;
    case 'Haie':
      $L = $num('haie_longueur'); $H = $num('haie_hauteur');
      $fa = ['2c+d' => [1, 'deux côtés et le dessus'], '1c+d' => [0.6, 'un côté et le dessus'], '2c' => [0.8, 'deux côtés sans le dessus'], 'd' => [0.35, 'le dessus seulement']][$r['haie_faces'] ?? ''] ?? null;
      $titre = "Taille de haie : $L m de long, $H m de haut";
      $detail = 'Taille ' . ($fa ? $fa[1] : '') . ', ramassage des déchets de coupe.';
      if ($L > 0 && $H > 0 && $fa) { $hh = $H <= 1.5 ? 0.8 : ($H <= 2.5 ? 1 : ($H <= 3.5 ? 1.3 : 1.6)); $p = max($L * (500 / 30) * $fa[0] * $hh * $k, 100); $bas = $p * 0.85; $haut = $p * 1.15; }
      $evacInclus = true;
      break;
    case 'Souche':
      $C = $num('souche_circ'); $N = max(1, (int)$num('souche_nb'));
      $rc = ['peu' => [1, 'peu visibles'], 'grosses' => [1.2, 'grosses racines en surface'], 'etendues' => [1.5, 'racines très étendues']][$r['souche_racines'] ?? ''] ?? null;
      $titre = "Enlèvement de $N souche" . ($N > 1 ? 's' : '') . " (tour du tronc $C cm)";
      $detail = 'Rognage de la souche' . ($rc ? ', ' . $rc[1] : '') . ', rebouchage du trou.';
      if ($C > 0 && $rc) { $b = $C < 60 ? [260, 500] : ($C < 150 ? [500, 1200] : [1200, 2600]); $bas = min($b[0] * $rc[0], 2600) * $N * $k; $haut = min($b[1] * $rc[0], 2600) * $N * $k; }
      $extra[] = ['Location de la rogneuse', 'Si la souche l\'exige, chiffrée lors de la visite.', null];
      break;
    case 'Tonte':
      $S = $num('surface');
      $titre = "Tonte de pelouse : $S m²";
      $detail = 'Tonte, bordures, ramassage de l\'herbe. Prix par passage.';
      if ($S > 0) { $q = max($S * 0.6 * $k, 100); $bas = $q * 0.9; $haut = $q * 1.1; }
      $evacInclus = true;
      break;
    case 'Clôture':
      $ml = $num('cloture_ml');
      $titre = 'Pose de clôture ' . mb_strtolower($r['cloture_type'] ?? '') . " : $ml m";
      $detail = 'Main-d\'œuvre de pose, 40 € le mètre linéaire.';
      if ($ml > 0) $bas = $ml * 40;
      $extra[] = ['Fourniture du matériel', 'Non comprise : panneaux, poteaux et accessoires selon votre choix.', null];
      $evac = false;
      break;
    case 'Création de pelouse':
      $titre = 'Création de pelouse : ' . $num('surface') . ' m²'; $detail = 'Préparation du sol, semis.'; $evac = false; break;
    case 'Terrassement':
      $titre = 'Mise à niveau du terrain : ' . $num('terrain_surface') . ' m²'; $detail = 'Nivellement du terrain.'; $evac = false; break;
    default:
      $titre = $r['travaux'] ?? 'Travaux';
  }
  $fourchette = $bas === null ? '' : ($haut === null ? 'à partir de ' . eur($bas) : 'entre ' . eur($bas) . ' et ' . eur($haut));
  if ($bas === null) return ['postes' => [[$titre, $detail, null]], 'total' => null, 'fourchette' => '', 'note' => $note ?: 'Ce chantier se chiffre après visite.'];
  $total = arrondi(choisir($bas, $haut));
  $postes = [];
  if ($evac && !$evacInclus) {
    $base = arrondi($total / 1.3);
    $postes[] = [$titre, $detail, $base];
    $postes[] = ['Évacuation des déchets verts', 'Chargement, transport et dépôt des branches et du bois.', $total - $base];
  } else {
    $postes[] = [$titre, $detail . ($evacInclus && !$garde ? ' Évacuation des déchets verts comprise.' : ''), $total];
    if ($garde && in_array($r['travaux'], ['Élagage', 'Abattage', 'Souche', 'Haie', 'Tonte'])) $postes[] = ['Déchets verts', 'Laissés sur place à votre demande (prix réduit).', 0];
  }
  foreach ($extra as $e) $postes[] = $e;
  return ['postes' => $postes, 'total' => $total, 'fourchette' => $fourchette, 'note' => $note];
}

function devis_pdf($d) {
  $p = new MiniPDF(); $p->addPage();
  $vert = '#1f4d2e'; $gris = '#5b6b5e'; $m = 42; $W = MiniPDF::W - 2 * $m;
  $p->rect(0, 0, MiniPDF::W, 92, $vert);
  $p->texte($m, 44, 'Jean Ferret', 22, true, '#ffffff');
  $p->texte($m, 62, 'PAYSAGE · ÉLAGAGE', 9, false, '#d9e6d3');
  $p->texte(MiniPDF::W - $m, 40, 'DEVIS', 20, true, '#ffffff', 'd');
  $p->texte(MiniPDF::W - $m, 58, 'N° ' . $d['numero'], 9, false, '#ffffff', 'd');
  $p->texte(MiniPDF::W - $m, 72, 'Du ' . $d['date'] . ' · valable jusqu\'au ' . $d['validite'], 9, false, '#ffffff', 'd');
  $y = 122;
  $p->texte($m, $y, 'ENTREPRISE', 8, true, $gris);
  $p->texte($m + $W / 2 + 10, $y, 'CLIENT', 8, true, $gris);
  $y1 = $p->paragraphe($m, $y + 16, $W / 2 - 20, ENTREPRISE . "\nJean Ferret, entrepreneur individuel (EI)\n" . ADRESSE . "\nSIREN " . SIREN . "\n" . TEL . "\n" . DESTINATAIRE, 9.5);
  $c = $d['client'];
  $y2 = $p->paragraphe($m + $W / 2 + 10, $y + 16, $W / 2 - 10, $c['nom'] . "\n" . $c['adresse'] . "\n" . $c['commune'] . "\n" . $c['telephone'] . "\n" . $c['email'], 9.5);
  $y = max($y1, $y2) + 14;
  $p->texte($m, $y, 'Chantier : ' . $c['adresse'] . ', ' . $c['commune'] . ($d['acces'] ? ' · Accès : ' . $d['acces'] : ''), 9.5, false, $gris);
  $y += 22;
  // Tableau des postes
  $p->rect($m, $y, $W, 22, $vert);
  $p->texte($m + 10, $y + 15, 'Désignation', 9.5, true, '#ffffff');
  $p->texte($m + $W - 10, $y + 15, 'Montant net', 9.5, true, '#ffffff', 'd');
  $y += 22;
  foreach ($d['postes'] as $po) {
    $y0 = $y + 16;
    $p->texte($m + 10, $y0, $po[0], 10, true);
    $yd = $p->paragraphe($m + 10, $y0 + 14, $W - 130, $po[1], 9, false, $gris);
    $p->texte($m + $W - 10, $y0, $po[2] === null ? 'à la visite' : ($po[2] == 0 ? '—' : eur($po[2])), 10, $po[2] !== null, $po[2] === null ? $gris : '#1d2a1f', 'd');
    $y = $yd + 2; $p->ligne($m, $y, $m + $W);
  }
  $y += 10;
  $p->rect($m + $W - 230, $y, 230, 40, '#eef5e4');
  $p->texte($m + $W - 220, $y + 25, 'TOTAL NET À PAYER', 10, true);
  $p->texte($m + $W - 10, $y + 26, eur($d['total']), 15, true, $vert, 'd');
  $p->texte($m + $W - 10, $y + 56, 'TVA non applicable, article 293 B du CGI', 8.5, false, $gris, 'd');
  $y += 84;
  $p->texte($m, $y, 'CONDITIONS', 8, true, $gris); $y += 15;
  $cond = "Prix forfaitaire établi d'après les informations et photos que vous avez transmises. Il est confirmé lors d'une visite gratuite avant les travaux ; si l'état réel du chantier diffère, un devis rectificatif vous sera proposé et ne s'applique qu'avec votre accord.\n"
        . "Devis gratuit, valable " . VALIDITE_JOURS . " jours. Date d'intervention fixée ensemble après acceptation. Règlement à la fin des travaux, sur facture.\n"
        . "Vous disposez d'un délai de rétractation de 14 jours à compter de l'acceptation de ce devis (articles L221-18 et suivants du Code de la consommation).\n"
        . "Entreprise assurée en responsabilité civile professionnelle.";
  $y = $p->paragraphe($m, $y, $W, $cond, 8.8, false, '#1d2a1f', 1.4) + 12;
  $p->rect($m, $y, $W, 92, null, '#7fae3e');
  $p->texte($m + 12, $y + 20, 'BON POUR ACCORD', 10, true, $vert);
  if (!empty($d['accepte_le'])) {
    $p->paragraphe($m + 12, $y + 38, $W - 24, 'Devis accepté en ligne le ' . $d['accepte_le'] . ' par ' . $d['accepte_par'] . '.', 9.5, true);
  } else {
    $p->paragraphe($m + 12, $y + 38, $W - 24, "Acceptez ce devis en un clic avec le lien reçu par e-mail.\nOu renvoyez-le daté et signé, précédé de la mention « Bon pour accord ».", 9.5);
    $p->texte($m + 12, $y + 80, 'Date :', 9, false, $gris); $p->texte($m + $W / 2, $y + 80, 'Signature :', 9, false, $gris);
  }
  $p->texte(MiniPDF::W / 2, MiniPDF::H - 24, ENTREPRISE . ' · ' . ADRESSE . ' · SIREN ' . SIREN . ' · jeanferretpaysage.fr', 7.5, false, $gris, 'c');
  return $p->sortie();
}

function entete($s) { return '=?UTF-8?B?' . base64_encode($s) . '?='; }
// Envoi d'un e-mail texte + HTML, avec pièces jointes [[nom, type, contenu]]
function envoyer($a, $sujet, $texte, $html = null, $pj = [], $repondre = null, $nomExp = 'Jean Ferret Paysage') {
  $lim = 'jf' . bin2hex(random_bytes(8)); $alt = 'jfa' . bin2hex(random_bytes(8));
  $c = "--$lim\r\nContent-Type: multipart/alternative; boundary=\"$alt\"\r\n\r\n"
     . "--$alt\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Transfer-Encoding: base64\r\n\r\n" . chunk_split(base64_encode($texte)) . "\r\n";
  if ($html) $c .= "--$alt\r\nContent-Type: text/html; charset=UTF-8\r\nContent-Transfer-Encoding: base64\r\n\r\n" . chunk_split(base64_encode($html)) . "\r\n";
  $c .= "--$alt--\r\n";
  foreach ($pj as $f) $c .= "--$lim\r\nContent-Type: {$f[1]}; name=\"{$f[0]}\"\r\nContent-Transfer-Encoding: base64\r\nContent-Disposition: attachment; filename=\"{$f[0]}\"\r\n\r\n" . chunk_split(base64_encode($f[2])) . "\r\n";
  $c .= "--$lim--";
  $h = "From: " . entete($nomExp) . " <" . EXPEDITEUR . ">\r\n" . ($repondre ? "Reply-To: $repondre\r\n" : '') . "MIME-Version: 1.0\r\nContent-Type: multipart/mixed; boundary=\"$lim\"";
  return mail($a, entete($sujet), $c, $h, '-f' . EXPEDITEUR);
}
function h($s) { return htmlspecialchars((string)$s, ENT_QUOTES, 'UTF-8'); }
// Gabarit d'e-mail HTML aux couleurs du site
function email_html($titre, $corps) {
  return '<!doctype html><html lang="fr"><body style="margin:0;background:#f2f4f1;font-family:Arial,sans-serif;color:#1d2a1f">'
   . '<table width="100%" cellpadding="0" cellspacing="0"><tr><td align="center" style="padding:24px 12px">'
   . '<table width="600" cellpadding="0" cellspacing="0" style="max-width:600px;background:#fff;border-radius:8px">'
   . '<tr><td style="background:#1f4d2e;color:#fff;padding:20px 24px;border-radius:8px 8px 0 0"><strong style="font-size:20px">Jean Ferret</strong><br><span style="font-size:12px;letter-spacing:1px">PAYSAGE · ÉLAGAGE</span></td></tr>'
   . '<tr><td style="padding:24px"><h1 style="margin:0 0 16px;font-size:22px">' . $titre . '</h1>' . $corps . '</td></tr>'
   . '<tr><td style="padding:16px 24px;background:#f2f4f1;font-size:12px;color:#5b6b5e;border-radius:0 0 8px 8px">' . ENTREPRISE . ' · Jean Ferret EI · ' . ADRESSE . ' · SIREN ' . SIREN . ' · ' . TEL . '</td></tr>'
   . '</table></td></tr></table></body></html>';
}
function bouton($url, $txt) { return '<p style="margin:24px 0"><a href="' . h($url) . '" style="background:#7fae3e;color:#10210f;text-decoration:none;font-weight:bold;padding:14px 22px;border-radius:6px;display:inline-block">' . h($txt) . '</a></p>'; }
