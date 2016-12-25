import itertools

def swap(inp, i1, i2):
    if i1 < len(inp) and i2 < len(inp):
        inp[i1], inp[i2] = inp[i2], inp[i1]
    return inp

def rotate_right(inp, i):
    return inp[-i:] + inp[:-i]

def rotate_left(inp, i):
    return inp[i:] + inp[:i]

def parse_line(line, password):
    line = line.split()
    # print(line)
    if line[0] == "swap" and line[1] == "position":
        x, y = int(line[2]), int(line[5])
        return swap(password, x, y)
    if line[0] == "swap" and line[1] == "letter":
        x = password.index(line[2])
        y = password.index(line[5])
        return swap(password, x, y)
    if line[0] == "rotate" and line[1] == "right":
        x = int(line[2])
        return rotate_right(password, x)
    if line[0] == "rotate" and line[1] == "left":
        x = int(line[2])
        return rotate_left(password, x)
    if line[0] == "rotate" and line[1] == "based":
        x = line[6]
        index = "".join(password).find(x)
        if index >= 0:
            if index >= 4:
                index += 1
            rotate = (1 + index) % len(password)
            return rotate_right(password, rotate)
        return password
    if line[0] == "reverse":
        x = int(line[2])
        y = int(line[4])
        return password[:x] + (password[x:y+1])[::-1] + password[y+1:]
    if line[0] == "move":
        x = int(line[2])
        y = int(line[5])
        letter = password[x]
        removed = password[:x] + password[x+1:]
        return removed[:y] + [letter] + removed[y:]
    else:
        raise Exception("Cannot parse instructions in line {}".format(line))


def scramble_pass(password, input_string):
    lines = input_string.split('\n')
    password = list(password)
    for line in lines:
        password = parse_line(line, password)
    return "".join(password)

def unscramble_pass(password, input_string):
    lines = input_string.split('\n')[::-1]
    for start in itertools.permutations(password):
        if scramble_pass(start, input_string) == password:
            return start


test_pass = "abcde"
test_input = """swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d"""

my_pass = "abcdefgh"
my_input = """rotate right 3 steps
swap letter b with letter a
move position 3 to position 4
swap position 0 with position 7
swap letter f with letter h
rotate based on position of letter f
rotate based on position of letter b
swap position 3 with position 0
swap position 6 with position 1
move position 4 to position 0
rotate based on position of letter d
swap letter d with letter h
reverse positions 5 through 6
rotate based on position of letter h
reverse positions 4 through 5
move position 3 to position 6
rotate based on position of letter e
rotate based on position of letter c
rotate right 2 steps
reverse positions 5 through 6
rotate right 3 steps
rotate based on position of letter b
rotate right 5 steps
swap position 5 with position 6
move position 6 to position 4
rotate left 0 steps
swap position 3 with position 5
move position 4 to position 7
reverse positions 0 through 7
rotate left 4 steps
rotate based on position of letter d
rotate left 3 steps
swap position 0 with position 7
rotate based on position of letter e
swap letter e with letter a
rotate based on position of letter c
swap position 3 with position 2
rotate based on position of letter d
reverse positions 2 through 4
rotate based on position of letter g
move position 3 to position 0
move position 3 to position 5
swap letter b with letter d
reverse positions 1 through 5
reverse positions 0 through 1
rotate based on position of letter a
reverse positions 2 through 5
swap position 1 with position 6
swap letter f with letter e
swap position 5 with position 1
rotate based on position of letter a
move position 1 to position 6
swap letter e with letter d
reverse positions 4 through 7
swap position 7 with position 5
swap letter c with letter g
swap letter e with letter g
rotate left 4 steps
swap letter c with letter a
rotate left 0 steps
swap position 0 with position 1
reverse positions 1 through 4
rotate based on position of letter d
swap position 4 with position 2
rotate right 0 steps
swap position 1 with position 0
swap letter c with letter a
swap position 7 with position 3
swap letter a with letter f
reverse positions 3 through 7
rotate right 1 step
swap letter h with letter c
move position 1 to position 3
swap position 4 with position 2
rotate based on position of letter b
reverse positions 5 through 6
move position 5 to position 3
swap letter b with letter g
rotate right 6 steps
reverse positions 6 through 7
swap position 2 with position 5
rotate based on position of letter e
swap position 1 with position 7
swap position 1 with position 5
reverse positions 2 through 7
reverse positions 5 through 7
rotate left 3 steps
rotate based on position of letter b
rotate left 3 steps
swap letter e with letter c
rotate based on position of letter a
swap letter f with letter a
swap position 0 with position 6
swap position 4 with position 7
reverse positions 0 through 5
reverse positions 3 through 5
swap letter d with letter e
move position 0 to position 7
move position 1 to position 3
reverse positions 4 through 7"""

assert scramble_pass(test_pass, test_input) == "decab"
print scramble_pass(my_pass, my_input)
x = unscramble_pass("fbgdceah", my_input)
print(x)
assert scramble_pass(x, my_input) == "fbgdceah"
