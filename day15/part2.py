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

doubled_grid = []
for i in range(n):
    doubled_grid.append([])
    for j in range(m):
        if grid[i][j] == '#':
            doubled_grid[i] += ["#","#"]
        if grid[i][j] == 'O':
            doubled_grid[i] += ["[","]"]
        if grid[i][j] == '.':
            doubled_grid[i] += [".","."]
        if grid[i][j] == '@':
            doubled_grid[i] += ["@","."]
    
def find_pos(char:str, stop_after_first:bool=True, grid=grid) -> list:
    n = len(grid)
    m = len(grid[0])
    positions = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == char:
                if stop_after_first:
                    return [(i,j)]
                else:
                    positions.append((i,j))
    
    return positions

robot = find_pos("@", grid=doubled_grid)[0]

def move(pos:tuple, direction:str, grid:list[list[str]], from_half = False):
    n = len(grid)
    m = len(grid[0])
    dirs = {
        "^":(-1,0),
        ">":(0,1),
        "v":(1,0),
        "<":(0,-1)
    }
    #print(pos, direction)
    x,y = pos
    if grid[x][y] == "#":
        return False, pos, grid
    
    if grid[x][y] == ".":
        return True, pos, grid
    
    nx, ny = x+dirs[direction][0], y+dirs[direction][1]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        return False, pos, grid
    
    if grid[x][y] == "[" and not from_half:
        right_grid = [row[:] for row in grid]
        right_side, _, right_grid = move((x, y+1), direction, right_grid, True)
        if not right_side:
            return False, pos, grid
        next_move, _, right_grid = move((nx,ny), direction, right_grid)
        if not next_move:
            return False, pos, grid
        
        grid = right_grid
        grid[nx][ny] = grid[x][y]
        grid[x][y] = "."

    elif grid[x][y] == "]" and not from_half:
        left_grid = [row[:] for row in grid]
        left_side, _, left_grid = move((x, y-1), direction, left_grid, True)
        if not left_side:
            return False, pos, grid
        next_move, _, left_grid = move((nx,ny), direction, left_grid)
        if not next_move:
            return False, pos, grid
        
        grid = left_grid
        grid[nx][ny] = grid[x][y]
        grid[x][y] = "."

    else:
        next_move, _, grid = move((nx,ny), direction, grid)
        if not next_move:
            return False, pos, grid
    
        grid[nx][ny] = grid[x][y]
        grid[x][y] = "."
    
    return True, (nx,ny), grid

for inst in instructions:
    result, robot, doubled_grid = move(robot, inst, doubled_grid)

gps = 0
boxes = find_pos("[", stop_after_first=False, grid=doubled_grid)
for box in boxes:
    if box[1] <= m:
        gps += 100*box[0]+box[1]
    else:
        gps += 100*box[0] + box[1] 

print(gps)

for i in range(len(doubled_grid)):
    for j in range(len(doubled_grid[0])):
        print(doubled_grid[i][j], end="")
    print()

