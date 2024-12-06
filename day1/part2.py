input1 = []
input2 = []

freq = {}
with open("input.txt", "r") as f:
    for line in f:
        first, second = line.split()
        input1.append(int(first))
        
        second = int(second)

        if second in freq:
            freq[second] += 1
        else:
            freq[second] = 1

sim_score = 0
for i in range(len(input1)):
    if input1[i] in freq:
        sim_score += input1[i]*freq[input1[i]]
    else:
        pass

print(sim_score)
        
                
