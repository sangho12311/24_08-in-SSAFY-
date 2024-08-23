def omok(arr):
    dr=[1,1,0,-1]
    dc=[0,1,1,1]
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 'o':
                for i in range(4):
                    cnt = 0
                    if 0 <= r+5*dr[i] < N and 0 <= c+5*dc[i] <N:
                        for k in range(1, 5):
                            nr = r + k*dr[i]
                            nc = c + k*dc[i]
                        if arr[nr][nc]!='o':
                            break
                        else:
                            cnt += 1
                        if cnt == 5:
                            return 'YES'
    return 'NO'

T=int(input())
for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int,input().split())) for _ in range(N)]
    result = omok(table)
    print(f'#{tc} {result}')
