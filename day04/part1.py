ROLL = "@"

map = []

def is_accessible(y, x, map):
    adjacent_rolls_count = 0

    if x - 1 >= 0:
        if map[y][x-1] == ROLL:
            adjacent_rolls_count += 1

    if x + 1 < len(map[y]): 
        if map[y][x+1] == ROLL:
            adjacent_rolls_count += 1

    if y - 1 >= 0:
        if x - 1 >= 0:
            if map[y-1][x-1] == ROLL:
                adjacent_rolls_count += 1

        if map[y-1][x] == ROLL:
            adjacent_rolls_count += 1

        if x + 1 < len(map[y]): 
            if map[y-1][x+1] == ROLL:
                adjacent_rolls_count += 1

    if y + 1 < len(map): 
        if x - 1 >= 0:
            if map[y+1][x-1] == ROLL:
                adjacent_rolls_count += 1

        if map[y+1][x] == ROLL:
            adjacent_rolls_count += 1

        if x + 1 < len(map[y]): 
            if map[y+1][x+1] == ROLL:
                adjacent_rolls_count += 1
                
    return adjacent_rolls_count < 4

file = open("input.txt", "r")
for line in file:
    row = [x for x in line.strip()]
    map.append(row)

accessible_rolls_count = 0

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == ROLL and is_accessible(i, j, map):
            accessible_rolls_count += 1

print(accessible_rolls_count)