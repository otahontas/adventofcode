#!/usr/bin/env bash
source "./common.sh"

input=$(readinput "17")

readarray -t nums <<< "$(echo "$input" | grep -Eo "\-*[0-9]+")"
lx="${nums[0]}"
ux="${nums[1]}"
ly="${nums[2]}"
uy="${nums[3]}"

echo "Part 1: $lx $ux $ly $uy"

