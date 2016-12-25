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

    def out(self, t):
        # print("out ", self.get_value(t))
        return self.get_value(t)

    def parse(self, line):
        params = line.split()
        ret = getattr(self, params[0])(*params[1:])
        self.pointer += 1
        return ret

    def run(self, instruction_string, max_output_length):
        instructions = instruction_string.split('\n')
        current_step = 0
        output_list = []
        while self.pointer < len(instructions):
            output = self.parse(instructions[self.pointer])
            if output is not None:
                output_list.append(output)
                if len(output_list) >= max_output_length:
                    break
        return output_list


my_input = """cpy a d
cpy 7 c
cpy 365 b
inc d
dec b
jnz b -2
dec c
jnz c -5
cpy d a
jnz 0 0
cpy a b
cpy 0 a
cpy 2 c
jnz b 2
jnz 1 6
dec b
dec c
jnz c -4
inc a
jnz 1 -7
cpy 2 b
jnz c 2
jnz 1 4
dec b
dec c
jnz 1 -4
jnz 0 0
out b
jnz a -19
jnz 1 -21"""

res = []
a = 0
while not res == list(10 * [0, 1]):
    res = AssemBunnyInterpreter(a=a).run(my_input, 20)
    a += 1
print a-1, res
