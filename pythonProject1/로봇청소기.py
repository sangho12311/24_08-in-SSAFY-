di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
def solve(ci,cj,cd):
    cnt = 0
    while True:
        arr[ci][cj] = 2
        cnt += 1
        flag = 1
        while flag == 1:
            for nd in ((cd+3)%4, (cd+2)%4, (cd+1)%4, cd):
                ni, nj = ci+di[nd], cj+dj[nd]
                if arr[ni][nj] == 0:
                    ci, cj, cd = ni, nj, nd
                    flag = 0
                    break
            else:
                bi, bj = ci-di[cd], cj - dj[cd]
                if arr[bi][bj] == 1:
                    return cnt
                else:
                    ci, cj = bi, bj


N, M = map(int,input().split())
si, sj, sd = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
result = solve(si, sj, sd)
print(result)


