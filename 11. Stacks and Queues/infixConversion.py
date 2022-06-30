def precedence(optor):
    if optor == '+':
        return 1
    elif optor == '-':
        return 1
    elif optor == '*':
        return 2
    else:
        return 2


def infix(exp):
# write your code here
    post = []
    pre = []
    ops = []

    for i in range(len(exp)):
        ch = exp[i]

        if ch == '(':
            ops.append(ch)

        elif((ch >= '0' and ch <= '9') or (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z')):
            post.append(ch)
            pre.append(ch)

        elif(ch == ')'):
            while(ops[-1] != '('):
                op = ops.pop()

                postV2 = post.pop()
                postV1 = post.pop()
                postV = postV1 + postV2 + op
                post.append(postV)

                
                preV2 = pre.pop()
                preV1 = pre.pop()
                preV = op + preV1 + preV2 
                post.append(preV)

            ops.append(ch)

        elif(ch == '+' or ch == '-' or ch == '*' or ch == "/"):
            while(len(ops)> 0 and ops[-1] != '(' and precedence(ch) <= precedence(ops[-1])):
                op = ops.pop()

                postV2 = post.pop()
                postV1 = post.pop()
                postV = postV1 + postV2 + op
                post.append(postV)

                
                preV2 = pre.pop()
                preV1 = pre.pop()
                preV = preV1 + preV2 + op
                post.append(preV)
                
            ops.append(ch)
    
    while(len(ops) > 0):
        op = ops.pop()

        postV2 = post.pop()
        postV1 = post.pop()
        postV = postV1 + postV2 + op
        post.append(postV)
        
        preV2 = pre.pop()
        preV1 = pre.pop()
        preV = op + preV1 + preV2 
        post.append(preV)

    print(post.pop())
    print(pre.pop())



exp = list(input())  # taking i / p from user in list['ch']

infix(exp)