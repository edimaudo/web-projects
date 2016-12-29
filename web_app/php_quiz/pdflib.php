<?php
// create short variable names $name = $_POST['name']; $score = $_POST['score'];
if(!$name || !$score) { echo "<h1>Error:</h1>
<p>This page was called incorrectly</p>"; } else {
	$date = date( 'F d, Y' );
// create a pdf document in memory $pdf = pdf_new(); pdf_open_file($pdf, "");
// set up name of font for later use $fontname = 'Times-Roman';
// set up the page size in points and create page
// US letter is 11" x 8.5" and there are approximately // 72 points per inch
$width = 11*72;
$height = 8.5*72;
pdf_begin_page($pdf, $width, $height);
// draw our borders
$inset = 20; // space between border and page edge $border = 10; // width of main border line
$inner = 2; // gap within the border
//draw outer border pdf_rect($pdf, $inset-$inner,
$inset-$inner, $width-2*($inset-$inner), $height-2*($inset-$inner));
pdf_stroke($pdf);
//draw main border $border points wide pdf_setlinewidth($pdf, $border); pdf_rect($pdf, $inset+$border/2,
$inset+$border/2, $width-2*($inset+$border/2), $height-2*($inset+$border/2));
pdf_stroke($pdf); pdf_setlinewidth($pdf, 1.0);
// draw inner border
pdf_rect($pdf, $inset+$border+$inner,
$inset+$border+$inner, $width-2*($inset+$border+$inner), $height-2*($inset+$border+$inner));
pdf_stroke($pdf);
// add heading
$font = pdf_findfont($pdf, $fontname, 'host', 0); if ($font) {
pdf_setfont($pdf, $font, 48); }
$startx = ($width - pdf_stringwidth($pdf, 'PHP Certification', $font, '12'))/2;
pdf_show_xy($pdf, 'PHP Certification', $startx, 490);
// add text
$font = pdf_findfont($pdf, $fontname, 'host', 0); if ($font) {
pdf_setfont($pdf, $font, 26); }
$startx = 70;
pdf_show_xy($pdf, 'This is to certify that:', $startx, 430); pdf_show_xy($pdf, strtoupper($name), $startx+90, 391);
$font = pdf_findfont($pdf, $fontname, 'host', 0); if ($font)
pdf_setfont($pdf, $font, 20);
 pdf_show_xy($pdf, pdf_show_xy($pdf,
pdf_show_xy($pdf,
pdf_show_xy($pdf, pdf_show_xy($pdf,
pdf_show_xy($pdf, pdf_show_xy($pdf,
'has demonstrated that they are certifiable '. 'by passing a rigorous exam', $startx, 340); 'consisting of three multiple choice questions.',
$startx, 310);
"$name obtained a score of $score".'%.', $startx, 260);
'The test was set and overseen by the ', $startx, 210); 'Fictional Institute of PHP Certification',
$startx, 180);
"on $date.", $startx, 150);
'Authorised by:', $startx, 100);
// add bitmap signature image
$signature = pdf_load_image($pdf, 'png', '/Program Files/Apache Software Foundation/Apache2.2/htdocs/phpmysql4e/chapter32/signature.png', '');
pdf_fit_image($pdf, $signature, 200, 75, ''); pdf_close_image($pdf, $signature);

// finish up the page and prepare to output pdf_end_page($pdf);
pdf_close($pdf);
$data = pdf_get_buffer($pdf);
// generate the headers to help a browser choose the correct application header('Content-type: application/pdf');
header('Content-disposition: inline; filename=test.pdf'); header('Content-length: ' . strlen($data));
// output PDF
echo $data;

?>