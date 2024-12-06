import re

pattern = 'mul\((\d{1,3}),(\d{1,3})\)'

with open("input.txt", 'r') as f:
    s = ''.join(f.readlines())

matches = re.findall(pattern, s)

summ = 0
for match in matches:
    summ += int(match[0])*int(match[1])

print(summ)