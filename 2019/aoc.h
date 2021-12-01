#pragma once
#include <iostream>
#include <map>
#include <queue>
#include <vector>

namespace aoc {
// Holds both solutions and supports displaying them to stdout.
struct Solution {
    long long part_one = 0;
    long long part_two = 0;
    Solution();
    // Give both answers already in constructor.
    Solution(long long first, long long second);

    // Support for printing solution
    friend std::ostream& operator<<(std::ostream& os, const Solution& st);
};

// Comp simulator to run Int Code programs in different puzzles.
class IntCodeComp {
   private:
    // Private instance variables
    int opcode = 0;
    long long pointer = 0;
    long long base = 0;
    std::string state = "idle";
    std::map<long long, long long> tape;
    std::queue<long long> inputs;
    std::queue<long long> outputs;

    // Private methods to help executing instructions, documented in cpp
    // file.
    std::string GetInstruction();
    static int GetOpcode(std::string& instruction);
    long long GetParam(std::string& instruction, int param_number);
    std::vector<long long> GetParams(std::string& instruction);
    void IncreasePointer();
    void ChangeState(const std::string& input);

   public:
    // Initialize computer with tape.
    explicit IntCodeComp(const std::vector<long long>& initial_tape);

    // Run program until it halts.
    void Run();

    // Get value from memory address, or error if address is not
    // initialized.
    long long ValueAtAddress(long long address);

    // Add input
    void AddInput(long long input);

    // Get output from output queue.
    long long GetOutput();

    // Get halt status.
    bool IsHalted();
};

// Functions to read inputs for given day
std::vector<int> ReadInputToInts(int day);
std::vector<long long> ReadInputToLongs(int day);
std::vector<std::string> ReadInputToLines(int day);
std::string ReadInputToLine(int day);
std::vector<int> ReadInputToDigits(int day);

// Helper functions to reformat inputs
std::vector<int> PositiveIntsFromString(std::string s);
}  // namespace aoc
