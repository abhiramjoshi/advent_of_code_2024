import re
#Unlike our previous regex implementation, this time we will have to make use of a sliding window approach

multiply = True

mult_pattern = 'mul\((\d{1,3}),(\d{1,3})\)' #max length 12
do_pattern = "do()"
dont_pattern = "don't()"

do_counter = 0
dont_counter = 0

def match_mult(pattern, string): #Potentially do this with regex
    match = re.match(pattern, string)
    if match:
        return True, int(match[1]), int(match[2])
    
    return False, 0, 0

def match_pattern(pattern, letter, counter):
    if letter == pattern[counter]:
        counter += 1
    else:
        counter = 0
    
    if counter == len(pattern) - 1:
        counter = 0
        return True, counter
    
    return False, counter

with open("input.txt", 'r') as f:
    s = ''.join(f.readlines())

result = 0

dos = 0
donts = 0

for i in range(len(s)):
    mul, num1, num2 = match_mult(mult_pattern, s[i:i+13])
    do, do_counter = match_pattern(do_pattern, s[i], do_counter)
    dont, dont_counter = match_pattern(dont_pattern, s[i], dont_counter)

    if mul:
        # print("Mult matched: ", num1, num2)
        if multiply:
            result += num1*num2
    
    if do:
        dos += 1
        # print("Do matched")
        multiply = True
    
    if dont:
        donts += 1
        # print("Dont matched")
        multiply = False

# Can optimize by shifting forward the start index by our match span every time we get a match in regex
print(result, dos, donts)