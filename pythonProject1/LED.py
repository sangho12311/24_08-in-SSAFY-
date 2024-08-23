T = int(input())
for tc in range(1, T+1):
    N = int(input())
    LED_p = list(map(int, input().split()))
    c_p = [0]*N
    cnt = 0
    for i in range(0, N):
        if c_p[i] != LED_p[i]:
            for j in range(0, N):
                if (j+1) % (i+1) == 0:
                    if c_p[j] == 0:
                        c_p[j] = 1

                    elif c_p[j] == 1:
                        c_p[j] = 0
            cnt += 1
    print(f'#{tc} {cnt}')