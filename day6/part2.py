# We need to count the gaurd's distinct positions
import time

grid: list[list] = []
with open("input.txt", "r") as f:
    for line in f:
        row = [c for c in line]
        grid.append(row)


def check_valid_pos(x, dim):
    if x < 0 or x >= dim:
        return False
    return True


def find_starting_pos(grid: list[list]):
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "^":
                return i, j
    return 0, 0



def run_sim(grid, start):  
    n = len(grid)
    m = len(grid[0])
    x, y = start[0], start[1]
    heading = 0
    path = {}
    directions = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
    while check_valid_pos(x, n) and check_valid_pos(y, m):
        curr_dir = directions[heading]
        
        if (x,y) in path:
            if heading in path[(x,y)]:
                return path, True
            else:
                path[(x,y)].append(heading)
        else:
            path[(x,y)] = [heading]
    
        if not check_valid_pos(x + curr_dir[0], n) or not check_valid_pos(
            y + curr_dir[1], m
        ):
            break
    
        if grid[x + curr_dir[0]][y + curr_dir[1]] == "#":
            heading += 1
            heading %= 4
            continue
    
        x += curr_dir[0]
        y += curr_dir[1]
        

    return path, False

# We can do this using brute force, basically we can put a block in every valid
# location, if this results in a loop, count it, if it results in our gaurd
# leaving the grid, we can remove it.

start_time = time.time()
start = (find_starting_pos(grid))
path,_ = run_sim(grid, start)
path.pop(start)
path = list(path.keys())
loop_obstacles = 0

for p in path:
    grid[p[0]][p[1]] = '#'
    _, loop = run_sim(grid, start)
    if loop:
        loop_obstacles += 1
    
    grid[p[0]][p[1]] = '.'
end_time = time.time()
print(loop_obstacles)
print("Time elapsed: ", end_time-start_time)
