graph = []

file = open("input.txt", "r")
for line in file:
    data = line.split(":")
    vertex = data[0].strip()
    connected_vertices = [x.strip() for x in data[1].split()]
    graph.append((vertex, connected_vertices))

graph.append(("out", []))

paths = 0

current = None

for v in graph:
    if v[0] == "you":
        current = v

def get_vertex(name):
    for v in graph:
        if v[0] == name:
            return v
    return None

def process_vertex(vertex):
    if vertex[0] == "out":
        global paths
        paths += 1
        return
    for v in vertex[1]:
        process_vertex(get_vertex(v))


process_vertex(current)

print(paths)