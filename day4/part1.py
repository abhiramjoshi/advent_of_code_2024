# We will basically go to each character and do a search in all directions for our word
grid = []
with open("input.txt", "r") as f:
    for line in f:
        row = [l for l in line.strip()]
        grid.append(row)

word = "XMAS"

n = len(grid)
m = len(grid[0])

print(n, m)


def find_word(x, y, word):
    occurr = 0
    for dir in [[1, 0], (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
        n_w = len(word)
        # If the end of the word will be out of bounds, not point looking
        if (
            x + n_w * dir[0] > n
            or x + n_w * dir[0] < -1
            or y + n_w * dir[1] > m
            or y + n_w * dir[1] < -1
        ):
            print("Start not an option: ", x, y, dir)
            continue
        curr_x = x
        curr_y = y
        found = True
        for i in range(n_w):
            if grid[curr_x][curr_y] != word[i]:
                found = False
                break
            curr_x += dir[0]
            curr_y += dir[1]

        if found:
            print("Found occurrance in start, direction: ", x, y, dir)
            occurr += 1

    return occurr


total = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == word[0]:
            total += find_word(i, j, word)

print(total)
