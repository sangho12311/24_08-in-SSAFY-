import math
def Map(N,arr):
    Two_r = 0
    Two_c = 0
    length_lst=[]
    for r in range(N+1):
        for c in range(N+1):
            if arr[r][c] == 2:
                Two_r,Two_c = r,c

    for i in range(N+1):
        for j in range(N+1):
            if arr[i][j] == 1:
                length = ((abs(i-Two_r))**2 + (abs(j-Two_c))**2)**0.5
                length_lst.append(length)

    return math.ceil(max(length_lst))

T=int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N+1)]
    result = Map(N, arr)
    print(f'#{tc} {result}')