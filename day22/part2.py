with open("input.txt", "r") as f:
    secret_nums = [int(l.strip("\n")) for l in f.readlines()]

def cal_next_secret(num):
    prev_num = num
    mix = num * 64
    num ^= mix
    num %= 16777216

    mix = num // 32
    num ^= mix
    num %= 16777216

    mix = num * 2048
    num ^= mix
    num %= 16777216

    return num, num%10

num = 123

sequence_nums = [[] for _ in range(len(secret_nums))]
change_sequences = {}

for i,num in enumerate(secret_nums):
    running_sequence = [0]
    seen_sequences = set()
    sequence_nums[i].append((num, num%10))
    for j in range(2000):
        num, bananas = cal_next_secret(num)
        #print(sequence_nums)
        #print(num, bananas)
        diff = bananas-sequence_nums[i][j][1]
        running_sequence.append(diff)
        if j >= 2:
            if tuple(running_sequence) in seen_sequences:
                pass
            elif tuple(running_sequence) in change_sequences:
                change_sequences[tuple(running_sequence)] += bananas
            else:
                change_sequences[tuple(running_sequence)] = bananas
            #if tuple(running_sequence) == (-2,1,-1,3):
            #    print(i,j, bananas)
            seen_sequences.add(tuple(running_sequence))
            running_sequence.pop(0)
        
        sequence_nums[i].append((num, bananas))

#print(secret_nums)
#print(change_sequences)
#print(sequence_nums)
best = sorted(change_sequences.items(), key=lambda x: x[1])
print(best[-10:])
#print(change_sequences[(-2,1,-1,3)])

