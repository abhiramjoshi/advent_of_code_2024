grid = []
instructions = []
parsegrid = True
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip("\n")
        if not line:
            parsegrid = False
            continue
        
        if parsegrid:
            row = [ch for ch in line]
            grid.append(row)
        else:
            instructions += [ch for ch in line]

n = len(grid)
m = len(grid[0])
def find_pos(char:str, stop_after_first:bool=True) -> list:
    positions = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == char:
                if stop_after_first:
                    return [(i,j)]
                else:
                    positions.append((i,j))
    
    return positions

robot = find_pos("@")[0]

def move(pos:tuple, direction:str, grid:list[list[str]]=grid):
    n = len(grid)
    m = len(grid[0])
    dirs = {
        "^":(-1,0),
        ">":(0,1),
        "v":(1,0),
        "<":(0,-1)
    }
    
    x,y = pos
    if grid[x][y] == "#":
        return False, pos, grid
    
    if grid[x][y] == ".":
        return True, pos, grid
    
    nx, ny = x+dirs[direction][0], y+dirs[direction][1]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        return False, pos, grid
    
    
    next_move, _, grid = move((nx,ny), direction, grid)
    if not next_move:
        return False, pos, grid
    
    grid[nx][ny] = grid[x][y]
    grid[x][y] = "."
    return True, (nx,ny), grid

    
for inst in instructions:
    result, robot, grid = move(robot, inst, grid)

gps = 0
boxes = find_pos("O", stop_after_first=False)
for box in boxes:
    gps += 100*box[0]+box[1]

print(gps)

for i in range(n):
    for j in range(m):
        print(grid[i][j], end="")
    print()

