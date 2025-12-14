import math

boxes = []

file = open("input.txt", "r")
for line in file:
    box = [int(i) for i in line.split(",")]
    boxes.append(box)

def euclidean_distance(box1, box2):
    return int(math.sqrt(math.pow(box1[0] - box2[0], 2) + math.pow(box1[1] - box2[1], 2) + math.pow(box1[2] - box2[2], 2)))

distances = []

for i in range(len(boxes)):
    for j in range(len(boxes)):
        if i < j:
            distances.append((euclidean_distance(boxes[i], boxes[j]), i, j))

sorted_distances = sorted(distances, key=lambda x: x[0])

circuits = [i for i in range(len(boxes))]

def is_in_one_circuit(circuits):
    for i in range(len(circuits)):
        if circuits[i] != circuits[0]:
            return False
    return True

def put_into_same_cicruit(box_1, box_2, circuits):
    new_circuit = circuits[box_1]
    old_circuit = circuits[box_2]
    for i in range(len(circuits)):
        if circuits[i] == old_circuit:
            circuits[i] = new_circuit

for i in range(len(sorted_distances)):
    distance_tuple = sorted_distances[i]
    box_1 = distance_tuple[1]
    box_2 = distance_tuple[2]
    if circuits[box_1] != circuits[box_2]:
        put_into_same_cicruit(box_1, box_2, circuits)
        if is_in_one_circuit(circuits):
            print(boxes[box_1][0] * boxes[box_2][0])