#!/bin/sh
echo "Part 01:"
gamma=""

while read -r line; do
  read -r zeros ones <<< $(echo "$line" | grep -o . | sort | uniq -c | awk '{print $1}')
  gamma=$([ $zeros -gt $ones ] && echo "${gamma}0" || echo "${gamma}1")
done <<< "$(awk '{$1=$1} 1' FS= inputs/d03.txt | rs -Tng0)"

epsilon="$(echo $gamma | tr 01 10)"

echo "$(( $((2#$gamma)) * $((2#$epsilon)) ))"
