def precedence(optor):
    if optor == '+':
        return 1
    elif optor == '-':
        return 1
    elif optor == '*':
        return 2
    else:
        return 2


def operation(v1, v2, optor):
    if optor == '+':
        return v1 + v2
    elif optor == '-':
        return v1 - v2
    elif optor == '*':
        return v1 * v2
    else:
        return v1 / v2    



def infix(exp):
    # write your code here
    opnds = []
    optors = []

    for i in range(len(exp)):
        ch = exp[i]
        
        if ch == '(':
            optors.append(ch)

        elif ch.isdigit():
            opnds.append(ord(ch) - ord('0'))  # char to int

        elif ch == ')':
            while optors[-1] != '(':
                optor = optors.pop()
                v2 = opnds.pop()
                v1 = opnds.pop()
                opv = operation(v1, v2, optor)
                opnds.append(opv)

            optors.pop()

        elif ch == '+' or ch == '-' or ch == '*' or ch == '/':
            # ch wanting higher priority operators to solve first
            while(len(optors) > 0 and optors[-1] != '(' and precedence(ch) <= precedence(optors[-1])):
                optor = optors.pop()
                v2 = opnds.pop()
                v1 = opnds.pop()
                opv = operation(v1, v2, optor)
                opnds.append(opv)
            # ch is puhsing itself now
            optors.append(ch)


    while len(optors) != 0:
        optor = optors.pop()
        v2 = opnds.pop()
        v1 = opnds.pop()
        opv = operation(v1, v2, optor)
        opnds.append(opv)
    ans = int(opnds.pop())
    print(ans)





exp = input()
exp = exp.replace(" ", "")


infix(exp)

# i/p test case
# 2 + 6 * 4 / 8 - 3


""" Pepcoding solution"""
# def pre(ch):
#     if ch == '+':
#         return 1
#     elif ch == '-':
#         return 1
#     elif ch == '*':
#         return 2
#     else:
#         return 2

# def operation(v1, v2, op):
#     if op == '+':
#         return v1 + v2
#     elif op == '-':
#         return v1 - v2
#     elif op == '*':
#         return v1 * v2
#     else:
#         return v1 / v2

# def infix(exp):
#     sti = []
#     stc = []
#     for i in range(0, len(exp)) :
#         ch = exp[i]
#         # print(ch, end = ' ')
#         if ch == '(':
#             stc.append(ch)
#         elif ch == '+' or ch == '-' or ch == '*' or ch == '/':
#             while len(stc) > 0 and stc[-1] != '(' and pre(ch) <= pre(stc[-1]):
#                 v2 = sti.pop()
#                 v1 = sti.pop()
#                 op = stc.pop()

#                 val = operation(v1, v2, op)
#                 sti.append(val)
#             stc.append(ch)

#         elif ch == ')':
#             while len(stc) > 0 and stc[-1] != '(':
#                 v2 = sti.pop()
#                 v1 = sti.pop()
#                 op = stc.pop()

#                 val = operation(v1, v2, op)
#                 sti.append(val)
#             if len(stc) > 0:
#                 stc.pop()
#             else:
#             # print(ch)
#                 val = int(ch)
#             # print(val)
#                 sti.append(val)

#     while len(stc) > 0:
#         v2 = sti.pop()
#         v1 = sti.pop()
#         op = stc.pop()
#         val = operation(v1, v2, op)
        
#     sti.append(val)

#     val = int(sti.pop())
#     print(val)



# exp = input()
# exp = exp.replace(" ", "")

# infix(exp)
