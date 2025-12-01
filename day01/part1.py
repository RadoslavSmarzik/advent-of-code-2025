LEFT = "L"

instructions = []

file = open("input.txt", "r")
for line in file:
    instructions.append(line.strip())

current = 50
zero_counter = 0

for instruction in instructions:
    direction = instruction[0]
    number = int(instruction[1:])
    if direction == LEFT:
        current -= number
    else:
        current += number
    current = current % 100
    if current == 0:
        zero_counter += 1

print(zero_counter)