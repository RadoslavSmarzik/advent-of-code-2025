red_tiles = []

file = open("input.txt", "r")
for line in file:
    coordinates = [int(i) for i in line.split(",")]
    red_tiles.append((coordinates[0], coordinates[1]))

largest_rectangle = -1

for i in range(len(red_tiles)):
    for j in range(i + 1, len(red_tiles)):
        rectangle = (abs(red_tiles[i][0] - red_tiles[j][0]) + 1) * (abs(red_tiles[i][1] - red_tiles[j][1]) + 1)
        if rectangle > largest_rectangle:
            largest_rectangle = rectangle

print(largest_rectangle)