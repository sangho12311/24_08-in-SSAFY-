T = int(input())
answer = []
for tc in range(T):
    N = int(input())
    result = []
    arr1 = [list(map(int, input().split())) for _ in range(N)]
    check = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for l in range(j, N):
                    if i == k and j < l and arr1[i][j] == arr1[k][l]:
                        result.append((abs(i - k) + 1) * (abs(j - l) + 1))

                    if i < k and arr1[i][j] == arr1[k][l]:
                        result.append((abs(i - k) + 1) * (abs(j - l) + 1))
    if result:
        mx = max(result)
        count = result.count(mx)
    else:
        count = 0
    answer.append(count)

for i in range(T):
    print(f'#{i + 1} {answer[i]}')