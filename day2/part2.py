def check_safe(levels):
    n = len(levels)
    direction = True
    for i in range(n):
        if i == 0:
            continue
        
        diff = levels[i] - levels[i-1]
        if i == 1:
            if diff < 0:
                direction = False
        
        if diff == 0:
            return False
        
        if diff < 0 and direction:
            return False

        if diff > 0 and not direction:
            return False

        if abs(diff) > 3:
            return False

    return True 

safe = 0

with open("input.txt", 'r') as reports:
    for report in reports:
        levels = list(map(int, report.split()))
        n = len(levels)
        for i in range(n+1):
            if check_safe(levels[:i]+levels[i+1:]):
                safe += 1
                break


print(f"Safe reports: ", safe)