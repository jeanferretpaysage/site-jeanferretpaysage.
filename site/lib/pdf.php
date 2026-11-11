<?php
// Petit générateur de PDF sans dépendance (police Helvetica, accents français).
class MiniPDF {
  private $pages = []; private $cur = -1;
  const W = 595.28; const H = 841.89;
  // Largeurs Helvetica (1/1000 em) pour les caractères courants, sinon 556.
  private static $w = [' '=>278,'!'=>278,'"'=>355,"'"=>191,'('=>333,')'=>333,'*'=>389,'+'=>584,','=>278,'-'=>333,'.'=>278,'/'=>278,':'=>278,';'=>278,'?'=>556,'°'=>400,'€'=>556,'%'=>889,'&'=>667,'«'=>556,'»'=>556,'·'=>278,'²'=>333,
    'I'=>278,'J'=>500,'M'=>833,'W'=>944,'f'=>278,'i'=>222,'j'=>222,'l'=>222,'m'=>833,'r'=>333,'t'=>278,'w'=>722,'c'=>500,'k'=>500,'s'=>500,'v'=>500,'x'=>500,'y'=>500,'z'=>500,
    'A'=>667,'B'=>667,'C'=>722,'D'=>722,'E'=>667,'F'=>611,'G'=>778,'H'=>722,'K'=>667,'L'=>556,'N'=>722,'O'=>778,'P'=>667,'Q'=>778,'R'=>722,'S'=>667,'T'=>611,'U'=>722,'V'=>667,'X'=>667,'Y'=>667,'Z'=>611];
  function addPage() { $this->pages[] = ''; $this->cur++; }
  private function out($s) { $this->pages[$this->cur] .= $s . "\n"; }
  private static function enc($s) { return iconv('UTF-8', 'Windows-1252//TRANSLIT', $s); }
  private static function esc($s) { return str_replace(['\\', '(', ')', "\r"], ['\\\\', '\\(', '\\)', ''], $s); }
  static function largeur($s, $taille, $gras = false) {
    $t = 0; foreach (preg_split('//u', $s, -1, PREG_SPLIT_NO_EMPTY) as $c) {
      $b = preg_replace('/[àâä]/u','a',preg_replace('/[éèêë]/u','e',preg_replace('/[ôö]/u','o',preg_replace('/[ùûü]/u','u',preg_replace('/[îï]/u','i',preg_replace('/ç/u','c',$c))))));
      $b = preg_replace('/[ÉÈÊ]/u','E',preg_replace('/[ÀÂ]/u','A',$b));
      $t += self::$w[$b] ?? 556; }
    return $t * $taille / 1000 * ($gras ? 1.05 : 1);
  }
  private static function rgb($hex) { return implode(' ', array_map(function ($i) use ($hex) { return round(hexdec(substr($hex, $i, 2)) / 255, 3); }, [1, 3, 5])); }
  // y mesuré depuis le haut de la page
  function texte($x, $y, $s, $taille = 10, $gras = false, $coul = '#1d2a1f', $align = 'g') {
    if ($align === 'd') $x -= self::largeur($s, $taille, $gras);
    elseif ($align === 'c') $x -= self::largeur($s, $taille, $gras) / 2;
    $this->out('BT /' . ($gras ? 'F2' : 'F1') . " $taille Tf " . self::rgb($coul) . ' rg ' . round($x, 2) . ' ' . round(self::H - $y, 2) . ' Td (' . self::esc(self::enc($s)) . ') Tj ET');
  }
  // Texte sur plusieurs lignes, renvoie le y final
  function paragraphe($x, $y, $largeur, $s, $taille = 10, $gras = false, $coul = '#1d2a1f', $interligne = 1.35) {
    foreach (explode("\n", $s) as $bloc) {
      $ligne = '';
      foreach (explode(' ', $bloc) as $mot) {
        $essai = $ligne === '' ? $mot : "$ligne $mot";
        if (self::largeur($essai, $taille, $gras) > $largeur && $ligne !== '') { $this->texte($x, $y, $ligne, $taille, $gras, $coul); $y += $taille * $interligne; $ligne = $mot; }
        else $ligne = $essai;
      }
      $this->texte($x, $y, $ligne, $taille, $gras, $coul); $y += $taille * $interligne;
    }
    return $y;
  }
  function rect($x, $y, $w, $h, $fond = null, $trait = null) {
    $op = $fond && $trait ? 'B' : ($fond ? 'f' : 'S');
    $this->out(($fond ? self::rgb($fond) . ' rg ' : '') . ($trait ? self::rgb($trait) . ' RG 0.8 w ' : '') . round($x, 2) . ' ' . round(self::H - $y - $h, 2) . ' ' . round($w, 2) . ' ' . round($h, 2) . " re $op");
  }
  function ligne($x1, $y, $x2, $coul = '#dde3dc', $ep = 0.8) {
    $this->out(self::rgb($coul) . " RG $ep w " . round($x1, 2) . ' ' . round(self::H - $y, 2) . ' m ' . round($x2, 2) . ' ' . round(self::H - $y, 2) . ' l S');
  }
  function sortie() {
    $o = []; $pdf = "%PDF-1.4\n%\xE2\xE3\xCF\xD3\n";
    $add = function ($s) use (&$o, &$pdf) { $o[] = strlen($pdf); $pdf .= (count($o)) . " 0 obj\n$s\nendobj\n"; return count($o); };
    $add('<< /Type /Catalog /Pages 2 0 R >>');
    $n = count($this->pages); $kids = [];
    for ($i = 0; $i < $n; $i++) $kids[] = (5 + 2 * $i) . ' 0 R';
    $add('<< /Type /Pages /Kids [' . implode(' ', $kids) . "] /Count $n >>");
    $add('<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>');
    $add('<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>');
    foreach ($this->pages as $i => $c) {
      $add('<< /Type /Page /Parent 2 0 R /MediaBox [0 0 ' . self::W . ' ' . self::H . '] /Resources << /Font << /F1 3 0 R /F2 4 0 R >> >> /Contents ' . (6 + 2 * $i) . ' 0 R >>');
      $z = gzcompress($c);
      $add('<< /Length ' . strlen($z) . " /Filter /FlateDecode >>\nstream\n$z\nendstream");
    }
    $x = strlen($pdf);
    $pdf .= "xref\n0 " . (count($o) + 1) . "\n0000000000 65535 f \n";
    foreach ($o as $p) $pdf .= sprintf("%010d 00000 n \n", $p);
    $pdf .= "trailer\n<< /Size " . (count($o) + 1) . " /Root 1 0 R >>\nstartxref\n$x\n%%EOF";
    return $pdf;
  }
}
