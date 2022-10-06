<?php
$ageNow = (int) date('Y');
$ageUser = (int) readline("In what year were you born ?  ");
$total = $ageNow - $ageUser;

echo PHP_EOL;

echo "Your Age Is  :  ". $total;

echo PHP_EOL;
?>
