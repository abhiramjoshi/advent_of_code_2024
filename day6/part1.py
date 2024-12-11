#We need to count the gaurd's distinct positions

grid:list[list] = []
with open("input.txt", 'r') as f:
    for line in f:
        row = [c for c in line]
        grid.append(row)

for row in grid:
    print("".join(row))

def check_valid_pos(x, dim):
    if x < 0 or x >= dim:
        return False
    return True

def find_starting_pos(grid:list[list]):
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '^':
                return i,j
    return 0,0

n = len(grid)
m = len(grid[0])
x,y = find_starting_pos(grid)
heading = 0
distict_positions = 0
directions = {
    0:(-1,0),
    1:(0,1),
    2:(1,0),
    3:(0,-1)
}

while check_valid_pos(x, n) and check_valid_pos(y, m):
    curr_dir = directions[heading]

    if not grid[x][y] == "X":
        distict_positions += 1

    grid[x][y] = "X"
    
    if not check_valid_pos(x+curr_dir[0], n) or not check_valid_pos(y+curr_dir[1], m):
        break

    if grid[x+curr_dir[0]][y+curr_dir[1]] == '#':
        heading += 1
        heading %= 4
        continue

    x += curr_dir[0]
    y += curr_dir[1]

for row in grid:
    print("".join(row))

print(distict_positions)
