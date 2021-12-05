#!/usr/bin/env bash

declare -A matrix
declare -A matrix2

while IFS= read -r line; do
  start=${line% -> *}
  dest=${line#* -> }
  IFS=',' read -r x1 y1 <<< "$start"
  IFS=',' read -r x2 y2 <<< "$dest"
  if [ "$x1" -eq "$x2" ]; then
    if [ "$y1" -gt "$y2" ]; then
      z=$y1
      y1=$y2
      y2=$z
    fi
    for i in $(seq "$y1" "$y2"); do
      matrix[$x1,$i]=$(( matrix[$x1,$i] + 1 ))
      matrix2[$x1,$i]=$(( matrix2[$x1,$i] + 1 ))
    done
  elif [ "$y1" -eq "$y2" ]; then
    if [ "$x1" -gt "$x2" ]; then
      z=$x1
      x1=$x2
      x2=$z
    fi
    for i in $(seq "$x1" "$x2"); do
      matrix[$i,$y1]=$(( matrix[$i,$y1] + 1 ))
      matrix2[$i,$y1]=$(( matrix2[$i,$y1] + 1 ))
    done
  else
    if [ "$x1" -gt "$x2" ]; then
      z=$x1
      x1=$x2
      x2=$z
      z=$y1
      y1=$y2
      y2=$z
    fi
    slope=$(( (y2 - y1) / (x2 - x1) ))
    if [ $slope -eq 1 ]; then
      for i in $(seq "$x1" "$x2"); do
        matrix2[$i,$y1]=$(( matrix2[$i,$y1] + 1 ))
        y1=$(( y1 + 1 ))
      done
    elif [ $slope -eq -1 ]; then
      for i in $(seq "$x1" "$x2"); do
        matrix2[$i,$y1]=$(( matrix2[$i,$y1] + 1 ))
        y1=$(( y1 - 1 ))
      done
    fi
  fi
done < inputs/d05.txt

echo "Part 1:"
echo "${matrix[@]}" | awk '{for (i=1; i<=NF; i++) {if ($i>1) count++}} END {print count}'
echo "Part 2:"
echo "${matrix2[@]}" | awk '{for (i=1; i<=NF; i++) {if ($i>1) count++}} END {print count}'
