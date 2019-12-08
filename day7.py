import itertools
L_original  = [3,8,1001,8,10,8,105,1,0,0,21,38,47,64,89,110,191,272,353,434,99999,3,9,101,4,9,9,102,3,9,9,101,5,9,9,4,9,99,3,9,1002,9,5,9,4,9,99,3,9,101,2,9,9,102,5,9,9,1001,9,5,9,4,9,99,3,9,1001,9,5,9,102,4,9,9,1001,9,5,9,1002,9,2,9,1001,9,3,9,4,9,99,3,9,102,2,9,9,101,4,9,9,1002,9,4,9,1001,9,4,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99]

def get_parameter(L, pc, modes, pos):
    if len(modes) >= pos and modes[pos - 1] == "1":
        return L[pc + pos]
    else:
        return L[L[pc + pos]]


def run_code(L, inputs, pc = 0):
    n = len(L)
    while pc < n:
        full_opcode = L[pc]
        opcode = int(''.join(list(str(full_opcode))[-2:]))
        modes = (list(str(full_opcode))[:-2])[::-1]

        if opcode == 99:
            break

        # Addition and multiplication
        if opcode in [1, 2]:
            op1 = get_parameter(L, pc, modes, 1)
            op2 = get_parameter(L, pc, modes, 2)
            add = L[pc + 3]

            if opcode == 1:
                L[add] = op1 + op2
            else:
                L[add] = op1 * op2
            pc += 4

        # Read input
        elif opcode == 3:
            L[L[pc + 1]] = inputs.pop(0)
            pc += 2

        # Print output
        elif opcode == 4:
            x = get_parameter(L, pc, modes, 1)
            # print("Output:", x)
            res = x
            pc += 2
            return res, pc

        # jump-if-true, jump-if-false
        elif opcode in [5, 6]:
            op1 = get_parameter(L, pc, modes, 1)
            op2 = get_parameter(L, pc, modes, 2)

            if (opcode == 5 and op1 != 0) or (opcode == 6 and op1 == 0):
                pc = op2
            else:
                pc += 3

        # less than, equals
        elif opcode in [7, 8]:
            op1 = get_parameter(L, pc, modes, 1)
            op2 = get_parameter(L, pc, modes, 2)
            add = L[pc + 3]

            if (opcode == 7 and op1 < op2) or (opcode == 8 and op1 == op2):
                L[add] = 1
            else:
                L[add] = 0

            pc += 4

        else:
            print("Unknown code")
            break

    return res, pc

if False:
    t = -1000
    for phases in itertools.permutations([0,1,2,3,4]):

        a, b, c, d, e = phases

        A = run_code(L_original.copy(), [a, 0])
        B = run_code(L_original.copy(), [b, A])
        C = run_code(L_original.copy(), [c, B])
        D = run_code(L_original.copy(), [d, C])
        E = run_code(L_original.copy(), [e, D])
        if E > t:
            t = E

    print("Res: ", t)


A_code = L_original.copy()
B_code = L_original.copy()
C_code = L_original.copy()
D_code = L_original.copy()
E_code = L_original.copy()

phases = [ 9,7,8,5,6]
a, b, c, d, e = phases

pcs = [0, 0, 0, 0, 0]
pc_a, pc_b, pc_c, pc_d, pc_e = pcs

i = 0
while True:
    A, pc_a = run_code(A_code, [a, i], pc_a)
    B, pc_b = run_code(B_code, [b, A], pc_b)
    C, pc_c = run_code(C_code, [c, B], pc_c)
    D, pc_d = run_code(D_code, [d, C], pc_d)
    E, pc_e = run_code(E_code, [e, D], pc_e)
    i = E
    print(E)