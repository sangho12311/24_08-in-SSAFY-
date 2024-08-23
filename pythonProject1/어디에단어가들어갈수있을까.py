def word(N, M, arr):
    ans = 0
    for i in range(N):
        cont = 0
        for j in range(N):
            if arr[i][j] == 1:
                cont += 1
            else:
                if cont == M:
                    ans += 1
                    cont = 0
                else:
                    cont = 0
        if cont == M:
            ans += 1
    for j in range(N):
        cont = 0
        for i in range(N):
            if arr[i][j] == 1:
                cont += 1
            else:
                if cont == M:
                    ans += 1
                    cont = 0
                else:
                    cont = 0
        if cont == M:
            ans += 1
    return ans


results = []
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = word(N, M, arr)
    results.append(result)

for i in range(T):
    print(f'#{i + 1}', results[i])