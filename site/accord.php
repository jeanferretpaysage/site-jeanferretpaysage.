<?php
// Page « Bon pour accord » : le client consulte son devis et l'accepte en un clic.
require __DIR__ . '/lib/devis-lib.php';
header('X-Robots-Tag: noindex');
$num = (string)($_GET['d'] ?? $_POST['d'] ?? '');
$tok = (string)($_GET['t'] ?? $_POST['t'] ?? '');
$d = charger_devis($num);
$valide = $d && hash_equals(jeton($num), $tok);

if ($valide && isset($_GET['pdf'])) {
  header('Content-Type: application/pdf');
  header('Content-Disposition: inline; filename="devis-' . $num . '.pdf"');
  echo devis_pdf($d); exit;
}

$etat = 'voir'; $erreur = '';
if ($valide && !empty($d['accepte_le'])) $etat = 'deja';
elseif ($valide && strtotime(str_replace('/', '-', $d['validite']) . ' 23:59') < time()) $etat = 'expire';
elseif ($valide && $_SERVER['REQUEST_METHOD'] === 'POST') {
  $nom = trim(strip_tags((string)($_POST['signature'] ?? '')));
  if (empty($_POST['accepte']) || mb_strlen($nom) < 3) $erreur = 'Cochez la case et écrivez votre nom pour accepter le devis.';
  else {
    $d['accepte_le'] = date('d/m/Y à H:i'); $d['accepte_par'] = mb_substr($nom, 0, 120);
    $d['accepte_ip'] = $_SERVER['REMOTE_ADDR'] ?? ''; $d['statut'] = 'accepté';
    $d['debut_anticipe'] = !empty($_POST['anticipe']);
    enregistrer_devis($d);
    $pdf = devis_pdf($d);
    $c = $d['client'];
    envoyer(DESTINATAIRE, "✅ Devis {$d['numero']} ACCEPTÉ : {$d['travaux']} à {$c['commune']} ({$c['nom']})",
      "Bonne nouvelle : le devis {$d['numero']} vient d'être accepté en ligne.\n\nClient : {$c['nom']}\nTéléphone : {$c['telephone']}\nE-mail : {$c['email']}\nChantier : {$c['adresse']}, {$c['commune']}\n\nTotal : " . eur($d['total']) . "\nAccepté le {$d['accepte_le']} par « {$d['accepte_par']} ».\n" . ($d['debut_anticipe'] ? "Le client DEMANDE à commencer avant la fin du délai de rétractation de 14 jours.\n" : "Le client n'a pas demandé de début anticipé : attendre la fin du délai de rétractation de 14 jours (sauf nouvel accord écrit).\n") . "\nAppelez le client pour fixer la visite et la date des travaux. Le devis signé est joint.",
      null, [["devis-{$d['numero']}-accepte.pdf", 'application/pdf', $pdf]], $c['email'], 'Site Jean Ferret');
    envoyer($c['email'], "Devis {$d['numero']} accepté – Jean Ferret Paysage",
      "Bonjour {$c['nom']},\n\nVotre accord pour le devis {$d['numero']} (" . eur($d['total']) . ") est bien enregistré. Jean Ferret vous appelle pour fixer la visite et la date des travaux.\n\nVous disposez d'un délai de rétractation de 14 jours.\n\nJean Ferret · " . TEL,
      email_html('Merci ' . h($c['nom']) . ' !', '<p>Votre accord pour le devis n° ' . h($d['numero']) . ' (' . eur($d['total']) . ') est bien enregistré. Le devis accepté est joint à cet e-mail.</p><p>Jean Ferret vous appelle pour fixer la visite et la date des travaux.</p><p style="font-size:13px;color:#5b6b5e">Vous disposez d\'un délai de rétractation de 14 jours à compter de votre acceptation.</p>'),
      [["devis-{$d['numero']}-accepte.pdf", 'application/pdf', $pdf]], DESTINATAIRE);
    $etat = 'merci';
  }
}
?><!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Votre devis | Jean Ferret Paysage</title>
<meta name="robots" content="noindex">
<link rel="stylesheet" href="/css/style.css?v=20261111d">
<link rel="icon" href="/img/logo.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<style>
.devis-recap{border:1px solid var(--line);border-radius:8px;padding:20px;margin:20px 0;background:#fff}
.devis-recap table{width:100%;border-collapse:collapse}.devis-recap td{padding:10px 0;border-bottom:1px solid var(--line);vertical-align:top}
.devis-recap td:last-child{text-align:right;white-space:nowrap;padding-left:12px}.devis-recap small{display:block;color:var(--muted)}
.devis-total td{font-weight:700;font-size:1.15rem;border-bottom:0}
.accord{display:flex;flex-direction:column;gap:12px;max-width:520px}.accord label{display:flex;gap:10px;align-items:flex-start}
.accord input[type=text]{width:100%;padding:12px;border:2px solid var(--line);border-radius:6px;font:inherit}
.erreur{color:#a12a1a;font-weight:600}
</style>
</head>
<body>
<header class="site-header"><div class="in">
  <a class="logo" href="/"><img src="/img/logo.svg" width="52" height="52" alt=""><span><b>Jean Ferret</b><small>Paysage · Élagage</small></span></a>
</div></header>
<main><section><div class="in" style="max-width:760px">
<?php if (!$valide): ?>
  <h1>Lien de devis introuvable</h1>
  <p>Ce lien ne correspond à aucun devis. Vérifiez que vous avez copié le lien en entier, ou appelez Jean Ferret au <a href="tel:+33610641947"><?= TEL ?></a>.</p>
<?php elseif ($etat === 'merci' || $etat === 'deja'): ?>
  <span class="eyebrow">Devis n° <?= h($d['numero']) ?></span>
  <h1><?= $etat === 'merci' ? 'Merci, votre accord est enregistré' : 'Ce devis est déjà accepté' ?></h1>
  <p>Accepté le <?= h($d['accepte_le']) ?> par <?= h($d['accepte_par']) ?>. Jean Ferret vous appelle pour fixer la visite et la date des travaux. Une confirmation vous a été envoyée par e-mail.</p>
  <p><a class="btn btn-m" href="?d=<?= h($num) ?>&amp;t=<?= h($tok) ?>&amp;pdf=1">Voir le devis accepté (PDF)</a></p>
<?php else: ?>
  <span class="eyebrow">Devis n° <?= h($d['numero']) ?> du <?= h($d['date']) ?></span>
  <h1>Votre devis, <?= h($d['client']['nom']) ?></h1>
  <div class="devis-recap">
    <table>
      <?php foreach ($d['postes'] as $p): ?>
      <tr><td><strong><?= h($p[0]) ?></strong><small><?= h($p[1]) ?></small></td><td><?= $p[2] === null ? 'à la visite' : ($p[2] == 0 ? '—' : eur($p[2])) ?></td></tr>
      <?php endforeach; ?>
      <tr class="devis-total"><td>Total net</td><td><?= eur($d['total']) ?></td></tr>
    </table>
    <p class="note">TVA non applicable, article 293 B du CGI. Chantier : <?= h($d['client']['adresse'] . ', ' . $d['client']['commune']) ?>. Prix confirmé lors d'une visite gratuite avant les travaux ; si l'état réel diffère, un devis rectificatif vous sera proposé. Valable jusqu'au <?= h($d['validite']) ?>.</p>
    <p><a href="?d=<?= h($num) ?>&amp;t=<?= h($tok) ?>&amp;pdf=1">Télécharger le devis complet (PDF)</a></p>
  </div>
  <?php if ($etat === 'expire'): ?>
    <p class="erreur">Ce devis a expiré. Appelez le <a href="tel:+33610641947"><?= TEL ?></a> ou refaites une demande sur le site.</p>
  <?php else: ?>
  <h2>Bon pour accord</h2>
  <form class="accord" method="post">
    <input type="hidden" name="d" value="<?= h($num) ?>"><input type="hidden" name="t" value="<?= h($tok) ?>">
    <?php if ($erreur): ?><p class="erreur"><?= h($erreur) ?></p><?php endif; ?>
    <label><input type="checkbox" name="accepte" value="1" required> <span>J'ai lu ce devis et je l'accepte, ainsi que les <a href="/conditions-generales/" target="_blank">conditions générales de vente</a>. Je dispose d'un délai de rétractation de 14 jours.</span></label>
    <label><input type="checkbox" name="anticipe" value="1"> <span>Facultatif : je demande que les travaux puissent commencer avant la fin de ce délai de 14 jours. Si je me rétracte ensuite, je paierai la part déjà réalisée.</span></label>
    <label style="flex-direction:column;gap:6px">Votre nom et prénom, en guise de signature<input type="text" name="signature" required autocomplete="name"></label>
    <button class="btn btn-a" type="submit">J'accepte le devis</button>
    <p class="note">Une question avant d'accepter ? Appelez le <a href="tel:+33610641947"><?= TEL ?></a>.</p>
  </form>
  <?php endif; ?>
<?php endif; ?>
</div></section></main>
<script src="/js/consentement.js?v=1" defer></script>
</body>
</html>
