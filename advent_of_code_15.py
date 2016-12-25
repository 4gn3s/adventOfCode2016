import re

test_input = """Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1."""

def parse_input(input_string):
    discs = []
    for line in input_string.split("\n"):
        d_id, positions, t, pt = re.findall("Disc #(\d+) has (\d+) positions; at time=(\d+), it is at position (\d+).", line)[0]
        discs.append({
            "id": d_id,
            "total": int(positions),
            "time": int(t),
            "pos_in_time": int(pt),
        })
    return discs

def get_position_in_time(t, pt, total, time):
    return (pt + (time - t)) % total

def simulate(discs, time):
    for disc in discs:
        time += 1
        pos = get_position_in_time(disc["time"], disc["pos_in_time"],
                                   disc["total"], time)
        if pos != 0:
            return False
    return True

def find_perfect_moment(discs):
    time = 0
    while not simulate(discs, time):
        time += 1
    return time

test_discs = parse_input(test_input)
assert simulate(test_discs, 5)
assert not simulate(test_discs, 0)
assert find_perfect_moment(test_discs) == 5

my_input = """Disc #1 has 13 positions; at time=0, it is at position 10.
Disc #2 has 17 positions; at time=0, it is at position 15.
Disc #3 has 19 positions; at time=0, it is at position 17.
Disc #4 has 7 positions; at time=0, it is at position 1.
Disc #5 has 5 positions; at time=0, it is at position 0.
Disc #6 has 3 positions; at time=0, it is at position 1."""

discs = parse_input(my_input)
print find_perfect_moment(discs)

discs.append({
    "id": 7,
    "total": 11,
    "time": 0,
    "pos_in_time": 0,
})
print find_perfect_moment(discs)
