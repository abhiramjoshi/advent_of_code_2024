def check_safe(report):
    levels = report.split()
    print(levels)
    n = len(levels)
    direction = True
    for i in range(n):
        if i == 0:
            continue
        
        diff = int(levels[i]) - int(levels[i-1])
        if i == 1:
            if diff < 0:
                direction = False
        
        if diff == 0:
            print("Non-increasing")
            return False
        
        if diff < 0 and direction:
            print("Change direction to negative")
            return False

        if diff > 0 and not direction:
            print("Change direction to positive")
            return False

        if abs(diff) > 3:
            print("Greater than 3 levels of change")
            return False
        
    print("Safe report")
    return True 

safe = 0
unsafe = 0

with open("debug_input.txt", 'r') as reports:
    for report in reports:
        if check_safe(report):
            safe += 1
        else:
            unsafe += 1

print(f"Safe reports: ", safe)
print(f"Unsafe reports: ", unsafe)