#!/bin/sh

echo "Part 1:"
awk '{
if ($1 == "forward") {
  x += $2
} else if ($1 == "up") {
  z -= $2
} else if ($1 == "down") {
  z += $2
}
} { res = z * x}
END {
  print res
}' inputs/d02.txt

echo "Part 2:"
awk '{
  if ($1 == "forward") {
    z += aim * $2
    x += $2
  } else if ($1 == "up") {
    aim -= $2
  } else if ($1 == "down") {
    aim += $2
  }
} { res = z * x }
END {
  print res
}' inputs/d02.txt
