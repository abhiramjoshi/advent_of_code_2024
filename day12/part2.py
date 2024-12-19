grid = []

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip("\n")
        row = [c for c in line]
        grid.append(row)

# We can do a breadth first search for areas. When we come to the edge of the
# area, we will need to calculate its perimeter, and when we and the area every
# time we encounter a new area of the same letter.

# We will keep track of the seen nodes


def detect_cornor(node, grid):
    corners = {
        "TR": [(-1, 0), (0, 1), (-1, 1)],
        "TL": [(-1, 0), (0, -1), (-1, -1)],
        "BR": [(1, 0), (0, 1), (1, 1)],
        "BL": [(1, 0), (0, -1), (1, -1)],
    }

    def check_if_same_region(node, direction, grid):
        n = len(grid)
        m = len(grid[0])
        x, y = node
        nx, ny = x + direction[0], y + direction[1]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            return False
        if grid[nx][ny] != grid[x][y]:
            return False
        return True

    x, y = node
    num_corners = 0
    for corner in corners:
        if (not check_if_same_region(node, corners[corner][0], grid) and 
                not check_if_same_region(node, corners[corner][1], grid)):
            num_corners += 1
        elif (check_if_same_region(node, corners[corner][0], grid) and 
                check_if_same_region(node, corners[corner][1], grid) and
                not check_if_same_region(node, corners[corner][2], grid)):
            num_corners += 1
    return num_corners


def search_region(start, grid, seen) -> tuple[int, int, set]:
    n = len(grid)
    m = len(grid[0])
    area = 0
    num_sides = 0
    queue = [start]

    while queue:
        node = queue.pop()
        x = node[0]
        y = node[1]
        plant = grid[x][y]

        if node in seen:
            continue

        seen.add(node)

        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            if x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= m:
                continue

            if grid[x + dx][y + dy] == plant:
                queue.insert(0, (x + dx, y + dy))
            

        area += 1
        num_sides += detect_cornor(node, grid)

    return area, num_sides, seen


n = len(grid)
m = len(grid[0])
seen = set()
regions = []
for i in range(n):
    for j in range(m):
        a, p, seen = search_region((i, j), grid, seen)
        if a:
            regions.append((grid[i][j], a, p))

total = 0
for region in regions:
    total += region[1] * region[2]

print(regions)
print(total)
