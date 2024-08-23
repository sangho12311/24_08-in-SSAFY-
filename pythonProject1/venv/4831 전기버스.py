def bus(K, N, char):
    course = [0] * N
    for i in char:
        course[i] = 1
    bat = K
    me = 0
    cnt = 0
    while bat > 0:
        bat -= 1
        if course[me] == 1:
            bat = K
            cnt += 1
        me += 1
        if me == N:
            return cnt
    return cnt

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    char = list(map(int, input().split()))
    print(f'{tc} {bus(K, N, char)})

