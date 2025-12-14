input = []

file = open("input.txt", "r")
for line in file:
    one_line = line.split()
    input.append(one_line)

result = 0

for i in range(len(input[0])):
    if input[len(input) - 1][i] == "+":
        add_result = 0
        for j in range(len(input) - 1):
            add_result += int(input[j][i])
        result += add_result
    else:
        mult_result = 1
        for j in range(len(input) - 1):
            mult_result *= int(input[j][i])
        result += mult_result

print(result)
    
    