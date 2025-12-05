ranges = []
ingredient_ids = []

file = open("input.txt", "r")
for line in file:
    line = line.strip()
    if line == "":
        break
    r = [int(x) for x in line.split("-")]
    ranges.append(r)

for line in file:
    line = line.strip()
    ingredient_ids.append(int(line))

fresh_counter = 0

for ingredient_id in ingredient_ids:
    for r in ranges:
        if r[0] <= ingredient_id and ingredient_id <= r[1]:
            fresh_counter += 1
            break

print(fresh_counter)
