equations = []
max_l = 0
ops = 0
with open("/Users/abhiramj/Documents/advent_of_code_2024/day7/input.txt", "r") as f:
    for line in f:
        ans, nums = line.split(":")
        ans = int(ans)
        nums = nums.strip().split(' ')
        nums = list(map(int, nums))

        max_l = max(max_l, len(nums))
        equations.append((ans, nums))
        ops += 3**(len(nums))

print(equations[0])
print(max_l)
print(ops)

def ternary(i,n):
    if i==0:
        return ''.zfill(n)
    nums = []
    while i:
        i, r = divmod(i,3)
        nums.append(str(r))
    return ''.join(reversed(nums)).zfill(n)

def evaluate_equation(eq):
    ans = eq[0]
    nums = eq[1]
    n = len(nums)-1
    # print(eq)
    for i in range(3**n):
        ops = ternary(i,n)
        total = nums[0]

        for i in range(n):
            if ops[i] == "0":
                total += nums[i+1]
            elif ops[i] == "1":
                total *= nums[i+1]
            else:
                total = str(total) + str(nums[i+1])
                total = int(total)
        
        # print(ops)
        # print(total)
        # print(total == ans)
        # print()
        if total == ans:
            return True, ans

    return False, 0

grand_total = 0
for eq in equations:
    valid, tot = evaluate_equation(eq)
    if valid:
        grand_total += tot

print("Grand total: ", grand_total)
