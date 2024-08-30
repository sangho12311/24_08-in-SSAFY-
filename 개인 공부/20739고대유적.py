T = int(input())
for tc in range(T):
    H, W, N = map(int, input().split())
    X = (N//H)+1
    Y = N % H
    if Y == 0:
        X -= 1
        Y = H

    print(Y*100+X)