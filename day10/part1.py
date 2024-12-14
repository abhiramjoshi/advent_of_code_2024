# A trailhead must start at a 0, so we must detect a 0, then all the paths going
# up from there to a 9 will count. Therefore, we can treat this as a graph
# problem, where we are starting at nodes beginning with 0. 

# We can do a breadth first search

grid = []

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        row = []
        for n in line:
            if n == '.':
                row.append(1)
            else:
                row.append(int(n))
        #row = [int(n) for n in line]
        grid.append(row)

def find_complete_trails(x,y,n,m):
    if grid[x][y] == 9:
        return [(x,y)]

    complete_trails = set() 
    for dx, dy in [(0,1), (1,0), (-1, 0), (0,-1)]:
        if x+dx < 0 or x+dx >= n or y+dy < 0 or y+dy >= m:
            continue

        if grid[x+dx][y+dy] == grid[x][y] + 1:
            complete_trails.update(find_complete_trails(x+dx,y+dy,n,m))
    return complete_trails

total_trails = 0
n = len(grid)
m = len(grid[0])

for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            total_trails += len(find_complete_trails(i,j,n,m))

print(total_trails)
