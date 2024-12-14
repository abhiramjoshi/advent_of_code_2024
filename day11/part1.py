stones = []
with open("input.txt", "r") as f:
    stones = [int(n) for n in f.readline().split(' ')]


def perform_blink(stones:list[int]):
    i = 0
    while i < len(stones):
        if stones[i] == 0:
            stones[i] = 1
            i += 1
            continue
        if len(str(stones[i])) % 2 == 0:
            string_stone = str(stones[i])
            n = len(string_stone) // 2
            first = string_stone[:n]
            second = string_stone[n:]
            # print(string_stone)
            # print(first)
            # print(second)
            stones[i] = int(second)
            stones.insert(i, int(first))
            i += 2
            continue
        
        stones[i] *= 2024
        i += 1

blinks = 28
for blink in range(blinks):
    print(blink)
    perform_blink(stones)

print(len(stones))



