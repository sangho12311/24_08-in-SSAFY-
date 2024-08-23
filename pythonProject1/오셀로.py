T = int(input())
result = []
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]
    mid = N // 2
    arr[mid][mid] = 2
    arr[mid - 1][mid - 1] = 2
    arr[mid - 1][mid] = 1
    arr[mid][mid - 1] = 1
    di = [1, 1, 1, -1, -1, -1, 0, 0]
    dj = [1, 0, -1, 1, 0, -1, 1, -1]
    color = [0, 2, 1]
    for _ in range(M):
        x, y, c = map(int, input().split())
        x, y = x - 1, y - 1
        arr[x][y] = c
        for k in range(8):
            ni, nj = x + di[k], y + dj[k]
            stack = []
            while 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == color[c]:
                stack.append([ni, nj])
                ni += di[k]
                nj += dj[k]
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == c:
                    for ni, nj in stack:
                        arr[ni][nj] = c
    Black, White = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                Black += 1
            elif arr[i][j] == 2:
                White += 1
    result.append([Black, White])

for i in range(T):
    print(f'#{i + 1}', result[i][0], result[i][1])