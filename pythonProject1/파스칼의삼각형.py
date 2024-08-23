def pascal(N):
    result = [1]
    stack = [1]
    for i in range(N):
        print(*stack, sep=" ")
        result = stack
        stack=[]
        stack.append(1)
        if len(result)>1:
            for j in range(len(result)-1):
                stack.append(result[j]+result[j+1])
            stack.append(1)
        else:
            stack.append(1)

T = int(input())
for tc in range(1,T+1):
    n=int(input())
    print(f'#{tc}')
    pascal(n)
