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

def dfs(node:tuple[int, int], maze, score:int, heading:tuple[int, int], path:set, end:tuple[int, int]):
    if node == end:
        return score
    
    x,y = node
    path.add(node)
    end_scores = [10**27]
    for dx, dy in [(0,1), (1, 0), (-1,0), (0,-1)]:
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
            end_scores.append(dfs((x+dx, y+dy), maze, new_score+1, (dx,dy), new_path, end))
        else:
            end_scores.append(dfs((x+dx, y+dy), maze, new_score+1001, (dx,dy), new_path, end))
        
    return min(end_scores)

print(dfs(start, grid, 0, (0,1), set(), end))