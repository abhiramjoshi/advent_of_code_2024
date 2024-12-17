import numpy as np

raw_equations = []
with open("/Users/abhiramj/Documents/advent_of_code_2024/day13/input.txt", "r") as f:
    machine = []
    for line in f:
        line = line.strip("\n")
        if not line:
            raw_equations.append(machine)
            machine = []
        else:
            machine.append(line)
    
    raw_equations.append(machine)

print(raw_equations)

solutions = []
for machine in raw_equations:
    a_temp = machine[0].split(',')
    button_a = (int(a_temp[0].strip("Button A: X+")), int(a_temp[1].strip(" Y+")))
    b_temp = machine[1].split(',')
    button_b = (int(b_temp[0].strip("Button B: X+")), int(b_temp[1].strip(" Y+")))
    p_temp = machine[2].split(',')
    prize = (int(p_temp[0].strip("Prize: X=")), int(p_temp[1].strip(" Y=")))
    
    a_coeff = np.array([button_a[0], button_b[0]])
    b_coeff = np.array([button_a[1], button_b[1]])
    const = np.array(prize)

    sol = np.linalg.solve(np.array([a_coeff, b_coeff]), prize)
    sol = np.around(sol, 2)
    if sol[0] == int(sol[0]) and sol[1] == int(sol[1]):
        solutions.append(sol)

total_cost = 0
for sol in solutions:
    total_cost += int(sol[0])*3 + int(sol[1])
print("Total cost: ", total_cost)