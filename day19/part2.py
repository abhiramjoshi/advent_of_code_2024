with open("input.txt", "r") as f:
    lines = f.readlines()
    patterns = lines[0].strip("\n").split(", ")
    designs = [line.strip('\n') for line in lines[2:]]

# Do some sort of DP, where we will try to make all possible designs

def make_design(design, patterns):
    n = len(design)
    dp = [1]*(n+1)
    for i in range(1,n+1):
        ways = 0
        for pattern in patterns:
            j = len(pattern)
            if j > i:
                continue
            # If the pattern can make part of the design, use it
            #print(design[i-j:i])
            
            if design[i-j:i] == pattern:
                ways += dp[i-j]
        
        dp[i] = ways
    return dp

num_of_arr = 0
for i,design in enumerate(designs):
    num_of_arr += make_design(design, patterns)[-1]

print(num_of_arr)

