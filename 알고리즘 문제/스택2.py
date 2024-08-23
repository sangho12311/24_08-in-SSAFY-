T = int(input())
stack=[]
for _ in range(T):
    cod = list(map(int,input().split()))
    if cod[0] == 1:
        stack.append(cod[1])
    elif cod[0] == 2:
        if stack:
            stack.pop()
            if stack:
                print(stack[0])
            else:print(-1)
        else:
            print(-1)

    elif cod[0] == 3:
        print(len(stack))

    elif cod[0] == 4:
        if stack:
            print(0)
        else:
            print(1)
    elif cod[0] == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)

