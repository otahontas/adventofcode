#include "int_code_comp.h"

namespace int_code_comp {
// IntCode comp private methods.

// Format instruction number to string with opcode + three param modes.
std::string IntCodeComp::GetInstruction() {
  std::string instruction = std::to_string(tape[pointer]);
  int size = instruction.size();
  if (size > 5) {
    throw std::runtime_error("Unsupported instruction: " + instruction);
  }
  std::string prefix(5 - size, '0');
  return prefix + instruction;
}

// Get opcode from last two chars of instruction.
int IntCodeComp::GetOpcode(std::string &instruction) {
  int opcode = stoi(instruction.substr(3, 5));
  if (opcode == 99 || (opcode >= 1 && opcode <= 9)) {
    return opcode;
  }
  throw std::runtime_error("Unsupported opcode " + std::to_string(opcode));
}

// Get value or address for parameter based on param mode and opcode. Address
// for param -array holds whether to return address with given param number and
// opcode instead of value. -1 means address should be never returned.
long long IntCodeComp::GetParam(std::string &instruction, int param_number) {
  int address_for_param[9] = {3, 3, 1, -1, -1, -1, 3, 3, -1};
  int mode = instruction[abs(param_number - 3)] - '0';
  switch (mode) {
  case 0: {
    long long address = tape[pointer + param_number];
    if (address_for_param[opcode - 1] == param_number) {
      return address;
    }
    return tape[address];
  }
  case 1: {
    if (address_for_param[opcode - 1] == param_number) {
      throw std::runtime_error("Writing with immediate mode is not "
                               "supported. Instruction: " +
                               instruction);
    }
    return tape[pointer + param_number];
  }
  case 2: {
    long long address = base + tape[pointer + param_number];
    if (address_for_param[opcode - 1] == param_number) {
      return address;
    }
    return tape[address];
  }
  default: {
    throw std::runtime_error("Unsupported param mode: " + std::to_string(mode));
  }
  }
}
// Get one, two or three parameters based on opcode value. Parameters can be
// either usable values or addresses to write to. Amounts-array holds correct
// amount of params to get for each opcode.
std::vector<long long> IntCodeComp::GetParams(std::string &instruction) {
  int amounts[9] = {3, 3, 1, 1, 2, 2, 3, 3, 1};
  int amount = amounts[opcode - 1];
  std::vector<long long> params;
  for (int i = 1; i <= amount; i++) {
    params.push_back(GetParam(instruction, i));
  }
  return params;
}

// Increase pointer depending on opcode value.
void IntCodeComp::IncreasePointer() {
  long long amounts[9] = {4, 4, 2, 2, 0, 0, 4, 4, 2};
  pointer += amounts[opcode - 1];
}

// Change state of computer with some input or report error if state change not
// possible.
void IntCodeComp::ChangeState(const std::string &input) {
  if ((state == "idle" || state == "waiting") && input == "run") {
    state = "running";
    return;
  }
  if (state == "running" && input == "wait") {
    state = "waiting";
    return;
  }
  if (state == "running" && input == "halt") {
    state = "halted";
    return;
  }
  throw std::runtime_error("Illegal state change from state " + state +
                           " with input " + input);
}

// IntCode comp public methods, documented in header.

IntCodeComp::IntCodeComp(const std::vector<long long> &initial_tape) {
  for (int i = 0; i < (int)initial_tape.size(); i++) {
    tape[i] = initial_tape.at(i);
  }
}

void IntCodeComp::Run() {
  ChangeState("run");
  while (true) {
    std::string instruction = GetInstruction();
    opcode = GetOpcode(instruction);

    if (opcode == 99) {
      ChangeState("halt");
      return;
    }
    std::vector<long long> params = GetParams(instruction);

    switch (opcode) {
    case 1: {
      tape[params[2]] = params[0] + params[1];
      break;
    }
    case 2: {
      tape[params[2]] = params[0] * params[1];
      break;
    }
    case 3: {
      if (inputs.empty()) {
        ChangeState("wait");
        return;
      }
      tape[params[0]] = inputs.front();
      inputs.pop();
      break;
    }
    case 4: {
      outputs.push(params[0]);
      break;
    }
    case 5: {
      pointer = (params[0] != 0) ? params[1] : pointer + 3;
      break;
    }
    case 6: {
      pointer = (params[0] == 0) ? params[1] : pointer + 3;
      break;
    }
    case 7: {
      tape[params[2]] = (params[0] < params[1]) ? 1 : 0;
      break;
    }
    case 8: {
      tape[params[2]] = (params[0] == params[1]) ? 1 : 0;
      break;
    }
    case 9: {
      base += params[0];
      break;
    }
    default: {
      throw std::runtime_error("Unrecognized opcode " + std::to_string(opcode));
    }
    }
    IncreasePointer();
  }
}

long long IntCodeComp::ValueAtAddress(long long address) {
  long long value = tape[address];
  if (value == 0) {
    throw std::runtime_error("Address " + std::to_string(address) + " has not" +
                             "been initialized yet, would return 0.");
  }
  return value;
}

void IntCodeComp::AddInput(long long input) { inputs.push(input); }

long long IntCodeComp::GetOutput() {
  if (outputs.empty()) {
    throw std::runtime_error("Can't get output from an empty queue!");
  }
  long long output = outputs.front();
  outputs.pop();
  return output;
}

std::vector<long long> IntCodeComp::GetOutputs() {
  std::vector<long long> outputs_vector;
  while (!outputs.empty()) {
    outputs_vector.push_back(outputs.front());
    outputs.pop();
  }
  return outputs_vector;
}

bool IntCodeComp::IsHalted() { return state == "halted"; }
} // namespace int_code_comp
