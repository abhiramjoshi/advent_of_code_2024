from collections import defaultdict

connections = []
vertices = set()
with open("input.txt", "r") as f:
    for line in f:
        connections.append(line.strip("\n").split("-"))
        vertices.update(connections[-1])

adj_matrix = defaultdict(list)

for s, d in connections:
    adj_matrix[s].append(d)
    adj_matrix[d].append(s)

print(adj_matrix)

# We need to essentially find the maximal clique


def find_clique(node):
    clique = {node}

    for vertex in adj_matrix[node]:
        c_i = clique.intersection(adj_matrix[vertex])
        if len(c_i) != len(clique):
            continue
        clique.add(vertex)

    return sorted(clique)

max_clique = []
for vertex in vertices:
    c = find_clique(vertex)
    if len(c) > len(max_clique):
        max_clique = c

print(max_clique)
print(",".join(max_clique))
