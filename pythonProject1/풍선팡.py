def pang(r,c,table):
    sum = 0
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    k = table[r][c]
    for i in range(4):
        for j in range(1, k+1):
            nr = r+dr[i]*j
            nc = c+dc[i]*j
            if 0 <= nr < N and 0 <= nc < M:
                sum += table[nr][nc]
    sum += table[r][c]
    return sum

T = int(input())
for tc in range(1, T+1):
    result = 0
    max_lst = 0
    N, M = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(N)]

    for r in range(N):
        for c in range(M):
            result = pang(r, c, table)
            if result > max_lst:
                max_lst = result
    print(f'#{tc} {max_lst}')

