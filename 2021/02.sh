#!/usr/bin/env bash
source "./common.sh"

AIM=0
X=0
Z=0

forward() {
  Z=$((Z + AIM * $1))
  X=$((X + $1))
}

up() {
  AIM=$((AIM - $1))
}

down() {
  AIM=$((AIM + $1))
}

input=$(read_input "02")

# Treat input like a "source code", i.e. list of commands. We can just eval all the
# input lines, since they're "forward", "up" or "down.
eval "$input"

first=$((AIM * X))
second=$((Z * X))
msg "Part 1: $first"
msg "Part 2: $second"
