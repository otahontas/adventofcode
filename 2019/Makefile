CXXFLAGS = -std=c++17 -O2 -Wall -Wextra -Wshadow

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
