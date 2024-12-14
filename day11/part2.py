stones = {}
with open("input.txt", "r") as f:
    for stone in f.readline().split():
        if stone in stones:
            stones[stone] += 1
        else:
            stones[stone] = 1

def perform_blink(stones:dict):
    new_stones = {}

    for stone in stones:
        if int(stone) == 0:
            if "1" in new_stones:
                new_stones['1'] += stones[stone]
            else:
                new_stones['1'] = stones[stone]
            continue

        if len(stone) % 2 == 0:
            n = len(stone) // 2
            first = str(int(stone[:n]))
            second = str(int(stone[n:]))
            # print(string_stone)
            # print(first)
            # print(second)
            if first in new_stones:
                new_stones[first] += stones[stone]
            else:
                new_stones[first] = stones[stone]
            
            if second in new_stones:
                new_stones[second] += stones[stone]
            else:
                new_stones[second] = stones[stone]
                
            continue
        
        new_stone = str(int(stone)*2024)
        if new_stone in new_stones:
            new_stones[new_stone] += stones[stone]
        else:
            new_stones[new_stone] = stones[stone]

    return new_stones


blinks = 75
for blink in range(blinks):
    print(blink)
    stones = perform_blink(stones)

all_stones = sum([stones[stone] for stone in stones])
print(stones)
print(all_stones)


