import re


class AssemBunnyInterpreter:
    def __init__(self, instruction_string, a=0, b=0, c=0, d=0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.pointer = 0
        ins = instruction_string.split('\n')
        self.instructions = [line.split() for line in ins]

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
            self.pointer += self.get_value(steps)
            self.pointer -= 1

    def tgl(self, reg):
        x = getattr(self, reg)
        toggle_map = {
            "inc": "dec",
            "dec": "inc",
            "tgl": "inc",
            "jnz": "cpy",
            "cpy": "jnz"
        }
        if self.pointer + x < len(self.instructions):
            self.instructions[self.pointer + x][0] = toggle_map[self.instructions[self.pointer + x][0]]

    def parse(self, params):
        getattr(self, params[0])(*params[1:])
        self.pointer += 1

    def run(self):
        while self.pointer < len(self.instructions):
            # print(self.instructions[self.pointer])
            self.parse(self.instructions[self.pointer])
            # print({'a': self.a, 'b': self.b, 'c': self.c, 'd': self.d})
            # print(self.instructions)
        return {'a': self.a, 'b': self.b, 'c': self.c, 'd': self.d}


test_input = """cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a"""

my_input = """cpy a b
dec b
cpy a d
cpy 0 a
cpy b c
inc a
dec c
jnz c -2
dec d
jnz d -5
dec b
cpy b c
cpy c d
dec d
inc c
jnz d -2
tgl c
cpy -16 c
jnz 1 c
cpy 83 c
jnz 78 d
inc a
inc d
jnz d -2
inc c
jnz c -5"""

assert AssemBunnyInterpreter(test_input).run()['a'] == 3
# print AssemBunnyInterpreter(my_input, a=7).run()
print AssemBunnyInterpreter(my_input, a=12).run()
