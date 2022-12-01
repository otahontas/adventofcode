#!/usr/bin/env bash
source "./common.sh"
input=$(read_input "04")

# To make this a bit easier to work with, we handle each board as a 25-bit number.
# The first 5 bits are the first row, the next 5 bits are the second row, and so on.
#
# So we can create winner boards
winners_bin=(
  "1111100000000000000000000" # first row
  "0000011111000000000000000" # second row
  "0000000000111110000000000" # third row
  "0000000000000001111100000" # fourth row
  "0000000000000000000011111" # fifth row
  "1000001000001000001000001" # first column
  "0100000100000100000100000" # second column
  "0010000010000010000010000" # third column
  "0001000001000001000001000" # fourth column
  "0000100000100000100000100" # fifth column
)

winners=()
for winner in "${winners_bin[@]}"; do
  winners+=("$(echo "ibase=2; $winner" | bc)")
done

# Parse nums from input:
# - IFS = Internal Field Separator, using comma instead of the default space/tab/newline
# - read -a = read into an array
# - read -r = do not let backslashes escape anything
IFS="," read -r -a nums <<<"$(echo "$input" | head -1)"

for line in 
# Parse boards:
# - awk RS='\n\n' = split by two newlines
# - awk {print $0"LB"} = print current line followed by literal "LB" (just a separator)
# - tr -d '\n' = remove all newlines
# - awk RS='LB' = split by LB
#
# Then read flattened boards into array, without separator (IFS= )
#flattened="$(echo "$input" | tail -n+3 | awk -v RS='\n\n' '{print $0"LB"}' | tr -d '\n' | awk -v RS='LB' '{print $0"\n"}')"

echo "all boards: ${#boards[@]}"

# for board in "${boards[@]}"; do
# echo "BOARD"
# echo "$board"
# done

#boards=()
#board=""
# while read -r line; do
#   if [[ -z "$line" ]]; then
#     boards+=("$board")
#   else
#     board="$board$line"
#   fi
# done <<<"$input"

#
# boards=()
# checks=()
# for board in "${input[@]:1}"; do
#   boards+=("$board")
#   checks+=("$(head -c 25 </dev/zero | tr '\0' "0")")
# done
#
# IFS="," read -ra nums <<<"${input[0]}"
#
# has_won=()
# last_num=()
#
# calculate_score() {
#   mode=$1
#   if [ "$mode" == "first" ]; then
#     index=0
#   else
#     index=$((${#has_won[@]} - 1))
#   fi
#   board_index=${has_won[index]}
#   unmarked_pos=$(echo "${checks[$board_index]}" | grep -o . | grep -n "0" | awk -F':' '{print $1}')
#   sed_cmd=-n
#   for pos in $unmarked_pos; do
#     sed_cmd="$sed_cmd -e ${pos}p"
#   done
#   sum=0
#   board="${boards[$board_index]}"
#   for i in $(echo "$board" | tr " " "\n" | sed "$sed_cmd"); do
#     sum=$((sum + i))
#   done
#   echo "$((sum * ${last_num[$index]}))"
# }
#
# for num in "${nums[@]}"; do
#   for index in "${!boards[@]}"; do
#     if [[ "${has_won[*]}" =~ ${index} ]]; then
#       continue
#     fi
#     board="${boards[$index]}"
#     pos=$(echo "$board" | xargs -n1 | grep -nw "$num" | cut -d: -f1)
#     if [ -n "$pos" ]; then
#       checks[$index]="$(echo "${checks[$index]}" | sed "s/./1/$pos")"
#     fi
#     for winner in "${winners[@]}"; do
#       if [ $((2#${checks[$index]} & winner)) -eq "$winner" ]; then
#         has_won+=("$index")
#         last_num+=("$num")
#         break
#       fi
#     done
#   done
# done
#
# echo "Part 1: $(calculate_score "first")"
# echo "Part 2: $(calculate_score "last")"
