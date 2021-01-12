#pragma once
#include <vector>
#include <iostream>

namespace aoc {
    // Holds both solutions and supports displaying them to stdout.
    struct Solution {
        public:
            int part_one = 0;
            int part_two = 0;

            friend std::ostream& operator<<(std::ostream& os, const Solution& st);
    };


    class IntCodeComp {

        private:
            int head = 0;
            std::vector<int> tape;

        public:
            // Initialize Int Code computer with tape.
            IntCodeComp(std::vector<int> initial_tape);

            // Run program until it halts.
            void Run();

            // Get value from memory address.
            int ValueAtAddress(int address);
    };

    std::vector<int> ReadInputToInts(int day);
    std::vector<std::string> ReadInputToLines(int day);
}
