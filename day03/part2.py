DIGITS = 12

def create_number(input):
    result = 0
    for i in range(len(input)):
        result += input[i] * 10**(DIGITS - i - 1)

    return result

def calculate_bank(input):
    indexes = [0] * DIGITS

    for i in range(DIGITS):
        if i == 0:
            next_index = 0
        else :
            next_index = indexes[i - 1] + 1

        for j in range(next_index, len(input) - (DIGITS - i) + 1):
            if input[j] > input[next_index]:
                next_index = j
        indexes[i] = next_index

    number_array = [input[i] for i in indexes]
    return create_number(number_array)
    
banks = []

file = open("input.txt", "r")
for line in file:
    bank = [int(battery) for battery in line.strip()]
    banks.append(bank)

sum = 0
for bank in banks:
    sum += calculate_bank(bank)

print(sum)