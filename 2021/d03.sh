#!/usr/bin/env bash
source "./common.sh"

input=$(read_input "03")

# Init vars
gamma=""
head=$(echo "$input" | head -n1)
line_len=${#head}
input_len=$(echo "$input"l | wc -l)
oxygen=$input
scrubber=$input

get_rating() {
  mode=$1 # oxygen or scrubber
  lines=$2
  index=$3
  # Return if solution already found
  amount_of_lines=$(echo "$lines" | wc -l)
  if [[ amount_of_lines -eq 1 ]]; then
    echo "$lines"
    return
  fi

  # Grep by matching which rows have matching number in col
  lines_with_zeros=$(echo "$lines" | grep -E "^[0-1]{$index}0")
  lines_with_ones=$(echo "$lines" | grep -E "^[0-1]{$index}1")
  zeros=$(echo "$lines_with_zeros" | wc -l)
  ones=$(echo "$lines_with_ones" | wc -l)

  # scrubber logic is just reverse of oxygen
  if [[ "$zeros" -gt "$ones" ]]; then
    if [[ "$mode" == "oxygen" ]]; then
      echo "$lines_with_zeros"
    else
      echo "$lines_with_ones"
    fi
  else
    if [[ "$mode" == "oxygen" ]]; then
      echo "$lines_with_ones"
    else
      echo "$lines_with_zeros"
    fi
  fi
}

# Loop through all columns
for ((i = 0; i < line_len; i++)); do

  ### Part 1 stuff
  # get amount of zeros in col
  zeros=$(echo "$input" | grep -E "^[0-1]{$i}0" -c)
  # and rest have ones
  ones=$((input_len - zeros))
  # check which num to add to gamma
  gamma=$([[ "$zeros" -gt "$ones" ]] && echo "${gamma}0" || echo "${gamma}1")

  ### Part 2 stuff
  oxygen=$(get_rating "oxygen" "$oxygen" "$i")
  scrubber=$(get_rating "scrubber" "$scrubber" "$i")
done

### Part 1 stuff
# since epsilon is just least common bits, we can flip gamma and use that
epsilon="$(echo "$gamma" | tr 01 10)"
# convert to decimal
gamma=$((2#$gamma))
epsilon=$((2#$epsilon))
# calculate ans
first=$((gamma * epsilon))
msg "Part 1: $first"

### Part 2 stuff
# convert to decimal
oxygen=$((2#$oxygen))
scrubber=$((2#$scrubber))
second=$((oxygen * scrubber))
msg "Part 2: $second"
