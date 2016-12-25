def get_next_elf(elves, current, total):
    if len(elves) == 1:
        return -1
    next_candidate = current + 1
    while next_candidate not in elves:
        next_candidate += 1
        if next_candidate >= total + 1:
            next_candidate = 1
    return next_candidate

def circular_elves(number_of_elves):
    elves = {i: 1 for i in range(1, number_of_elves + 1)}
    current = 1
    while True:
        if len(elves) <= 1:
            break
        next_elf = get_next_elf(elves, current, number_of_elves)
        elves[current] += elves[next_elf]
        del elves[next_elf]
        current = get_next_elf(elves, current, number_of_elves)

    print(elves)


# circular_elves(5)
# circular_elves(3004953)


class Node:
    def __init__(self, eid):
        self.id = eid
        self.next = None
        self.prev = None

    def delete(self):
        self.prev.next = self.next
        self.next.prev = self.prev


def circular_elves_smarter(number_of_elves):
    elves = [Node(i) for i in range(number_of_elves)]
    for i in range(number_of_elves):
        elves[i].prev = elves[(i - 1) % number_of_elves]
        elves[i].next = elves[(i + 1) % number_of_elves]

    start = elves[0]
    mid = elves[number_of_elves / 2]

    for i in range(number_of_elves - 1):
        tmp = mid
        mid.delete()
        mid = tmp.next
        if (number_of_elves - i) % 2 == 1:
            mid = mid.next
        start = start.next

    return start.id + 1 # elves numbered from 0


assert circular_elves_smarter(5) == 2
print circular_elves_smarter(3004953)
