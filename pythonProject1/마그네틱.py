T = 10
for test_case in range(1, 1+T):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        j = 0
        while j < 100:
            if arr[j][i] == 1:
                while j < 100:
                    if arr[j][i] == 2:
                        ans += 1
                        break
                    else:
                        j += 1
            j += 1
    print(f'#{test_case} {ans}')
