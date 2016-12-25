my_input = 1358

test_input = 10

current_location = (1, 1)


def f(x, y):
    return x * x + 3 * x + 2 * x * y + y + y * y


def get_field_type(x, y, magic_number):
    assert x >= 0 and y >= 0
    val = f(x, y) + magic_number
    bin_val = bin(val)[2:]  # binary in python starts with 0b...
    number_of_ones = len(filter(lambda x: x == '1', list(bin_val)))
    if number_of_ones % 2 == 0:
        return "."
    else:
        return "#"


def get_neighbours(x, y):
    return (x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)


def can_step_on(x, y, magic_number):
    if x < 0 or y < 0:
        return False
    return get_field_type(x, y, magic_number) != "#"


def find_path_in_maze(start, end, magic_number):
    if get_field_type(start[0], start[1], magic_number) == "#" or \
       get_field_type(end[0], end[1], magic_number) == "#":
        return []
    queue = [(start, [start])]
    visited = set(start)
    while queue:
        position, path = queue.pop(0)
        if position == end:
            return path
        for p in get_neighbours(*position):
            if can_step_on(p[0], p[1], magic_number) and p not in visited:
                queue.append((p, path + [p]))
                visited.add(p)
    return []


path = find_path_in_maze(current_location, (7, 4), test_input)
print("Fewest steps: {}".format(len(path) - 1))

path = find_path_in_maze(current_location, (31,39), my_input)
print("Fewest steps: {}".format(len(path) - 1))


def locations_reachable_in_steps(start, magic_number, steps):
    if get_field_type(start[0], start[1], magic_number) == "#":
        return 0
    queue = [start]
    distances = {start: 0}
    visited = set([start])
    while queue:
        position = queue.pop(0)
        distance = distances[position]
        for p in get_neighbours(*position):
            if can_step_on(p[0], p[1], magic_number) and p not in visited:
                if p in distances:
                    distances[p] = min(distances[p], distance + 1)
                else:
                    distances[p] = distance + 1
                queue.append(p)
                visited.add(p)
    return len(filter(lambda ((x, y), d): d <= steps, distances.items()))


print("Can reach {} locations".format(locations_reachable_in_steps(current_location, my_input, 50)))
