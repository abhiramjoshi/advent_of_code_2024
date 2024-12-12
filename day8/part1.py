grid = []

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip("\n")
        row = [c for c in line]
        grid.append(row)

# print(grid)


def calculate_valid_antinodes(a1, a2, n, m):
    slope = (abs(a2[0] - a1[0]), abs(a2[1] - a1[1]))
    
    antinodes = []

    node1 = [0,0]
    node2 = [0,0]
    if a1[0] < a2[0]:
        node1[0] = a1[0] - slope[0]
        node2[0] = a2[0] + slope[0]
    else:
        node1[0] = a1[0] + slope[0]
        node2[0] = a2[0] - slope[0]
    
    if a1[1] < a2[1]:
        node1[1] = a1[1] - slope[1]
        node2[1] = a2[1] + slope[1]
    else:
        node1[1] = a1[1] + slope[1]
        node2[1] = a2[1] - slope[1]
    antinodes += [tuple(node1), tuple(node2)]

    i = 0
    while i < len(antinodes):
        if antinodes[i][0] < 0 or antinodes[i][0] >= n:
            antinodes.pop(i)
            continue
        if antinodes[i][1] < 0 or antinodes[i][1] >= m:
            antinodes.pop(i)
            continue
        i += 1

    return antinodes


# Find all antennas
n = len(grid)
m = len(grid[0])

antennas = {}
for i in range(n):
    for j in range(m):
        ch = grid[i][j]
        if ch == ".":
            continue

        if ch in antennas:
            antennas[ch].append((i, j))
        else:
            antennas[ch] = [(i, j)]

# Calc antinodes
all_antinodes = set()

for freq, coords in antennas.items():
    a_len = len(coords)
    for i in range(a_len - 1):
        for j in range(i + 1, a_len):
            antinodes = calculate_valid_antinodes(coords[i], coords[j], n, m)
            all_antinodes.update(antinodes)

# print(all_antinodes)
print(len(all_antinodes))
