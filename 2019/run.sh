#!/bin/sh
[ -d build/ ] || mkdir build/
make "$1" && ./build/"$1"
