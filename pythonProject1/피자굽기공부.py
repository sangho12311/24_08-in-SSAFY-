from collections import deque


def bake_pizza(N, M, arr):
    oven = deque()
    for i in range(N):
        oven.append((i + 1, arr[i]))

    waiting = deque([(i + 1, arr[i]) for i in range(N, M)])
    last_pizza = None

    while oven:
        pizza_num, pizza_cheese = oven.popleft()
        pizza_cheese //= 2
        if pizza_cheese > 0:
            oven.append((pizza_num, pizza_cheese))
        else:
            if waiting:
                oven.append(waiting.popleft())
        if oven:
            last_pizza = oven[-1][0]

    return last_pizza
T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = list(map(int,input().split()))

    result = bake_pizza(N, M, arr)
    print(f'#{tc} {result}')