prereq = {}
updates = []

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

good_updates = 0

for update in updates:
    not_good_update = False
    seen = set()
    for doc in reversed(update):
        if doc not in prereq:
            seen.add(doc)
            continue

        for pre in prereq[doc]:
            if pre in seen:
                not_good_update = True
                break
        if not_good_update:
            break
        seen.add(doc)
    
    if not_good_update:
        print(','.join(list(map(str, update))))
        continue

    good_updates += update[len(update)//2]


print(good_updates)
