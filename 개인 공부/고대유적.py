def sol(N, M, table):
    ans = 0
    dr = [1, 0]
    dc = [0, 1]
    R = max(N, M)
    for r in range(N):
        for c in range(M):
            if table[r][c] == 1:
                for i in range(2):
                    t_cnt = 1
                    for k in range(1, R):
                        nr = r + dr[i]*k
                        nc = c + dc[i]*k
                        if 0 <= nr < N and 0 <= nc < M:
                            if table[nr][nc] == 1:
                                t_cnt += 1
                                if ans < t_cnt:
                                    ans = t_cnt
                            else:
                                if ans < t_cnt:
                                    ans = t_cnt
                                    t_cnt = 1

    return ans
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(M)]
    result = sol(N, M, table)
    print(f'#{tc} {result}')
