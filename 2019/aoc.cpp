#include "aoc.h"
#include <fstream>
#include <regex>
#include <vector>
#include <iostream>

// Opens inputstream of puzzle input for given day.
std::ifstream OpenFilestream(int day) {
    std::string day_str= day >= 10 ? std::to_string(day) : "0" + std::to_string(day);
    std::string filename = "inputs/d" + day_str + ".txt";
    std::ifstream puzzle_input(filename);
    if (!puzzle_input.is_open()) {
        throw std::runtime_error("Unable to open file with filename: " + filename);
    }
    return puzzle_input;
}

namespace aoc {
    // Solution methods
    std::ostream& operator<<(std::ostream& os, const Solution& st) {
        os << "Part 1: " << st.part_one << "\n";
        os << "Part 2: " << st.part_two << "\n";
        return os;
    };

    // IntCode Comp methods
    IntCodeComp::IntCodeComp(std::vector<int> initial_tape) {
        tape = initial_tape;
    }

    void IntCodeComp::Run() {
        while (true) {
            int opcode = tape[head];
            int input_one = tape[tape[head + 1]];
            int input_two = tape[tape[head + 2]];
            int address = tape[head + 3];
            switch (opcode) {
                case 1:
                    tape[address] = input_one + input_two;
                    break;
                case 2:
                    tape[address] = input_one * input_two;
                    break;
                case 99:
                    return;
            }
            head += 4;
        }
    }

    int IntCodeComp::ValueAtAddress(int address) {
        if (address >= (int) tape.size()) {
            std::cout << "Address out of index for tape size " <<  tape.size() << "\n";
            return 0;
        }
        return tape[address];
    }

    // Input functions
    std::vector<int> ReadInputToInts(int day) {
        std::regex extractor("\\d+");
        std::string line;
        std::vector<int> ints;
        std::ifstream puzzle_input= OpenFilestream(day);
        while (getline(puzzle_input, line)) {
            auto start = std::sregex_iterator(line.begin(), line.end(), extractor);
            auto end = std::sregex_iterator();
            for (auto iter = start; iter != end; iter++) {
                ints.push_back(stoi(iter->str()));
            }
        }
        return ints;
    }

    std::vector<std::string> ReadInputToLines(int day) {
        std::string line;
        std::vector<std::string> lines;
        std::ifstream puzzle_input = OpenFilestream(day);
        while (getline(puzzle_input, line)) {
            lines.push_back(line);
        }
        return lines;
    }

    std::string ReadInputToLine(int day) {
        std::string line;
        std::ifstream puzzle_input = OpenFilestream(day);
        getline(puzzle_input, line);
        return line;
    }


    // Helper functions
    std::vector<int> StringToInts(std::string s) {
        std::regex extractor("\\d+");
        std::vector<int> ints;
        auto start = std::sregex_iterator(s.begin(), s.end(), extractor);
        auto end = std::sregex_iterator();
        for (auto iter = start; iter != end; iter++) {
            ints.push_back(stoi(iter->str()));
        }
        return ints;
    }
}
