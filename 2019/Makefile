CXXFLAGS = -std=c++17 -O2 -Wall -Wextra -Wshadow

all: day01 day02 day03 day04 day05 day06 day07 day08

aoc.o: aoc.cpp aoc.h
	$(CXX) $(CXXFLAGS) -c aoc.cpp

dsalgos.o: dsalgos.cpp dsalgos.h
	$(CXX) $(CXXFLAGS) -c dsalgos.cpp

day01: day01.cpp aoc.o
	$(CXX) $(CXXFLAGS) day01.cpp aoc.o -o $@

day02: day02.cpp aoc.o
	$(CXX) $(CXXFLAGS) day02.cpp aoc.o -o $@

day03: day03.cpp aoc.o dsalgos.o
	$(CXX) $(CXXFLAGS) day03.cpp aoc.o dsalgos.o -o $@

day04: day04.cpp aoc.o
	$(CXX) $(CXXFLAGS) day04.cpp aoc.o -o $@

day05: day05.cpp aoc.o
	$(CXX) $(CXXFLAGS) day05.cpp aoc.o -o $@

day06: day06.cpp aoc.o
	$(CXX) $(CXXFLAGS) day06.cpp aoc.o -o $@

day07: day07.cpp aoc.o
	$(CXX) $(CXXFLAGS) day07.cpp aoc.o -o $@

day08: day08.cpp aoc.o
	$(CXX) $(CXXFLAGS) day08.cpp aoc.o -o $@
