trap = [
    ["^", "^", "."],
    [".", "^", "^"],
    ["^", ".", "."],
    [".", ".", "^"]
]

def get_tile(triple):
    if triple in trap:
        return "^"
    return "."

test_input = "..^^."
test_2_input = ".^^.^.^^^^"
my_input = ".^^^^^.^^^..^^^^^...^.^..^^^.^^....^.^...^^^...^^^^..^...^...^^.^.^.......^..^^...^.^.^^..^^^^^...^."

def get_next_row(prev_row):
    prev = ["."] + prev_row + ["."]
    row = []
    for i in range(1, len(prev) - 1):
        triple = prev[i-1:i+2]
        row.append(get_tile(triple))
    return row


def get_n_rows(start_row, n):
    rows = [list(start_row)]
    while len(rows) < n:
        rows.append(get_next_row(rows[-1]))
    return rows

def print_rows(rows):
    r = ["".join(row) for row in rows]
    print "\n".join(r)


def safe_tiles(rows):
    return sum([len(filter(lambda x: x=='.', row)) for row in rows])

print_rows(get_n_rows(test_input, 3))

bigger = get_n_rows(test_2_input, 10)
print_rows(bigger)
assert safe_tiles(bigger) == 38

print safe_tiles(get_n_rows(my_input, 40))
print safe_tiles(get_n_rows(my_input, 400000))
