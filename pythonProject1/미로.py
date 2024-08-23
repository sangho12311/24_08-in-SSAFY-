from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def solve(ci, cj):
    queue = deque()
    queue.append([ci, cj, 0])
    visited = [[False] * N for _ in range(N)]
    visited[ci][cj] = True
    while queue:
        ci, cj, dist = queue.popleft()

        if arr[ci][cj] == 3:
            return dist - 1

        for k in range(4):
            ni, nj = ci + di[k], cj + dj[k]
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == False and arr[ni][nj] != 1:
                visited[ni][nj] = True
                queue.append([ni, nj, dist + 1])
    return 0


T = int(input())
ans = []
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().strip())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si, sj = i, j
    ans.append(solve(si, sj))

for i in range(T):
    print(f'#{i + 1}', ans[i])