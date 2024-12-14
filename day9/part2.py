with open("/Users/abhiramj/Documents/advent_of_code_2024/day9/input.txt", "r") as f:
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
    n = len(expanded_diskmap)
    i = n - 1
    first_free = 0
    while i >= 0:
        c = expanded_diskmap[i]
        if c == ".":
            i -= 1
            continue

        j = i
        while expanded_diskmap[j] == c:
            j -= 1
        
        file_length = i-j
        # we now have j and i which are the start and end of the file
        free_size = 0
        for k in range(first_free, j+1):
            if expanded_diskmap[k] == '.':
                free_size += 1
            else:
                free_size = 0
            
            if free_size >= i-j:
                #insert file
                for l in range(file_length):
                    expanded_diskmap[k-file_length+l+1] = expanded_diskmap[j+1+l]
                    expanded_diskmap[j+1+l] = '.'

                if (k + 1 - (file_length)) == first_free:
                    first_free = k + 1

                break

        i -= file_length 
    # with open('datawrong.txt', 'w') as f:
    #     for char in expanded_diskmap:
    #         f.write(char)
    #         f.write('\n')
    checksum = 0
    for j,char in enumerate(expanded_diskmap):
        if char == '.':
            continue

        checksum += j*int(char)
    #print(expanded_diskmap)
    return checksum

exp_disk = expand_diskmap(disk_map)
with open("startwrong.txt", "w") as f:
    for char in exp_disk:
        f.write(str(char))
        f.write("\n")
    
print(compress_diskmap(exp_disk))
