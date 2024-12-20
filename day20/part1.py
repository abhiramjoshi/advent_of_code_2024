from heapq import heappush, heappop

grid = []
with open("test_input.txt", "r") as f:
    for line in f:
        line = line.strip("\n")
        row = [char for char in line]
        grid.append(row)

n = len(grid)
m = len(grid[0])


def find_position(tile: str = "S") -> tuple[int, int]:
    for i in range(n):
        for j in range(m):
            if grid[i][j] == tile:
                return i, j
    return 0, 0

def find_walls(grid):
    n = len(grid)
    m = len(grid[0])
    
    walls = []
    for i in range(1,n-1):
        for j in range(1,m-1):
            if grid[i][j] == '#':
                walls.append((i,j))
    return walls

def djikstras(start, end, grid):
    n = len(grid)
    m = len(grid[0])
    
    # for i in range(n):
    #     for j in range(m):
    #         print(grid[i][j], end=" ")
    #     print()

    dist = []
    for i in range(n):
        dist.append([])
        for _ in range(m):
            dist[i].append(float("inf"))

    dist[start[0]][start[1]] = 0

    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    visited = set()
    queue = [(0, start)]

    while queue:
        score, node = heappop(queue)
        x, y = node

        if node in visited:
            continue

        if score > dist[x][y]:
            continue

        if dist[x][y] >= score:
            dist[x][y] = score

        if node == end:
            break

        visited.add(node)
        for dx, dy in dirs:
            new_score = score
            if x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= m:
                continue
            if dist[x + dx][y + dy] < new_score + 1:
                continue
            if grid[x + dx][y + dy] != "#":
                heappush(queue, (new_score + 1, (x + dx, y + dy)))
    return dist

#Need to find the best path, then we will go on that path
start = find_position("S")
end = find_position("E")

dist = djikstras(start, end, grid)
total_length = dist[end[0]][end[1]]
walls = find_walls(grid)

total_cheats = 0
cheats = {}
for wall in walls:
    wx,wy = wall
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    on_path = False
    for nx,ny in dirs:
        if grid[wx+nx][wy+ny] == '.':
            on_path = True
            break

    if not on_path:
        continue
    
    cheat_grid = grid.copy()
    cheat_grid[wx][wy] = "."
    cheat = djikstras(start, end, cheat_grid)
    cheat_length = cheat[end[0]][end[1]]
    if total_length-cheat_length in cheats:
        cheats[total_length-cheat_length] += 1
    else:
        cheats[total_length-cheat_length] = 1
    cheat_grid[wx][wy] = "#"
    if total_length - cheat_length >= 100:
        total_cheats += 1

print(cheats)
print("Cheats saving 100ps: ", total_cheats)
# Remove one internal wall at a time and run djikstras to see if you get a
# smaller answer.
