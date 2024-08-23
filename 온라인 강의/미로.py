def fstart(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i ,j 


T=int(input())
for tc in range(1,T+1):
    N=int(input())
    maze = [list(map(int,input())) for _ in range(N)]

    #출발 위치 찾기
    sti,stj = fstart(N)

    visited = [[0] * N for _ in range(N)]