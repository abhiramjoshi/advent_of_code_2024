with open("input.txt", "r") as f:
    disk_map = f.readline().strip("\n")

def expand_diskmap(disk_map:str) -> list:
    expanded_map = []
    for i,c in enumerate(disk_map):
        if i % 2 == 1:
            expanded_map += ['.']*int(c)
        else:
            id = i // 2
            expanded_map += [str(id)]*int(c)
    return expanded_map

def compress_diskmap(expanded_diskmap:list) -> int:
    i = 0
    checksum = 0

    while i < len(expanded_diskmap):
        c = expanded_diskmap[i]
        if c == ".":
            char = '.'
            while char == '.':
                char = expanded_diskmap.pop()
            expanded_diskmap[i] = char
        else:
            pass
        
        checksum += int(expanded_diskmap[i])*i
        i += 1

    return checksum

exp_disk = expand_diskmap(disk_map)
print(compress_diskmap(exp_disk))
