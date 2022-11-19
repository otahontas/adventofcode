#!/usr/bin/env bash
# This file includes bunch of useful functions for aoc tasks

#######################################
# Set up sensible defaults for failing
#######################################
set -Eeuo pipefail

#######################################
# Set up globals
#######################################
SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd -P)

#######################################
# Set up colours for output if terminal supports it
#######################################
setup_colors() {
  if [[ -t 2 ]] && [[ -z "${NO_COLOR-}" ]] && [[ "${TERM-}" != "dumb" ]]; then
    NOFORMAT='\033[0m' RED='\033[0;31m' GREEN='\033[0;32m' ORANGE='\033[0;33m' BLUE='\033[0;34m' PURPLE='\033[0;35m' CYAN='\033[0;36m' YELLOW='\033[1;33m'
  else
    NOFORMAT='' RED='' GREEN='' ORANGE='' BLUE='' PURPLE='' CYAN='' YELLOW=''
  fi
}
setup_colors

#######################################
# Send messages to stderr stream and support special sequences, like colors. Use this to
# print everything that is not a script output, such as logs and messages. Sets color
# always back to noformat after printing message.
#
# Usage: msg "${RED}This is a red message"
# ARGUMENTS:
#   $1: Message to print
# OUTPUTS:
#   String to stderr
#######################################
msg() {
  echo >&2 -e "${1-}${NOFORMAT}"
}

#######################################
# Fail with a message. Defaults to error code 1, but can be overridden.
# ARGUMENTS:
#   $1: Message to print on fail
#   $2: Error code to exit with
# OUTPUTS:
#   Msg in red
# RETURN:
#   Error code
die() {
  msg "${RED}$1"
  exit "${2-1}"
}

#######################################
# Print content of given days puzzle input given a day
# ARGUMENTS:
#   $1: Day to get puzzle input for, with leading zero, eg. "01" or "10"
# OUTPUTS:
#   Write String to stdout
# RETURN:
#   0 if print succeeds, non-zero on error.
#######################################
read_input() {
  local day="$1"
  local file="$SCRIPT_DIR/inputs/d$day.txt"
  if [ -f "$file" ]; then cat "$file"; else die "File $file does not exist"; fi
}
