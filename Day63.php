<?php

$nilai = 80;

echo ("Nilai: {$nilai} <br>");

if ($nilai >= 85 and $nilai <= 100) {
  echo ("Grade: A");
} elseif ($nilai >= 75) {
  echo ("Grade: B");
} elseif ($nilai >= 60) {
  echo ("Grade: C");
} elseif ($nilai >= 50) {
  echo ("Grade: D");
} elseif ($nilai >= 0) {
  echo ("Grade: E");
} else {
  echo ("Nilai tidak valid.");
}
