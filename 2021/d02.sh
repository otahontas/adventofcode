#!/usr/bin/env bash
source "./common.sh"

AIM=0; X=0; Z=0

forward() {
  Z=$((Z + AIM * $1))
  X=$((X + $1))
}

up() {
  AIM=$(( AIM - $1 ))
}

down() {
  AIM=$(( AIM + $1 ))
}

input=$(readinput "02")

eval "$input"

first=$(( AIM * X ))
second=$(( Z * X ))
msg "Part 1: $first"
msg "Part 2: $second"
