import hashlib

my_input = "zpqevtbw"


def find_first_repeated(how_many, string):
    assert how_many > 1
    if len(string) < how_many:
        return None
    
    prev_letter = string[0]
    current_counter = 1
    
    for letter in string[1:]:
        if current_counter == how_many:
            return prev_letter
        if letter == prev_letter:
            current_counter += 1
        else:
            current_counter = 1
            prev_letter = letter
    if current_counter == how_many:
        return prev_letter
    return None

def generate_keys(salt, key_stretching=False):
    integer = 0
    keys = []
    key_candidate_queue = []
    while len(keys) <= 64:
        key_candidate_queue = filter(lambda x: x[0] + 1000 >= integer, key_candidate_queue)
        
        seed = '{}{}'.format(salt, integer).encode()
        key_candidate = hashlib.md5(seed).hexdigest()
        
        if key_stretching:
            for _ in range(2016):
                key_candidate = hashlib.md5(key_candidate).hexdigest()
        
        repeated_letter = find_first_repeated(5, key_candidate)
        if repeated_letter is not None:
            to_add = filter(lambda c: c[1] == repeated_letter, key_candidate_queue)
            for a in to_add:
                keys.append((a[0], a[2]))
                key_candidate_queue.remove(a)

        repeated_letter = find_first_repeated(3, key_candidate)
        if repeated_letter is not None:
            key_candidate_queue.append((integer, repeated_letter, key_candidate))
            
        integer += 1
    return sorted(keys, key=lambda x: x[0])
    

assert find_first_repeated(3, "abcddeeffgggg") == 'g'

assert generate_keys("abc")[63][0] == 22728

print(generate_keys(my_input)[63][0])

print(generate_keys(my_input, True)[63][0])
