connections = []
with open("input.txt", "r") as f:
    for line in f:
        connections.append(line.strip("\n").split("-"))

adj_matrix = {}

for connection in connections:
    source = connection[0]
    dest = connection[1]

    if source in adj_matrix:
        adj_matrix[source].add(dest)
    else:
        adj_matrix[source] = {dest}

    if dest in adj_matrix:
        adj_matrix[dest].add(source)
    else:
        adj_matrix[dest] = {source}

trisets = set()

for node in adj_matrix:
    n = len(adj_matrix[node])
    set_list = list(adj_matrix[node])
    for i in range(n - 1):
        for j in range(i + 1, n):
            if set_list[j] in adj_matrix[set_list[i]]:
                tri = [node, set_list[i], set_list[j]]
                for m in tri:
                    if "t" == m[0]:
                        trisets.add(tuple(sorted([node, set_list[i], set_list[j]])))
                        #trisets.add((node, set_list[i], set_list[j]))
                        break
print(trisets)
print(len(trisets))
