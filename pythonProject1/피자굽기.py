# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#
from collections import deque

def bake_pizza(N, M, cheese):
    # 화덕에 들어가는 피자를 추적하기 위해 deque를 사용
    # 화덕에는 N개의 피자만 들어갈 수 있음
    oven = deque()

    # 피자 번호와 치즈 양을 함께 저장하기 위해 (피자 번호, 치즈 양)의 튜플을 사용
    for i in range(N):
        oven.append((i + 1, cheese[i]))  # 초기 화덕에 N개의 피자 넣기

    # 남은 피자들을 대기열에 추가
    waiting = deque([(i + 1, cheese[i]) for i in range(N, M)])

    last_pizza = None

    while oven:
        pizza_num, pizza_cheese = oven.popleft()  # 화덕에서 피자 하나 꺼내기

        pizza_cheese //= 2  # 꺼낸 피자의 치즈 양을 반으로 줄이기

        if pizza_cheese > 0:  # 아직 치즈가 남아 있으면 다시 화덕에 넣기
            oven.append((pizza_num, pizza_cheese))
        else:
            # 치즈가 모두 녹았다면 그 자리에 대기 중인 피자를 넣음
            if waiting:
                oven.append(waiting.popleft())

        # 현재 화덕에 피자가 남아있다면 그 피자가 마지막 피자 후보
        if oven:
            last_pizza = oven[-1][0]

    return last_pizza  # 마지막으로 남아있는 피자의 번호 반환


# 입력 받기
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))

    result = bake_pizza(N, M, cheese)
    print(f'#{tc} {result}')