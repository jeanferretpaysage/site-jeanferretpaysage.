<?php
// Mise à jour automatique du site depuis GitHub.
// Lancé par une tâche cron Ionos (toutes les heures). Ce fichier est rangé
// hors du dossier "site", il n'est donc pas visible sur internet.
// Il télécharge la dernière version du dépôt, puis copie le contenu de son
// dossier "site/" dans le dossier /site de l'hébergement. Il ne supprime rien.

date_default_timezone_set('Europe/Paris');
const DEPOT  = 'jeanferretpaysage/site-jeanferretpaysage.';
const BRANCHE = 'main';

$ici   = __DIR__;
$cible = dirname($ici) . '/site';
$journal = $ici . '/maj.log';
$memo  = $ici . '/version.txt';
function note($m) { global $journal; file_put_contents($journal, date('Y-m-d H:i ') . $m . "\n", FILE_APPEND); }
function telecharger($url) {
  $c = curl_init($url);
  curl_setopt_array($c, [CURLOPT_RETURNTRANSFER => true, CURLOPT_FOLLOWLOCATION => true, CURLOPT_TIMEOUT => 120,
    CURLOPT_USERAGENT => 'maj-site', CURLOPT_HTTPHEADER => ['Accept: application/vnd.github+json']]);
  $r = curl_exec($c); $code = curl_getinfo($c, CURLINFO_HTTP_CODE); curl_close($c);
  return $code === 200 ? $r : false;
}

// 1. Y a-t-il une nouvelle version ?
$info = telecharger('https://api.github.com/repos/' . DEPOT . '/commits/' . BRANCHE);
$sha = $info ? (json_decode($info, true)['sha'] ?? '') : '';
if ($sha === '') { note('GitHub injoignable, on réessaiera.'); exit; }
$force = isset($argv[1]) && $argv[1] === 'force';
if (!$force && is_file($memo) && trim(file_get_contents($memo)) === $sha) exit; // déjà à jour

// 2. Télécharger et copier
$zip = telecharger('https://api.github.com/repos/' . DEPOT . '/zipball/' . $sha);
if ($zip === false) { note('Téléchargement impossible.'); exit; }
$tmp = $ici . '/depot.zip';
file_put_contents($tmp, $zip);
$z = new ZipArchive();
if ($z->open($tmp) !== true) { note('Archive illisible.'); @unlink($tmp); exit; }
$n = 0;
for ($i = 0; $i < $z->numFiles; $i++) {
  $nom = $z->getNameIndex($i);
  $pos = strpos($nom, '/site/');              // "<dossier-du-depot>/site/chemin"
  if ($pos === false || substr_count(substr($nom, 0, $pos), '/') > 0) continue;
  $rel = substr($nom, $pos + 6);
  if ($rel === '' || strpos($rel, '..') !== false) continue;
  $dest = $cible . '/' . $rel;
  if (substr($nom, -1) === '/') { if (!is_dir($dest)) mkdir($dest, 0755, true); continue; }
  if (!is_dir(dirname($dest))) mkdir(dirname($dest), 0755, true);
  file_put_contents($dest, $z->getFromIndex($i));
  $n++;
}
$z->close(); @unlink($tmp);
if ($n > 0) { file_put_contents($memo, $sha); note("Site mis à jour : $n fichiers (version " . substr($sha, 0, 7) . ').'); }
else note('Aucun fichier trouvé dans le dossier site du dépôt.');
