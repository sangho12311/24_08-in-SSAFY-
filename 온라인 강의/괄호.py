T=int(input())

for _ in range(T):
    stack=[]
    vps=list(str(input()))
    for i in vps:
        vps.append(i)
        if i==')':
            vps.pop()
    if stack==[]:
        print('YES')
    else:
        print('NO')

    