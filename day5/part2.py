prereq = {}
updates:list[list] = []

with open("/Users/abhiramj/Documents/advent_of_code_2024/day5/input.txt", "r") as f:
    update = False
    for line in f:
        line = line.strip("\n")
        if update:
            updates.append(list(map(int, line.split(','))))
            continue

        if not line:
            update = True
            continue
        
        edge = line.split("|")
        edge = list(map(int, edge))
        if edge[1] in prereq:
            prereq[edge[1]].add(edge[0])
        else:
            prereq[edge[1]] = {edge[0]}
print(prereq)

good_updates = 0

for update in updates:
    i = len(update) - 1
    while i >= 0:
        doc = update[i]
        if doc not in prereq:
            i -= 1
            continue
        for pre in prereq[doc]:
            if pre in update[i+1:]:
                #pop current index, add it to before after prereq and change index to new insert
                p_i = update[i:].index(pre)
                curr = update.pop(i)
                update.insert(i+p_i, curr)
                i = i+p_i
        i -= 1

    good_updates += update[len(update)//2]


print(good_updates)
