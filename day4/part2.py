# This is some sort of convolutional pattern matching situation. At each possible possition, if we can match our set of required patters, we are good, then we just do sliding window over all possible positons


x_length = 3
y_length = 3


def match_pattern(pattern: list[list], grid: list[list], x: int, y: int):
    for i, j in [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)]:
        # print("Checking grid: ", x, y)
        # print("Pattern position: ", j, i)
        # print("Pattern Letter: ", pattern[j][i])
        # print("Grid: ", grid[y+i][x+j])
        if pattern[i][j] != grid[y+i][x+j]:
            return False

    return True


def check_if_x_mas(x, y, grid):
    patterns = [
        [["M", ".", "M"], 
         [".", "A", "."], 
         ["S", ".", "S"]],
        [["S", ".", "S"], 
         [".", "A", "."], 
         ["M", ".", "M"]],
        [["S", ".", "M"], 
         [".", "A", "."], 
         ["S", ".", "M"]],
        [["M", ".", "S"], 
         [".", "A", "."], 
         ["M", ".", "S"]],
    ]
    matches = 0
    for pattern in patterns:
        if match_pattern(pattern, grid, x, y):
            matches += 1
            break

    return matches


grid = []

with open("/input.txt", "r") as f:
    for line in f:
        row = [l for l in line.strip()]
        grid.append(row)

n = len(grid)
m = len(grid[0])

total = 0
for i in range(n-y_length+1):
    for j in range(m - x_length+1):
        total += check_if_x_mas(j, i, grid)

print(total)
