with open("input.txt", "r") as f:
    secret_nums = [int(l.strip("\n")) for l in f.readlines()]

def cal_next_secret(num):
    mix = num * 64
    num ^= mix
    num %= 16777216

    mix = num // 32
    num ^= mix
    num %= 16777216

    mix = num * 2048
    num ^= mix
    num %= 16777216

    return num

num = 123

final_nums = []

for num in secret_nums:
    print(f"{num}: ", end="")
    for _ in range(2000):
        num = cal_next_secret(num)
    final_nums.append(num)
    print(num)
print(sum(final_nums))

