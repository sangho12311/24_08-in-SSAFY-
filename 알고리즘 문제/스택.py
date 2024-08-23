T=int(input())
stack=[]
for k in range(T):
    code = str(input())
    if 'push' in code :
        _ ,i = code.split()
        stack.append(int(i))
        
    elif code == 'top':
        if stack:
            print(stack[-1])
        else: 
            print(-1)

    elif code == 'pop':
        if stack:
            print(stack[-1])
            stack.pop()
        else: 
            print(-1)

    elif code == 'size':
        print(len(stack))

    elif code == 'empty':
        if stack:
            print(0)
        else:
            print(1)