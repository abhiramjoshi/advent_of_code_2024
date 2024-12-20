from heapq import heappush, heappop
from pprint import pprint

grid = []
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip("\n")
        row = [char for char in line]
        grid.append(row)

n = len(grid)
m = len(grid[0])

def manhattan_dist(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

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
    
    parents = {start: None}
    dist = []
    for i in range(n):
        dist.append([])
        for _ in range(m):
            dist[i].append(float("inf"))

    dist[start[0]][start[1]] = 0

    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    visited = set()
    queue = [(0, start, None)]

    while queue:
        score, node, parent = heappop(queue)
        x, y = node

        if node in visited:
            continue

        if score > dist[x][y]:
            continue

        if dist[x][y] >= score:
            dist[x][y] = score
            if node in parents:
                parents[node] = parent
            else:
                parents[node] = parent

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
                heappush(queue, (new_score + 1, (x + dx, y + dy), node))
    return dist, parents

#Need to find the best path, then we will go on that path
start = find_position("S")
end = find_position("E")

dist, parents = djikstras(start, end, grid)

path = []
backtrack = end
while backtrack:
    path.insert(0, backtrack)
    backtrack=parents[backtrack]
    if backtrack is None:
        break

path_len = len(path)
max_cheat_dist = 20
cheats = {}
best_cheats = 0
for i in range(path_len):
    for j in range(path_len):
        if i == j:
            continue
        man_dist = manhattan_dist(path[i], path[j])
        if man_dist <= max_cheat_dist:
            cheat_dist = (dist[end[0]][end[1]] - dist[path[j][0]][path[j][1]] 
                            + man_dist + dist[path[i][0]][path[i][1]])
            if cheat_dist >= path_len - 1:
                continue
            if path_len - cheat_dist -1 in cheats:
                cheats[path_len - cheat_dist -1] += 1
            else:
                cheats[path_len - cheat_dist -1] = 1
            if path_len - cheat_dist - 1 >= 100:
                best_cheats += 1
pprint(cheats)
print("Cheats that save 100 ps: ", best_cheats)
total_length = dist[end[0]][end[1]]


# We need to get the path through the maze. Then we can go through each node of
# that path, and if they are within a manhattan distance of 20, then it is
# equivalent of simply "cheating" to that point. Since there is only one path,
# the distance between that point and the end is the difference in distance from
# the start to end - start to that node.


