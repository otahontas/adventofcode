#!/usr/bin/env bash
# 1=2
# 4=4
# 7=3
# 8=7

contains() {

}

lengths1478=(2 4 3 7)

# muut
# 6 --> 0,6,9
# 5 --> 2,3,5

# rules

# length === 5 && contains 1 alkiot --> 3
# length === 5 && contains (diff 4 - 1) alkiot --> 5
# length === 5 && ei contains 1 eikä diff (4 -1) alkiot --> 2

# length === 6 && contains 4 alkiot --> 9
# length === 6 && 6 contains tämän alkiot --> 5
# length === 6 && ei contains 1 eikä 4 --> 0

count=0
declare -A lengths
lengths[1]=2
lengths[4]=4
lengths[7]=3
lengths[8]=7

while IFS="|" read -r patterns_str output; do
  unset mappings
  declare -A mappings
  IFS=" " read -r -a patterns <<< "$patterns_str"
  len_five=()
  len_six=()

  for pattern in "${patterns[@]}"; do
    for num in "${!lengths[@]}"; do
      if [[ "${#pattern}" -eq "${lengths[$num]}"  ]]; then
        mappings[$num]=$pattern
      fi
    done
    if [[ "${#pattern}" -eq 5  ]]; then
      len_five+=("$pattern")
    elif [[ "${#pattern}" -eq 6  ]]; then
      len_six+=("$pattern")
    fi
  done

  for key in "${!mappings[@]}"; do
    echo "key : $key"
    echo "value : ${mappings[$key]}"
  done
  IFS=" " read -r -a array <<< "$output"
  for i in "${array[@]}"; do
    [[ " ${lengths1478[*]} " =~ ${#i} ]] && count=$((count+1))
  done
done < inputs/d08.txt
echo "Part 1: $count"

