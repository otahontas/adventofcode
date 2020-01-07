class Comp:
    def __init__(self,tape):
        """ Initialize intcode computer """ 
        self.tape = tape
        self.state = 0
        self.opcode = 99
        self.param_modes = [0,0,0]
        self.instructions = { 1 : "add", 
                              2 : "multiply",
                              3 : "input", 
                              4 : "output", 
                              5 : "jump_if_true",
                              6 : "jump_if_false",
                              7 : "less_than",
                              8 : "equals", 
                              99 : "halt"}
        self.input = []
        self.output = []


    def run(self):
        """ Runs intcode computer until it halts. During each state in tape
            program parses opcode and params and calls correct method based on 
            opcode""" 
        self.parse_opcode_and_params()
        print(self.opcode)
        getattr(self, self.instructions[self.opcode])()


    def add(self):
        addr1 = tape[state+1] if self.opcodes[0] == 0 else state+1
        addr2 = tape[state+2] if self.opcodes[0] == 0 else state+2
        tape[state + 3] = tape[addr1] + tape[addr2]
        state += 4


    def multiply(self):
        addr1 = tape[state+1] if self.opcodes[0] == 0 else state+1
        addr2 = tape[state+2] if self.opcodes[0] == 0 else state+2
        tape[state + 3] = tape[addr1] * tape[addr2]
        state += 4


    def input(self):
        """ Gets input and stores it to position given by parameter """ 
        if self.input:
            addr = tape[state + 1] 
            tape[addr] = self.input.pop()
            state += 2
        else:
            return


    def output(self):
        """ Outputs value """
        addr = tape[state+1] if self.opcodes[0] == 0 else state+1
        output = tape[state + 1]
        self.output.append(output)
        state += 2

    def jump_if_true(self):
        pass


    def jump_if_false(self):
        pass


    def less_than(self):
        pass


    def equals(self):
        pass


    def halt(self):
        print("HALTING")
        return self.output.pop()

    def parse_opcode_and_params(self):
        """ Parses opcode and param_modes from current value from tape """ 
        value = self.tape[self.state]
        self.opcode = value % 100
        self.param_modes = [(value // 10 ** i) % 10 for i in range(2, 5)]
        
    def give_input(self, x):
        """ Simulate user input """ 
        self.inputs.append(x)
