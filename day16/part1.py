# Flood fill BFS, fine the lowest score to the end.

grid = []
with open("test_input.txt", "r") as f:
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
print(end)

queue = [(start, (0,1), 0, set())]

min_score = 10**27

memoization = {}

while queue:
    (x, y), heading, score, path = queue.pop(0)
    #print((x, y), heading, score, path)
    if score > min_score:
        #print("Terminated search")
        continue
    
    if (x,y) in memoization:
        if memoization[(x,y)][0] < score:
            continue
        if memoization[(x,y)][0] >= score:
            memoization[(x,y)] = (score, path)
    else:
        memoization[(x,y)] = (score, path)
    # if (x,y) in path:
    #     print("Terminated search")
    #     continue
    
    path.add((x,y))
    
    if (x,y) == end:
        min_score = min(score, min_score)
        continue

    for dx, dy in [(0,1), (1, 0), (-1,0), (0,-1)]:
        if (x+dx, y+dy) in path:
            #print("Already searched")
            continue
        new_score = score
        new_path = path.copy()
        # Skipping of direction opposite to heading
        if x == dx and y == -dy:
            continue
        if x == -dx and y == dy:
            continue
        
        # Skipping if wall
        if x+dx < 0 or x+dx >= n or y+dy < 0 or y+dy >= m:
            continue
        if grid[x+dx][y+dy] == "#":
            continue
        if (x+dx, y+dy) in new_path:
            continue
        # If moving forward, add 1
        if (dx,dy) == heading:
            new_score += 1
        else:
            new_score += 1001
        
        queue.append(((x+dx, y+dy), (dx,dy), new_score, new_path))


print(min_score)