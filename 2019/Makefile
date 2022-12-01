CXXFLAGS = -std=c++17 -O2 -Wall -Wextra -Wshadow

all: 01 02 03 04 05 06 07 08 09 10

aoc.o: aoc.cpp aoc.h
	$(CXX) $(CXXFLAGS) -c aoc.cpp

dsalgos.o: dsalgos.cpp dsalgos.h
	$(CXX) $(CXXFLAGS) -c dsalgos.cpp

01: 01.cpp aoc.o
	$(CXX) $(CXXFLAGS) 01.cpp aoc.o -o build/$@

02: 02.cpp aoc.o
	$(CXX) $(CXXFLAGS) 02.cpp aoc.o -o build/$@

03: 03.cpp aoc.o dsalgos.o
	$(CXX) $(CXXFLAGS) 03.cpp aoc.o dsalgos.o -o build/$@

04: 04.cpp aoc.o
	$(CXX) $(CXXFLAGS) 04.cpp aoc.o -o build/$@

05: 05.cpp aoc.o
	$(CXX) $(CXXFLAGS) 05.cpp aoc.o -o build/$@

06: 06.cpp aoc.o
	$(CXX) $(CXXFLAGS) 06.cpp aoc.o -o build/$@

07: 07.cpp aoc.o
	$(CXX) $(CXXFLAGS) 07.cpp aoc.o -o build/$@

08: 08.cpp aoc.o
	$(CXX) $(CXXFLAGS) 08.cpp aoc.o -o build/$@

09: 09.cpp aoc.o
	$(CXX) $(CXXFLAGS) 09.cpp aoc.o -o build/$@

10: 10.cpp aoc.o dsalgos.o
	$(CXX) $(CXXFLAGS) 10.cpp aoc.o dsalgos.o -o build/$@
