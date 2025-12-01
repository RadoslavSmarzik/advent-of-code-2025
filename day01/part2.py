LEFT = "L"

instructions = []

file = open("input.txt", "r")
for line in file:
    instructions.append(line.strip())

old = None
current = 50
zero_counter = 0

for instruction in instructions:
    old = current
    direction = instruction[0]
    number = int(instruction[1:])
    zero_counter += number // 100
    if direction == LEFT:
        current -= number % 100
    else:
        current += number % 100
    if old != 0:
        if current >= 100:
            zero_counter += 1
        if current <= 0:
            zero_counter += 1
    current = current % 100

print(zero_counter)