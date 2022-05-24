#!/usr/bin/env bash
source "./common.sh"

read_packet() {
  local bits=$1
  local bits_to_read=3
  local version=""
  local type_id=""
  # Read without -r to grab the value as one uninterrupted string
  while read -n $bits_to_read c; do
    if [[ -z $version ]]; then
      version=$(( 2#$c ))
    elif [[ -z $type_id ]]; then
      type_id=$(( 2#$c ))
    else
      if [[ $type_id -eq 4 ]]; then
        echo "Version: $version"
      else [[ $type_id -eq 5 ]]
        echo "Type: $type_id"
      fi
      echo "we have packet: $version $type_id"
      return
    fi
    echo "$c"
  done <<< "$bits"
}

input=$(readinput "16")
read_packet "$(echo "ibase=16; obase=2; $input" | bc)"
