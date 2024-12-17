A_register = None
B_register = None
C_register = None
POINTER = 0

def adv(x):
    global A_register
    A_register = A_register//2**x

def bxl(x):
    global B_register
    B_register ^= x

def bst(x):
    global B_register
    B_register = x%8

def jnz(x):
    global A_register, POINTER
    if A_register == 0:
        return
    
    POINTER = x - 2


def bxc(x):
    global B_register, C_register
    B_register ^= C_register

def out(x):
    return x % 8

def bdv(x):
    global A_register, B_register
    B_register = A_register//2**x

def cdv(x):
    global A_register, C_register
    C_register = A_register//2**x


opcodes = {
    "0":adv,
    "1":bxl,
    "2":bst,
    "3":jnz,
    "4":bxc,
    "5":out,
    "6":bdv,
    "7":cdv,
}

def run_program(program, a_register_val, b_register_val, c_register_val):
    global A_register, B_register, C_register, POINTER
    A_register = a_register_val
    B_register = b_register_val
    C_register = c_register_val
    POINTER = 0
    output = []
    
    while POINTER < len(program)-1:
        operands = {
            "0":0,
            "1":1,
            "2":2,
            "3":3,
            "4":A_register,
            "5":B_register,
            "6":C_register,
        }
        opcode = str(program[POINTER])
        operand = str(program[POINTER+1])
        if opcode in ["1", "3"]:
            outvar = opcodes[opcode](int(operand))
        else:
            outvar = opcodes[opcode](operands[operand])
        if outvar != None:
            output.append(outvar)
        POINTER += 2

    return ",".join(list(map(str, output)))

def reverse_engineer(program, ans):
    print(program, ans)
    if program == []: return ans
    for t in range(8):
        a = (ans << 3) + t
        b = a % 8
        b = b ^ 1
        c = a >> b
        b = b ^ 5
        b = b ^ c
        if b % 8 == program[-1]:
            sub = reverse_engineer(program[:-1], a)
            if sub is None:continue
            return sub

program = "2,4,1,1,7,5,1,5,4,1,5,5,0,3,3,0"
a = 2408
b = 0
c = 0

output = run_program(program.split(','), a, b, c)
print(output)
print(program[-9:])
program = list(map(int, program.split(",")))
ans = reverse_engineer(program, 0)
print(ans)

