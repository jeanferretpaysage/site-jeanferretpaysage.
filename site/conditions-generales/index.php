<?php require dirname(__DIR__) . '/lib/devis-lib.php'; ?><!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Conditions générales de vente | Jean Ferret Paysage</title>
<meta name="description" content="Conditions générales de vente de Jean Ferret Paysage : devis, prix, exécution des travaux, paiement, droit de rétractation, assurance et médiation.">
<meta name="robots" content="noindex">
<link rel="canonical" href="https://jeanferretpaysage.fr/conditions-generales/">
<link rel="stylesheet" href="/css/style.css?v=20261111b">
</head>
<body>

<div class="topbar"><div class="in">
  <a href="tel:+33610641947">06 10 64 19 47 · lun.-sam. 9h-19h</a>
  <span>Saint-Étienne-de-Montluc · Nantes et 30 km autour</span>
</div></div>

<header class="site-header"><div class="in">
  <a class="logo" href="/" aria-label="Jean Ferret Paysage, accueil">
    <svg viewBox="0 0 32 32" aria-hidden="true"><path fill="#1f4d2e" d="M16 2c7 5 10 10 10 15a10 10 0 0 1-20 0C6 12 9 7 16 2z"/><rect fill="#7fae3e" x="14.6" y="19" width="2.8" height="11"/></svg>
    <span><b>Jean Ferret</b><small>Paysage · Élagage</small></span>
  </a>
  <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="menu">Menu</button>
  <nav class="menu" id="menu" aria-label="Menu principal"><ul>
    <li><a href="/elagage-nantes/">Élagage</a></li>
    <li><a href="/abattage-arbre-nantes/">Abattage</a></li>
    <li><a href="/taille-haie-nantes/">Haies</a></li>
    <li><a href="/tonte-entretien-jardin-nantes/">Jardin</a></li>
    <li><a href="/cloture-claustra-nantes/">Clôtures</a></li>
    <li><a href="/faq/">FAQ</a></li>
    <li><a class="cta" href="/tarifs-devis/">Estimer mon prix</a></li>
  </ul></nav>
</div></header>

<main>
<section><div class="in prose">
<h1 style="font-size:2rem;margin-bottom:8px">Conditions générales de vente</h1>
<p class="note"><?= CGV_VERSION ?> · Ces conditions sont jointes à chaque devis.</p>
<?php foreach (cgv() as $a): ?>
<h2><?= h($a[0]) ?></h2>
<p><?= h($a[1]) ?></p>
<?php endforeach; ?>
<h2>Formulaire de rétractation</h2>
<p style="white-space:pre-line"><?= h(formulaire_retractation()) ?></p>
</div></section>
</main>

<footer class="site-footer"><div class="in">
  <span>Jean Ferret Paysage · 4 le Gendre Moreau, 44360 Saint-Étienne-de-Montluc · <a href="tel:+33610641947">06 10 64 19 47</a></span>
  <span><a href="/mentions-legales/">Mentions légales</a> · <a href="/confidentialite/">Confidentialité et cookies</a> · <a href="/conditions-generales/">Conditions générales</a></span>
</div></footer>

<nav class="mbar" aria-label="Contact rapide"><a href="tel:+33610641947">Appeler</a><a href="/tarifs-devis/">Devis photo</a></nav>

<script>
(function(){var t=document.querySelector('.menu-toggle'),m=document.getElementById('menu');
t.addEventListener('click',function(){var o=m.classList.toggle('open');t.setAttribute('aria-expanded',o)});})();
</script>
<script src="/js/consentement.js?v=1" defer></script>
</body>
</html>
