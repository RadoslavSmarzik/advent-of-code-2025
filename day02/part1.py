def is_invalid(number):
    string = str(number)

    # ak ma cislo neparny pocet znakov, tak je validne
    if len(string) % 2 != 0:
        False

    first_half = string[:len(string) // 2]
    second_half = string[len(string) // 2:]

    if first_half == second_half:
        return True
    
    return False

file = open("input.txt", "r")
line = file.readline()

ranges = line.split(",")

sum = 0

for r in ranges:
    corners = r.split("-")
    min_val = int(corners[0])
    max_val = int(corners[1])
    for i in range(min_val, max_val + 1):
        if is_invalid(i):
            sum += i

print(sum)