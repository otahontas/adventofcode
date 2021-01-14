#include "aoc.h"
#include <fstream>
#include <iostream>
#include <regex>
#include <vector>

// Helper methods not to be used outside this scope.

// Opens input stream of puzzle input for given day.
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

    // IntCode comp private methods

    // Format instruction number to string with opcode + two param modes. Third
    // param is always in immediate mode (if even used), so its mode isn't needed.
    std::string IntCodeComp::GetInstruction() {
        std::string instruction = std::to_string(tape[head]);
        int size = instruction.size();
        if (size > 4) {
            throw std::runtime_error("Unsupported instruction: " + instruction);
        }
        std::string prefix(4 - size, '0');
        return prefix + instruction;
    }
    
    // Get opcode from last two chars of instruction
    int IntCodeComp::GetOpcode(std::string &instruction) {
        return stoi(instruction.substr(2, 4));
    }

    // Get value for 1st or 2nd parameter based on param mode in instruction
    int IntCodeComp::GetParam(std::string &instruction, int param_number) {
        int mode = instruction[abs(param_number - 2)] - '0';
        switch (mode) {
            case 0: {
                return tape[tape[head + param_number]];
            }
            case 1: {
                return tape[head + param_number];
            }
            default: {
                throw std::runtime_error("Unsupported param mode: " +
                                         std::to_string(mode));
            }
        }
    }
    // Get zero, one or two parameter values based on opcode value.
    std::vector<int> IntCodeComp::GetParams(std::string &instruction) {
        int amounts[9] = {0, 2, 2, 0, 1, 2, 2, 2, 2};
        switch (amounts[opcode]) {
            case 0: {
                return std::vector<int>();
            }
            case 1: {
                return std::vector<int> { GetParam(instruction, 1) };
            }
            case 2: {
                return std::vector<int> {
                    GetParam(instruction, 1),
                    GetParam(instruction, 2),
                };
            }
            default: {
                throw std::runtime_error("Couldn't get params from opcode " +
                                         std::to_string(opcode));
            }
        }
    }
    
    void IntCodeComp::IncreasePointer() {
        int amounts[9] = {0, 4, 4, 2, 2, 0, 0, 4, 4};
        if (opcode < 1 || opcode > 8) {
            throw std::runtime_error("Can't raise pointer with opcode" +
                                     std::to_string(opcode));
        }
        head += amounts[opcode];
    }

    // IntCode comp public methods

    IntCodeComp::IntCodeComp(std::vector<int> initial_tape) {
        tape = initial_tape;
    }

    void IntCodeComp::Run() {
        state = "running";
        while (true) {
            std::string instruction = GetInstruction();
            opcode = GetOpcode(instruction);

            if (opcode == 99) {
                state = "halted";
                return;
            }
            std::vector<int> params = GetParams(instruction);

            switch (opcode) {
                case 1: {
                    tape[tape[head + 3]] = params[0] + params[1];
                    break;
                }
                case 2: {
                    tape[tape[head + 3]] = params[0] * params[1];
                    break;
                }
                case 3: {
                    if (inputs.size() == 0) {
                        state = "waiting";
                        return;
                    }
                    tape[tape[head + 1]] = inputs.front(); 
                    inputs.pop();
                    break;
                }
                case 4: {
                    outputs.push(params[0]);
                    break;
                }
                case 5: {
                    head = (params[0] != 0) ? params[1] : head + 3;
                    break;
                }
                case 6: {
                    head = (params[0] == 0) ? params[1] : head + 3;
                    break;
                }
                case 7: {
                    int value = (params[0] < params[1]) ? 1 : 0;
                    tape[tape[head + 3]] = value;
                    break;
                }
                case 8: {
                    int value = (params[0] == params[1]) ? 1 : 0;
                    tape[tape[head + 3]] = value;
                    break;
                }
                default: {
                    throw std::runtime_error("Unrecognized opcode " + 
                                             std::to_string(opcode));
                }
            }
            IncreasePointer();
        }
    }

    int IntCodeComp::ValueAtAddress(int address) {
        if (address >= (int) tape.size()) {
            throw std::runtime_error("Address out of index for tape size " + 
                                     std::to_string(tape.size()));
        }
        return tape[address];
    }

    void IntCodeComp::AddInput(int input) {
        inputs.push(input);
    }

    int IntCodeComp::GetOutput() {
        if (outputs.size() == 0) {
            throw std::runtime_error("Can't get output from an empty queue!");
        }
        int output = outputs.front();
        outputs.pop();
        return output;
    }

    bool IntCodeComp::IsHalted() {
        return state == "halted";
    }

    // Input functions
    
    std::vector<int> ReadInputToInts(int day) {
        std::regex extractor("-\\d+|\\d+");
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

    std::vector<int> ReadDigitInputToInts(int day) {
        std::regex extractor("\\d");
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

    // Parser functions
    std::vector<int> PositiveIntsFromString(std::string s) {
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
