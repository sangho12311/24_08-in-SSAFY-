def bus(K, N, char):
    course = [0] * (N+1)
    for i in char:
        course[i] = 1
    bat = K
    me = 0
    cnt = 0
    temp = 0
    while me < N:
        me += 1
        if me == N:
            return cnt
        bat -= 1
        if course[me] == 1:
            if bat < (N-me):
                for j in range(1, bat+1):
                    if course[me+j] == 1:
                        temp += 1
                        continue
                if temp == 0:
                    bat = K
                    cnt += 1
                    temp = 0
                else:
                    temp = 0
        if bat == 0:
            return 0
    return cnt

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    char = list(map(int, input().split()))
    print(f'#{tc} {bus(K, N, char)}')

