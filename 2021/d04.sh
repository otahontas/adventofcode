#!/usr/bin/env bash

winners=(31 992 31744 1015808 32505856 17318416 8659208 4329604 2164802 1082401)

IFS= readarray -d '' input < <(awk -v RS= -v ORS='\0' '1' inputs/d04.txt)

boards=()
checks=()
for board in "${input[@]:1}"; do
  boards+=("$board")
  checks+=("$(head -c 25 </dev/zero | tr '\0' "0")")
done

IFS="," read -ra nums <<<"${input[0]}"

has_won=()
last_num=()

calculate_score() {
  mode=$1
  if [ "$mode" == "first" ]; then
    index=0
  else
    index=$((${#has_won[@]} - 1))
  fi
  board_index=${has_won[index]}
  unmarked_pos=$(echo "${checks[$board_index]}" | grep -o . | grep -n "0" | awk -F':' '{print $1}')
  sed_cmd=-n
  for pos in $unmarked_pos; do
    sed_cmd="$sed_cmd -e ${pos}p"
  done
  sum=0
  board="${boards[$board_index]}"
  for i in $(echo "$board" | tr " " "\n" | sed "$sed_cmd"); do
    sum=$((sum + i))
  done
  echo "$((sum * ${last_num[$index]}))"
}

for num in "${nums[@]}"; do
  for index in "${!boards[@]}"; do
    if [[ "${has_won[*]}" =~ ${index} ]]; then
      continue
    fi
    board="${boards[$index]}"
    pos=$(echo "$board" | xargs -n1 | grep -nw "$num" | cut -d: -f1)
    if [ -n "$pos" ]; then
      checks[$index]="$(echo "${checks[$index]}" | sed "s/./1/$pos")"
    fi
    for winner in "${winners[@]}"; do
      if [ $((2#${checks[$index]} & winner)) -eq "$winner" ]; then
        has_won+=("$index")
        last_num+=("$num")
        break
      fi
    done
  done
done

echo "Part 1: $(calculate_score "first")"
echo "Part 2: $(calculate_score "last")"
