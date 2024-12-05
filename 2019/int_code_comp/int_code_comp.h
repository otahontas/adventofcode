#ifndef _INT_CODE_COMP_H
#define _INT_CODE_COMP_H
#include <iostream>
#include <map>
#include <queue>

namespace int_code_comp {

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
  static int GetOpcode(std::string &instruction);
  long long GetParam(std::string &instruction, int param_number);
  std::vector<long long> GetParams(std::string &instruction);
  void IncreasePointer();
  void ChangeState(const std::string &input);

public:
  // Initialize computer with tape.
  explicit IntCodeComp(const std::vector<long long> &initial_tape);

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

}; // namespace int_code_comp
#endif
