map = []
SPLITTER = "^"

file = open("input.txt", "r")
for line in file:
    row = [char for char in line.strip()]
    map.append(row)

def go_down(s, all):
    column = s[0]
    row = s[1]
    new_s = []
    for i in range(row, len(map)):
        if map[i][column] == SPLITTER:
            if not (column - 1, i + 1) in all:
                all.add((column - 1, i + 1))
                new_s.append((column - 1, i + 1))
            if not (column + 1, i + 1) in all:
                all.add((column + 1, i + 1))
                new_s.append((column + 1, i + 1))
            break
    return new_s

starts = []
all_no_duplicate_starts = set()

# first start
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "S":
            starts.append((j, i))
            all_no_duplicate_starts.add((j, i))

split_counter = 0

while len(starts) > 0:
    s = starts.pop()
    new_starts = go_down(s, all_no_duplicate_starts)
    if len(new_starts) > 0:
        split_counter += 1
    starts.extend(new_starts)

print(split_counter)