#pragma once
#include <iostream>
#include <queue>
#include <vector>

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
            int opcode = 0;
            std::string state = "idle";
            std::vector<int> tape;
            std::queue<int> inputs;
            std::queue<int> outputs;

            // Private methods to help executing instructions
            std::string GetInstruction();
            int GetOpcode(std::string &instruction);
            int GetParam(std::string &instruction, int param_number);
            std::vector<int> GetParams(std::string &instruction);
            void IncreasePointer();

        public:
            // Initialize Int Code computer with tape.
            IntCodeComp(std::vector<int> initial_tape);

            // Run program until it halts.
            void Run();

            // Get value from memory address.
            int ValueAtAddress(int address);

            // Add input 
            void AddInput(int input);

            // Get output
            int GetOutput();

            // Get computer status
            bool IsHalted();

    };

    // Functions to read inputs for given day
    std::vector<int> ReadInputToInts(int day);
    std::vector<std::string> ReadInputToLines(int day);
    std::string ReadInputToLine(int day);
    std::vector<int> ReadDigitInputToInts(int day);

    // Helper functions to reformat inputs 
    std::vector<int> PositiveIntsFromString(std::string s);
}
