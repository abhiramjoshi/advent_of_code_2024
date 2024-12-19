with open("input.txt", "r") as f:
    lines = f.readlines()
    patterns = lines[0].strip("\n").split(", ")
    designs = [line.strip('\n') for line in lines[2:]]

# Do some sort of DP, where we will try to make all possible designs

def make_design(design, patters):
    n = len(design)
    dp = [float('inf')]*(n+1)
    dp[0] = 0

    for i in range(1,n+1):
        for pattern in patterns:
            j = len(pattern)
            if j > i:
                continue
            # If the pattern can make part of the design, use it
            #print(design[i-j:i])
            if design[i-j:i] == pattern:
                dp[i] = min(dp[i], dp[i-j]+1)
    
    return dp

possible = 0
for design in designs:
    if make_design(design, patterns)[-1] != float("inf"):
        possible += 1

print(possible)

