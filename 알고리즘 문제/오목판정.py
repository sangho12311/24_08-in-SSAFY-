def rock(N,r,c,arr):
    cnt=0
    for i in range(5): # x축 방향으로 진행 
        if r+5<=N:
            if arr[r+i][c]=='o':
                cnt+=1
            else:
                break
    if cnt == 5: 
        return 'YES'
    
    cnt=0
    for j in range(5): # y축 방향으로 진행 
        if c+5<=N:
            if arr[r][c+j]=='o':
                cnt+=1
            else:
                break
    if cnt == 5: 
        return 'YES'
    
    cnt=0
    for k in range(5): # 오른쪽 아래 방향으로 진행
        if r+5<=N and c+5<=5:
            if arr[r+k][c+k]=='o':
                cnt+=1
            else:
                break
    if cnt == 5: 
        return 'YES'
    
    cnt=0
    for l in range(5): #왼쪽 아래 방향으로 진행 
        if r+5<=N and c-5>=0:
            if arr[r+l][c-l]=='o':
                cnt+=1
            else:
                break
    if cnt == 5: 
        return 1
    
    return 2

T = int(input())
for tc in range(1,T+1):
    N=int(input())
    arr = [list(str(input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if rock(N,i,j,arr) == 1:
                print('YES')
                break
    print('NO')