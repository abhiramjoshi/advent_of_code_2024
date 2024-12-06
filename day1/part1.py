id_list1 = []
id_list2 = []

with open("input.txt", "r") as f:
    for line in f:
        first, second = line.split()
        id_list1.append(int(first))
        id_list2.append(int(second))
    
id_list1.sort()
id_list2.sort()

s = 0
for i in range(len(id_list1)):
    s += abs(id_list1[i] - id_list2[i])

print(s)


