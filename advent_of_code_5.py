import hashlib

ZEROES_COUNT = 5

PASSWORD_LENGTH = 8

def hash(string, number):
    m = hashlib.md5()
    m.update(string + str(number))
    return m.hexdigest()
    
def is_correct_hash(hashstr):
    return hashstr.startswith("".join([str(0) for _ in range(ZEROES_COUNT)]))

def find_password(door_id):
    password = []
    current_no = 0
    while len(password) < PASSWORD_LENGTH:
        h = hash(door_id, current_no)
        if is_correct_hash(h):
            print(current_no)
            print(h)
            password.append(h[5])
            print(password)
        current_no += 1
    return "".join(password)
    
def test():
    assert is_correct_hash(hash("abc", 3231929))
    assert find_password("abc") == "18f47a30"

test()

print(find_password("wtnhxymk"))


def is_filled(password):
    for letter in password:
        if letter is None:
            return False
    return True

def find_better_password(door_id):
    password = [None for _ in range(PASSWORD_LENGTH)]
    current_no = 0
    while not is_filled(password):
        h = hash(door_id, current_no)
        if is_correct_hash(h):
            print(current_no)
            print(h)
            try:
                index = int(h[5])
                if 0 <= index < len(password) and password[index] is None:
                    password[index] = h[6]
                print(password)
            except ValueError:
                pass
        current_no += 1
    return "".join(password)

def test_better():
    assert find_better_password("abc") == "05ace8e3"
    
test_better()

print(find_better_password("wtnhxymk"))
