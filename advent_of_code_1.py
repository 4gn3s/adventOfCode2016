def parse_input(input_list):
    steps = []
    for entry in input_list:
        if len(entry) < 2:
            raise Error("Input incorrect")
        steps.append({"dir": entry[0], "steps": int(entry[1:])})
    return steps
    
def rotate(current, next_dir):
    if next_dir != 'L' and next_dir != 'R':
        raise Error("Incorrect direction")
    if current == 'N':
        return 'W' if next_dir == 'L' else 'E'
    elif current == 'S':
        return 'E' if next_dir == 'L' else 'W'
    elif current == 'E':
        return 'N' if next_dir == 'L' else 'S'
    elif current == 'W':
        return 'S' if next_dir == 'L' else 'N'
    else:
        raise Error("Incorrect direction")
        
def move_in_dir(direction, current_pos, steps):
    pos = current_pos
    if direction == 'N':
        pos = (pos[0] - steps, pos[1])
    if direction == 'S':
        pos = (pos[0] + steps, pos[1])
    if direction == 'E':
        pos = (pos[0], pos[1] + steps)
    if direction == 'W':
        pos = (pos[0], pos[1] - steps)
    return pos
    
def distance(from_pos, to_pos):
    return abs(from_pos[0] - to_pos[0]) + abs(from_pos[1] - to_pos[1])

def headquarters_distance(input_list):
    moves = parse_input(input_list)
    current = 'N'
    current_pos = (0, 0)
    for move in moves:
        current = rotate(current, move["dir"])
        current_pos = move_in_dir(current, current_pos, move["steps"])
    return distance((0, 0), current_pos)

def test_1(input_list, result):
    assert headquarters_distance(input_list) == result

test_1(['R2', 'L3'], 5)
test_1(['R2', 'R2', 'R2'], 2)
test_1(['R5', 'L5', 'R5', 'R3'], 12)

my_input = ['R3', 'L5', 'R2', 'L1', 'L2', 'R5', 'L2', 'R2', 'L2', 
'L2', 'L1', 'R2', 'L2', 'R4', 'R4', 'R1', 'L2', 'L3', 'R3', 'L1', 'R2', 'L2', 'L4', 
'R4', 'R5', 'L3', 'R3', 'L3', 'L3', 'R4', 'R5', 'L3', 'R3', 'L5', 'L1', 'L2', 'R2',
 'L1', 'R3', 'R1', 'L1', 'R187', 'L1', 'R2', 'R47', 'L5', 'L1', 'L2', 'R4', 'R3', 
 'L3', 'R3', 'R4', 'R1', 'R3', 'L1', 'L4', 'L1', 'R2', 'L1', 'R4', 'R5', 'L1', 'R77', 
 'L5', 'L4', 'R3', 'L2', 'R4', 'R5', 'R5', 'L2', 'L2', 'R2', 'R5', 'L2', 'R194', 'R5', 
 'L2', 'R4', 'L5', 'L4', 'L2', 'R5', 'L3', 'L2', 'L5', 'R5', 'R2', 'L3', 'R3', 'R1',
 'L4', 'R2', 'L1', 'R5', 'L1', 'R5', 'L1', 'L1', 'R3', 'L1', 'R5', 'R2', 'R5', 'R5', 
 'L4', 'L5', 'L5', 'L5', 'R3', 'L2', 'L5', 'L4', 'R3', 'R1', 'R1', 'R4', 'L2', 'L4', 'R5',
  'R5', 'R4', 'L2', 'L2', 'R5', 'R5', 'L5', 'L2', 'R4', 'R4', 'L4', 'R1', 'L3', 'R1', 
  'L1', 'L1', 'L1', 'L4', 'R5', 'R4', 'L4', 'L4', 'R5', 'R3', 'L2', 'L2', 'R3', 'R1', 
  'R4', 'L3', 'R1', 'L4', 'R3', 'L3', 'L2', 'R2', 'R2', 'R2', 'L1', 'L4', 'R3', 'R2', 
  'R2', 'L3', 'R2', 'L3', 'L2', 'R4', 'L2', 'R3', 'L4', 'R5', 'R4', 'R1', 'R5', 'R3']

print(headquarters_distance(my_input))

def find_steps(prev_pos, cur_pos):
    if prev_pos[0] != cur_pos[0]:
        assert prev_pos[1] == cur_pos[1]
        if prev_pos[0] < cur_pos[0]:
            return [(x, prev_pos[1]) for x in range(prev_pos[0] + 1, cur_pos[0] + 1)]
        else:
            return [(x, prev_pos[1]) for x in range(prev_pos[0] - 1, cur_pos[0] - 1, -1)]
    else:
        assert prev_pos[0] == cur_pos[0]
        if prev_pos[1] < cur_pos[1]:
            return [(prev_pos[0], x) for x in range(prev_pos[1] + 1, cur_pos[1] + 1)]
        else:
            return [(prev_pos[0], x) for x in range(prev_pos[1] - 1, cur_pos[1] - 1, -1)]

def headquarters_visited_twice_distance(input_list):
    moves = parse_input(input_list)
    current = 'N'
    start = (0, 0)
    current_pos = start
    visited = set(current_pos)
    for move in moves:
        current = rotate(current, move["dir"])
        next_pos = move_in_dir(current, current_pos, move["steps"])
        print(current_pos, next_pos)
        steps = find_steps(current_pos, next_pos)
        for step in steps:
            if step in visited:
                print(".")
                print(step)
                print(".")
                return distance(start, step)
            else:
                visited.add(step)
        current_pos = next_pos
    return distance(start, current_pos)
    
def test_2(input_list, result):
    headquarters_visited_twice_distance(input_list) == result


test_2(['R8', 'R4', 'R4', 'R8'], 4)
    
print(headquarters_visited_twice_distance(my_input))
