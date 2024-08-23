T = int(input())

for _ in range(T):
    stack = []
    vps = list(str(input()))
    for i in range(len(vps)):
        if vps[i] == '(':
            stack.append(vps[i])
        elif vps[i] == ')':
            if len(stack) == 0:
                stack.append(vps[i])
                break
            else:
                stack.pop()
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')