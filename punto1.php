<?php
$v = array_fill(0, 30, 0);
for ($i = 0; $i < 5000; $i++) {
    $candi = rand(0, 29);
    $v[$candi]++;
}

rsort($v);

echo "El orden de votos del mayor al menor son: <br>";
foreach ($v as $i => $voticos) {
    echo "Candidato " . ($i + 1) . ": " . $voticos . " votos <br>";
}
?>
