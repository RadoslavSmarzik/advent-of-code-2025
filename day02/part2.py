# funkcia rozdeli string na n rovnako dlhych casti
def split_into_n_parts(string, n):
    parts = []

    part_length = int(len(string) / n)

    for i in range(n):
        parts.append(string[i * part_length : (i +1) * part_length ])

    return parts

def are_same(parts):
    first = parts[0]

    for part in parts:
        if part != first:
            return False
    
    return True

# funkcia overi, ci sa v stringu nachadza n-krat rovnaky pattern
def has_n_same_parts(string, n):
    length = len(string)

    # ak dlzka nie je delitelna poctom dielov, tak nemoze obsahovat n-krat pattern
    if length % n != 0:
        return False

    parts = split_into_n_parts(string, n)
    if are_same(parts):
        return True

def is_invalid(number):
    string = str(number)

    for i in range(2, len(string) + 1):
        if has_n_same_parts(string, i):
            return True
    
    return False

file = open("input.txt", "r")
line = file.readline()

ranges = line.split(",")

sum = 0

for r in ranges:
    corners = r.split("-")
    min_val = int(corners[0])
    max_val = int(corners[1])
    for i in range(min_val, max_val + 1):
        if is_invalid(i):
            print(i)
            sum += i

print(sum)