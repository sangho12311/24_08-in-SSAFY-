def flies(x,y):

    sum=0
    for i in range(M):
        for j in range(M):
            if 0<=x+i<N and 0<=y+j<N:
                sum+=arr[x+i][y+j]
    return sum

T=int(input())
for tc in range(T):
    N,M=map(int,input().split())
    arr=[list(map(int,input().split())) for i in range(N)]
    result_lst=[]
    for l in range(N):
        for k in range(N):
            result_lst.append(flies(l,k))
    print(f'#{tc+1} {max(result_lst)}')