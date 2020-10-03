"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        self.reg = [0] * 8
        self.reg[7] = 0xF4
        self.ram = [0] * 256
        self.pc = 0 #program counter
        self.ir = 0 #instruction register
        self.fl = [0] * 8 #Flags
        self.halted = False
        
    def ram_read(self,MAR):
        #takes in an address, and returns the value stored there
        return self.ram[MAR]
        

    def ram_write(self,MAR,MDR):
        #takes in an address MAR and data to write there MDR, then writes data to address
        self.ram[MAR] = MDR




    def load(self,file):
        """Load a program into memory."""
        program = []
        try:
            with open(file) as f:
                for line in f:
                    program.append(line.split('#')[0].split())
        except:
            print('file not found')
            sys.exit(1)            



        address = 0

        # For now, we've just hardcoded a program:

        #program = [
            # From print8.ls8
            #0b10000010, # LDI R0,8
            #0b00000000,
            #0b00001000,
            #0b01000111, # PRN R0
            #0b00000000,
            #0b00000001, # HLT
        #]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == 0b10100000: #ADD
            self.reg[reg_a] += self.reg[reg_b]
            self.pc += 3
        #elif op == "SUB": etc
        elif op == "AND":
            pass
        elif op == "CALL":
            pass
        elif op == "CMP":
            pass
        elif op == "DEC":
            pass
        
        elif op == "DIV":
            pass
        elif op == 0b00000001: #HLT
            self.halted = True
            self.pc += 1
        elif op == "INC":
            pass
        elif op == "INT":
            pass
        elif op == "IRET":
            pass
        elif op == "JEQ":
            pass
        elif op == "JGE":
            pass
        elif op == "JGT":
            pass
        elif op == "JLE":
            pass
        elif op == "JLT":
            pass
        elif op == "JMP":
            pass
        elif op == "JNE":
            pass
        elif op == "LD":
            pass
        elif op == 0b10000010: #LDI
            #sets the value of a register to an integer
            self.reg[reg_a] = reg_b
            self.pc +=3
            
        elif op == "MOD":
            pass
        elif op == 0b10100010 :#MUL
            self.reg[reg_a] *= self.reg[reg_b]
            self.pc += 3
        elif op == "NOP":
            pass
        elif op == "NOT":
            pass
        elif op == "OR":
            pass
        elif op == "POP":
            pass
        elif op == "PRA":
            pass
        elif op == 0b01000111: #PRN
            print(self.reg[reg_a])
            self.pc += 2
        elif op == "PUSH":
            pass
        elif op == "RET":
            pass
        elif op == "SHL":
            pass
        elif op == "SHR":
            pass
        elif op == "ST":
            pass
        elif op == 0b10100001: #SUB
            self.reg[reg_a] -= self.reg[reg_b]
            self.pc += 2
        elif op == "XOR":
            pass
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        while not self.halted :#HLT#<<This is probably not right
            self.ir = self.ram_read(self.pc)#copy the register value into the instruction register
            operand_a = self.ram_read(self.pc+1)
            operand_b = self.ram_read(self.pc+2)
            self.alu(self.ir,operand_a,operand_b)
            #self.pc +=1

curr_file = "ls8/examples/mult.ls8"        

PC1 = CPU()
PC1.load(curr_file)
PC1.run()