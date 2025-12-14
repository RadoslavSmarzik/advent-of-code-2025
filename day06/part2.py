input = []

file = open("input.txt", "r")
for line in file:
    input.append((" " + line).replace("\n", "")[::-1])

operators = input[-1].split()[::-1]

def calculate_problem(problem, symbol):
    if symbol == "+":
        add_result = 0
        for i in range(len(problem)):
            add_result += problem[i]
        return add_result
    else:
        mult_result = 1
        for i in range(len(problem)):
            mult_result *= problem[i]
        return mult_result

result = 0
one_problem = []

for i in range(len(input[0])):
    one_number = ""
    for j in range(len(input) - 1):
        one_number += input[j][i]
    if not one_number.strip() == "":
        one_problem.append(int(one_number))
    else:
        result += calculate_problem(one_problem, operators.pop())
        one_problem = []

print(result)
