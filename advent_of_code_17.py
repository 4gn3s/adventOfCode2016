import hashlib

GRID_SIZE = 4

START_POS = (0, 0)
END_POS = (3, 3)

def possible_moves(position):
    moves = list("UDLR")
    if position[1] == 0:
        moves.remove("U")
    if position[0] == 0:
        moves.remove("L")
    if position[1] == GRID_SIZE - 1:
        moves.remove("D")
    if position[0] == GRID_SIZE - 1:
        moves.remove("R")
    return moves

assert possible_moves(START_POS) == list("DR")
assert possible_moves(END_POS) == list("UL")


def get_md5(passcode, path):
    path_str = "".join(path)
    seed = '{}{}'.format(passcode, path_str).encode()
    return hashlib.md5(seed).hexdigest()[:4]

def get_moves(md5_hash):
    open_door = set("bcdef")
    moves = []
    assert len(md5_hash) == 4
    if md5_hash[0] in open_door:
        moves.append("U")
    if md5_hash[1] in open_door:
        moves.append("D")
    if md5_hash[2] in open_door:
        moves.append("L")
    if md5_hash[3] in open_door:
        moves.append("R")
    return moves

def get_end_position(path, start=START_POS):
    end = start
    for p in path:
        if p == 'U':
            end = (end[0], end[1] - 1)
        if p == 'D':
            end = (end[0], end[1] + 1)
        if p == 'L':
            end = (end[0] - 1, end[1])
        if p == 'R':
            end = (end[0] + 1, end[1])
    return end


def get_opposite_step(step):
    opposites = {"U": "D", "D": "U", "L": "R", "R": "L"}
    return opposites[step]


test_input = "hijkl"
assert get_md5(test_input, []) == "ced9"

def going_back(path, move):
    if len(path) == 0:
        return False
    last_move = path[-1]
    if get_opposite_step(last_move) == move:
        return True
    return False


def find_path(passcode):
    queue = [[]]
    while queue:
        path = queue.pop(0)
        current_position = get_end_position(path)
        if current_position == END_POS:
            return True, path
        moves = get_moves(get_md5(passcode, path))
        moves = [move for move in moves if move in possible_moves(current_position)]
        # print(path)
        # print(moves)
        for move in moves:
            queue.append(path + [move])
    return False, []


assert find_path("ihgpwlah")[1] == list("DDRRRD")
assert find_path("kglvqrro")[1] == list("DDUDRLRRUDRD")
assert find_path("ulqzkmiv")[1] == list("DRURDRUDDLLDLUURRDULRLDUUDDDRR")

print "".join(find_path("qljzarfv")[1])

def find_long_paths(passcode):
    queue = [[]]
    paths = []
    while queue:
        path = queue.pop(0)
        current_position = get_end_position(path)
        if current_position == END_POS:
            paths.append(path)
            continue
        moves = get_moves(get_md5(passcode, path))
        moves = [move for move in moves if move in possible_moves(current_position)]
        # print(path)
        # print(moves)
        for move in moves:
            queue.append(path + [move])
    return max([len(p) for p in paths])

# assert find_long_paths("ihgpwlah") == 370
# assert find_long_paths("kglvqrro") == 492
# assert find_long_paths("ulqzkmiv") == 830

print find_long_paths("qljzarfv")
