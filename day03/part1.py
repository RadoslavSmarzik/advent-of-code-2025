def calculate_bank(input):
    first_index = 0
    for i in range(len(input) - 1):
        if input[i] > input[first_index]:
            first_index = i
    
    second_index = first_index + 1
    for i in range(first_index + 1, len(input)):
        if input[i] > input[second_index]:
            second_index = i

    return input[first_index] * 10 + input[second_index]

banks = []

file = open("input.txt", "r")
for line in file:
    bank = [int(battery) for battery in line.strip()]
    banks.append(bank)

sum = 0
for bank in banks:
    sum += calculate_bank(bank)

print(sum)