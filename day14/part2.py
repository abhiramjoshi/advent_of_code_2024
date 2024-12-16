robots = []

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip("\n")
        pos, vel = line.split(" ")
        vel = vel.strip("v=").split(",") 
        pos = pos.strip("p=").split(",")

        robots.append([pos, vel])
n = 101
m = 103

def perform_step(robots):
    for i,robot in enumerate(robots):
        pos, vel = robot

        n_x = (int(pos[0]) + int(vel[0]))%n
        n_y = (int(pos[1]) + int(vel[1]))%m
        
        robots[i][0] = [n_x, n_y]

    return robots

def draw(robots):
    grid = []
    for i in range(n):
        grid.append([0 for _ in range(m)])

    for robot in robots:
        pos, vel = robot
        x,y = pos
        grid[x][y] += 1
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                grid[i][j] = '.'
            else:
                grid[i][j] = 'X'
            
        #     print(grid[i][j], end=' ')
        # print()

    threshold = 5
    if detect_horizontal_lines(grid, length=threshold) or detect_veritcal_lines(grid, length=threshold):
        for i in range(n):
            for j in range(m):
                print(grid[i][j], end=' ')
            print()
        input(f"Continue?")
    return grid

def detect_horizontal_lines(grid, length=10):
    for line in grid:
        line_length = 0
        for char in line:
            if char == "X":
                line_length += 1
            else:
                line_length = 0
            if line_length >= length:
                return True
    return False

def detect_veritcal_lines(grid, length=10):
    n = len(grid)
    m = len(grid[0])
    for i in range(m):
        line_length = 0
        for j in range(n):
            if grid[j][n] == "X":
                line_length += 1
            else:
                line_length = 0
            if line_length >= length:
                return True
    return False

seconds = 8000
for i in range(seconds):
    robots = perform_step(robots)
    print(f"Seconds elapsed {i}")
    if i > 6000:
        draw(robots)

quadrants = [0,0,0,0]
