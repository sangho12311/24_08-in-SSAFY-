T = int(input())

answer = []
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
for tc in range(T):
    lst = list(map(int, input().split()))
    N = lst[0]
    K = lst[1]
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            sums = 0
            sums += arr[i][j]
            for k in range(4):
                for l in range(1, K + 1):
                    ny, nx = i + dy[k] * l, j + dx[k] * l
                    if 0 <= nx < N and 0 <= ny < N:
                        sums += arr[ny][nx]
            if sums > result:
                result = sums
    answer.append(result)
for i in range(T):
    print(f'#{i + 1}', answer[i])