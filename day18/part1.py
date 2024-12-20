from heapq import heappop, heappush

bytes = []
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip("\n")
        bytes.append(line.split(','))

# We will do Dijkstras algorithm
def djikstras(bytes, seconds):
    memory_space = []
    n = 71

    for i in range(n):
        memory_space.append(["." for _ in range(n)])

    start = (0,0)
    end = (n-1,n-1)

    # Simulate bytes
    seconds = seconds
    for i in range(seconds):
        byte = bytes[i]
        memory_space[int(byte[1])][int(byte[0])] = "#"
    
    dist = []
    for i in range(n):
        dist.append([])
        for j in range(n):
            dist[i].append(float("inf"))

    dist[0][0] = 0

    dirs = [
        (1,0),
        (0,1),
        (-1, 0),
        (0, -1)
    ]

    visited = set()
    queue = [(0, (0,0))]

    while queue:
        score, node = heappop(queue)
        x,y = node

        if node in visited:
            continue

        if score > dist[x][y]: continue

        if dist[x][y] >= score:
            dist[x][y] = score
        
        if node == end:
            break
        
        visited.add(node)
        for dx, dy in dirs:
            new_score = score
            if x+dx < 0 or x+dx >= n or y+dy < 0 or y+dy >= n:
                continue
            if dist[x+dx][y+dy] < new_score+1:
                continue
            if memory_space[x+dx][y+dy] != "#":
                heappush(queue, (new_score+1, (x+dx, y+dy)))
    if dist[-1][-1] == float("inf"):
        return bytes[seconds-1]

# Part1 Djikstras and return path
# for node in backtrack_nodes:
#     x,y = node
#     grid[x][y] = "O"

# for i in range(n):
#     for j in range(m):
#         print(grid[i][j], end="")
#     print()

# Part2 Simulate paths and return byte when path does not exist
# Alternatively, you can use union find algorithm here to see 
# if end is connected to start
for i in range(len(bytes)):
    result = djikstras(bytes, i)
    if result:
        print(result)
        break