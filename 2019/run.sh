#!/bin/sh
[ -d build/ ] || mkdir build/
make day$1 && ./build/day$1
