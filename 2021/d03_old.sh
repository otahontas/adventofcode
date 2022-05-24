#!/bin/sh

# https://github.com/koffiebaard/advent-of-code-2021/blob/master/day3/challenge2.sh
# kiinnostavaa settiä

echo "Part 01:"
gamma=""

while read -r line; do
  read -r zeros ones <<< $(echo "$line" | grep -o . | sort | uniq -c | awk '{print $1}')
  gamma=$([ $zeros -gt $ones ] && echo "${gamma}0" || echo "${gamma}1")
done <<< "$(awk '{$1=$1} 1' FS= inputs/d03.txt | rs -Tng0)"

epsilon="$(echo $gamma | tr 01 10)"

echo "$(( $((2#$gamma)) * $((2#$epsilon)) ))"

echo "Part 02:"

function count() {
  mode=$1
  local lines=$(<inputs/d03.txt)
  local pos=1
  local max_pos=13
  while true; do
    cols=$(echo "$lines" | awk '{$1=$1} 1' FS= | rs -Tng0 | sed -n "${pos}p")
    read -r zeros ones <<< $(echo "$cols" | grep -o . | sort | uniq -c | awk '{print $1}')
    if [ "$mode" == "oxygen" ]; then
      popular=$([ $zeros -gt $ones ] && echo "0" || echo "1")
    else
      popular=$([ $zeros -le $ones ] && echo "0" || echo "1")
    fi
    rows_with_popular=$(echo "$cols" | sed 's/\(.\)/\1\n/g' | grep -n "$popular" | awk -F':' '{print $1}')
    sed_cmd=-n
    for row in $rows_with_popular; do
      sed_cmd="$sed_cmd -e ${row}p"
    done
    lines=$(echo "$lines" | sed $sed_cmd)
    amount=$(echo "$lines" | wc -l)
    if [ "$amount" -eq "1" ]; then
      break
    fi
    pos=$((pos + 1))
    if [ $pos -gt $max_pos ]; then
      pos=1
    fi
  done
  echo $((2#$lines))
}

oxygen=$(count "oxygen")
scrubber=$(count "scrubber")

echo "$(( $oxygen * $scrubber ))"
