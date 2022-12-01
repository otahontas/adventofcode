#!/usr/bin/env bash

rounds() {
  declare -A lives
  declare -A tmplives
  IFS="," read -r -a array <<< "$(<inputs/d06.txt)"
  for val in "${array[@]}"; do lives[$val]=$((lives[$val]+1)); done

  for _ in $(seq 1 "$1"); do
    tmplives=() && for i in "${!lives[@]}"; do
      if [[ $i -eq 0 ]]; then
        tmplives[6]=$((tmplives[6] + lives[0]))
        tmplives[8]=$((tmplives[8] + lives[0]))
      else
        tmplives[$((i-1))]=$((lives[$i]))
      fi
    done
    lives=() && for k in "${!tmplives[@]}"; do lives[$k]=${tmplives[$k]}; done
  done

  local sum=0
  for i in "${!lives[@]}"; do sum=$((sum+lives[$i])); done
  echo "sum: $sum"
}

rounds 80
rounds 256
