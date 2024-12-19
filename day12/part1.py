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


def search_region(start, grid, seen) -> tuple[int, int, set]:
    n = len(grid)
    m = len(grid[0])
    area = 0
    peri = 0
    queue = [start]

    while queue:
        node = queue.pop()
        x = node[0]
        y = node[1]
        plant = grid[x][y]
    
        if node in seen:
            continue
    
        seen.add(node)
    
        curr_par = 0
        for dx,dy in [(0,1), (1,0), (-1,0), (0,-1)]:
            if x+dx < 0 or x+dx >= n or y+dy < 0 or y+dy >=m:
                curr_par += 1
                continue
    
            if grid[x+dx][y+dy] == plant:
                queue.insert(0, (x+dx, y+dy))
            else:
                curr_par += 1
        
        area += 1
        peri += curr_par

    return area, peri, seen


n = len(grid)
m = len(grid[0])
seen = set()
regions = []
for i in range(n):
    for j in range(m):
        a,p,seen = search_region((i,j), grid, seen)
        if a:
            regions.append((grid[i][j], a, p))

total = 0
for region in regions:
    total += region[1]*region[2]

print(regions)
print(total)

