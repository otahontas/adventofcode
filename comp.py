from collections import deque


class Comp:
    def __init__(self, tape):
        self.tape = tape[:]
        self.tape.extend([0] * 10000)
        self.inputs = deque()
        self.outputs = deque()
        self.running = False
        self.halted = False
        self.head = 0
        self.base = 0
        self.instructions = {
            "01": "add",
            "02": "multiply",
            "03": "take_input",
            "04": "produce_output",
            "05": "jump_if_true",
            "06": "jump_if_false",
            "07": "less_than",
            "08": "equals",
            "09": "adjust_base",
            "99": "halt",
        }

    def run(self):
        if self.halted:
            print("Already halted, can't run")
            return
        self.running = True
        while self.running:
            opcode, param_modes = self.parse_opcode_and_param_modes(
                self.tape[self.head]
            )
            getattr(self, self.instructions[opcode])(param_modes)

    # === Instructions ===
    def add(self, param_modes):
        value1 = self.get_value_from_param_mode(param_modes[0], 0)
        value2 = self.get_value_from_param_mode(param_modes[1], 1)
        result = value1 + value2
        address_to_write = self.get_address_from_param_mode(param_modes[2], 2)
        self.tape[address_to_write] = result
        self.head += 4

    def multiply(self, param_modes):
        value1 = self.get_value_from_param_mode(param_modes[0], 0)
        value2 = self.get_value_from_param_mode(param_modes[1], 1)
        result = value1 * value2
        address_to_write = self.get_address_from_param_mode(param_modes[2], 2)
        self.tape[address_to_write] = result
        self.head += 4

    def take_input(self, param_modes):
        """Take input from input queue, wait for more if no input available."""
        if len(self.inputs) == 0:
            self.running = False
            return
        address_to_write = self.get_address_from_param_mode(param_modes[0], 0)
        self.tape[address_to_write] = self.inputs.popleft()
        self.head += 2

    def produce_output(self, param_modes):
        """Append output to output queue."""
        value = self.get_value_from_param_mode(param_modes[0], 0)
        self.outputs.append(value)
        self.head += 2

    def jump_if_true(self, param_modes):
        value1 = self.get_value_from_param_mode(param_modes[0], 0)
        value2 = self.get_value_from_param_mode(param_modes[1], 1)
        self.head = value2 if value1 != 0 else self.head + 3

    def jump_if_false(self, param_modes):
        value1 = self.get_value_from_param_mode(param_modes[0], 0)
        value2 = self.get_value_from_param_mode(param_modes[1], 1)
        self.head = value2 if value1 == 0 else self.head + 3

    def less_than(self, param_modes):
        value1 = self.get_value_from_param_mode(param_modes[0], 0)
        value2 = self.get_value_from_param_mode(param_modes[1], 1)
        result = 1 if value1 < value2 else 0
        address_to_write = self.get_address_from_param_mode(param_modes[2], 2)
        self.tape[address_to_write] = result
        self.head += 4

    def equals(self, param_modes):
        value1 = self.get_value_from_param_mode(param_modes[0], 0)
        value2 = self.get_value_from_param_mode(param_modes[1], 1)
        result = 1 if value1 == value2 else 0
        address_to_write = self.get_address_from_param_mode(param_modes[2], 2)
        self.tape[address_to_write] = result
        self.head += 4

    def adjust_base(self, param_modes):
        self.base += self.get_value_from_param_mode(param_modes[0], 0)
        self.head += 2

    def halt(self, param_modes):
        self.running = False
        self.halted = True

    # === Parsers ===
    def parse_opcode_and_param_modes(self, value):
        o = []
        b = str(value)[::-1]
        for p in range(5):
            try:
                o.append(int(b[p]))
            except IndexError:
                o.append(0)
        opcode = (str(o[0]) + str(o[1]))[::-1]
        param_modes = o[2:5]
        return (opcode, param_modes)

    def get_value_from_param_mode(self, param_mode, param_index):
        if param_mode == 0:
            return self.tape[self.tape[self.head + param_index + 1]]
        elif param_mode == 1:
            return self.tape[self.head + param_index + 1]
        elif param_mode == 2:
            return self.tape[self.base + self.tape[self.head + param_index + 1]]
        else:
            raise ValueError("not valid param mode")

    def get_address_from_param_mode(self, param_mode, param_index):
        if param_mode == 0:
            return self.tape[self.head + param_index + 1]
        elif param_mode == 2:
            return self.base + self.tape[self.head + param_index + 1]
        else:
            raise ValueError("not valid param mode")

    # === Input / output ===
    def print_outputs(self):
        print(list(self.outputs))

    def get_one_output(self):
        return self.outputs.popleft()

    def get_all_outputs(self):
        return self.outputs

    def add_one_input(self, value):
        self.inputs.append(value)

    def is_halted(self):
        return self.halted

    def restart(self):
        self.halted = False
