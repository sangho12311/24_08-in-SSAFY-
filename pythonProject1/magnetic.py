def meg(arr):
    cnt = 0
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 1:
                for k in range(1, 100):
                    if i + k < 100:
                        if arr[i + k][j] == 2:
                            cnt += 1
                            break
                        if arr[i + k][j] == 1:
                            break

    return cnt


for tc in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for i in range(100)]
    print(f'#{tc} {meg(table)}')
