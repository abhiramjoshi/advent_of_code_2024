from heapq import heappop, heappush

grid = []
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip("\n")
        row = [ch for ch in line]
        grid.append(row)

n = len(grid)
m = len(grid[0])

def find_position(tile="S"):
    for i in range(n):
        for j in range(m):
            if grid[i][j] == tile:
                return i,j
    
start = find_position("S")
end = find_position("E")

# We will do Dijkstras algorithm, but we care about the states (direction)

dist = []
for i in range(n):
    dist.append([])
    for j in range(m):
        dist[i].append([])
        for d in range(4):
            dist[i][j].append(float("inf"))

dist[start[0]][start[1]][0] = 1000
dist[start[0]][start[1]][1] = 1
dist[start[0]][start[1]][2] = 1000
dist[start[0]][start[1]][3] = 2000

parents = {}

dirs = {
    (1,0): 0,
    (0,1): 1,
    (-1, 0): 2,
    (0, -1): 3
}

visited = set()
queue = [(0, start, (0,1), None, None)]

while queue:
    score, node, heading, parent, prev_heading = heappop(queue)
    x,y = node
    dx,dy = heading
    new_score = score

    if score > dist[x][y][dirs[heading]]: continue

    if dist[x][y][dirs[heading]] >= score:
        dist[x][y][dirs[heading]] = score
    
    if (node, heading) in parents:
        parents[(node,heading)].add((parent, prev_heading))
    else:
        parents[(node,heading)] = {(parent, prev_heading)}
    
    # clockwise
    heappush(queue, (new_score+1000, (x, y), (-heading[1], heading[0]), node, heading))
    # counterclockwise
    heappush(queue, (new_score+1000, (x, y), (heading[1], -heading[0]), node, heading))

    #forward
    if x+dx < 0 or x+dx >= n or y+dy < 0 or y+dy >= m:
        continue
    if grid[x+dx][y+dy] != "#":
        heappush(queue, (new_score+1, (x+dx, y+dy), heading, node, heading))

print(dist[end[0]][end[1]])
print(parents[((13, 13), (-1, 0))])
backtrack = set(parents[(end, (-1, 0))])
backtrack_nodes = set()
while backtrack:
    node = backtrack.pop()
    if node == (None, None):
        break
    print("h", node)
    backtrack_nodes.add(node[0])
    backtrack.update(parents[node])

print(len(backtrack_nodes))
#print(parents)

for node in backtrack_nodes:
    x,y = node
    grid[x][y] = "O"

for i in range(n):
    for j in range(m):
        print(grid[i][j], end="")
    print()

print(dist[7][6])