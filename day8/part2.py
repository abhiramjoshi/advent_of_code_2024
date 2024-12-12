grid = []

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip("\n")
        row = [c for c in line]
        grid.append(row)

# print(grid)
def check_if_valid(node, n, m):
    x = node[0]
    y = node[1]

    if x < 0 or x >= n:
        return False

    if y < 0 or y >= m:
        return False

    return True

def calculate_valid_antinodes(a1, a2, n, m):
    slope = (a2[0] - a1[0], a2[1] - a1[1])
    
    antinodes = {a1, a2}
    #Calculate the line that goes through all the points and until we encounter
    # node that is outside our limits, we continue to calculate nodes
    for op in ["+", "-"]:
        curr = a1
        while check_if_valid(curr, n, m):
            antinodes.add(curr)
            if op == "+":
                curr = (curr[0] + slope[0], curr[1] + slope[1])
            else:
                curr = (curr[0] - slope[0], curr[1] - slope[1])
    return antinodes


antennas = {}
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
# print(all_antinodes)
print(len(all_antinodes))
