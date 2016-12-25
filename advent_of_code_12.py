import re


class AssemBunnyInterpreter:
    def __init__(self, a=0, b=0, c=0, d=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.pointer = 0
        
    def get_value(self, val):
        if val in 'abcd':
            return getattr(self, val)
        return int(val)
    
    def cpy(self, src, dst):
        setattr(self, dst, self.get_value(src))
        
    def inc(self, reg):
        current = getattr(self, reg)
        setattr(self, reg, current + 1)
    
    def dec(self, reg):
        current = getattr(self, reg)
        setattr(self, reg, current - 1)
        
    def jnz(self, t, steps):
        if self.get_value(t) != 0:
            self.pointer += int(steps)
            self.pointer -= 1
            
    def parse(self, line):
        params = line.split()
        getattr(self, params[0])(*params[1:])
        self.pointer += 1
        
    def run(self, instruction_string):
        instructions = instruction_string.split('\n')
        while self.pointer < len(instructions):
            self.parse(instructions[self.pointer])
        return {'a': self.a, 'b': self.b, 'c': self.c, 'd': self.d}


test_input = """cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a"""

my_input = """cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 16 c
cpy 17 d
inc a
dec d
jnz d -2
dec c
jnz c -5"""


assert AssemBunnyInterpreter().run(test_input) == {'a': 42, 'b': 0, 'c': 0, 'd': 0}
print AssemBunnyInterpreter().run(my_input)
print AssemBunnyInterpreter(c=1).run(my_input)
