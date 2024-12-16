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

seconds = 100
for _ in range(seconds):
    robots = perform_step(robots)

quadrants = [0,0,0,0]

for robot in robots:
    pos, vel = robot
    x,y = pos

    if x < n//2:
        if y < m//2:
            quadrants[0] += 1
        elif y > m//2:
            quadrants[1] += 1
    elif x > n//2:
        if y < m//2:
            quadrants[2] += 1
        elif y > m//2:
            quadrants[3] += 1

print(quadrants[0]*quadrants[1]*quadrants[2]*quadrants[3])
