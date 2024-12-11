equations = []
max_l = 0
ops = 0
with open("input.txt", "r") as f:
    for line in f:
        ans, nums = line.split(":")
        ans = int(ans)
        nums = nums.strip().split(' ')
        nums = list(map(int, nums))

        max_l = max(max_l, len(nums))
        equations.append((ans, nums))
        ops += 2**(len(nums))

print(equations[0])
print(max_l)
print(ops)

def evaluate_equation(eq):
    ans = eq[0]
    nums = eq[1]
    n = len(nums)-1
    op_pos = []
    for i in range(2**n):
        op_pos.append('{:0{}b}'.format(i, n))
    
    for pos in op_pos:
        total = nums[0]
        for i in range(n):
            if pos[i] == "1":
                total += nums[i+1]
            else:
                total *= nums[i+1]

        if total == ans:
            return True, ans

    return False, 0

grand_total = 0
for eq in equations:
    valid, tot = evaluate_equation(eq)
    if valid:
        grand_total += tot

print(grand_total)
