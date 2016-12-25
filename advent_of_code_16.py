def generate_data(initial_state, disk_length):
    data = initial_state
    while len(data) < disk_length:
        rev = data[::-1]
        b = [0 if x == 1 else 1 for x in rev]
        data = data + [0] + b
    return data

assert generate_data([1], 3) == map(int, list("100"))
assert generate_data([0], 3) == map(int, list("001"))

assert generate_data(map(int, list("11111")), 6) == map(int, list("11111000000"))
assert generate_data(map(int, list("111100001010")), 14) == map(int, list("1111000010100101011110000"))


def generate_checksum(data):
    checksum = []
    while True:
        for i in range(0, len(data) - 1, 2):
            if data[i] == data[i+1]:
                checksum.append(1)
            else:
                checksum.append(0)
        if len(checksum) % 2 != 0:
            return checksum
        else:
            data = checksum
            checksum = []


assert generate_checksum(map(int, list("110010110100"))) == map(int, list("100"))

assert generate_data(map(int, list("10000")), 20) == map(int, list("10000011110010000111110"))

def fill_disk(initial_state, disk_len):
    data = generate_data(initial_state, disk_len)[:disk_len]
    ch = generate_checksum(data)
    return ch

assert fill_disk(map(int, list("10000")), 20) == map(int, list("01100"))

print "".join(map(str, fill_disk(map(int, list("01000100010010111")), 272)))
print "".join(map(str, fill_disk(map(int, list("01000100010010111")), 35651584)))
