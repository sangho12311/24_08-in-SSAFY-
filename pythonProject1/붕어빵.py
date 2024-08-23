# def fishbread(M, K, P_lst):
#     time = 0
#     bread = 0
#     for time in range(1, max(P_lst)+1):
#
#         if time % M == 0:
#             bread += K
#
#         while time in P_lst:
#             if bread > 0:
#                 bread -= 1
#                 P_lst.remove(time)
#             elif bread == 0:
#                 return 'Impossible'
#
#     return 'Possible'
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M, K = map(int, input().split())
#     p_lst = list(map(int, input().split()))
#     p_lst.sort()
#     print(f'#{tc} {fishbread(M, K, p_lst)}')
# ####################################
# def fishbread(M, K, P_lst):
#     bread = 0
#
#     for time in P_lst:  # 손님 도착 시간에 맞춰 확인합니다.
#         bread = (time // M) * K  # 해당 시간까지 만들 수 있는 빵의 수
#         if P_lst.index(time) + 1 > bread:  # 손님이 도착했을 때 빵이 부족한지 확인합니다.
#             return 'Impossible'
#
#     return 'Possible'
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M, K = map(int, input().split())
#     p_lst = list(map(int, input().split()))
#     p_lst.sort()  # 손님 도착 시간을 오름차순으로 정렬합니다.
#     print(f'#{tc} {fishbread(M, K, p_lst)}')

from collections import deque

T = int(input())

result = []

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arrive_lst = list(map(int, input().split()))

    arrive_lst.sort()
    possible = True

    for i in range(N):
        time = arrive_lst[i]
        left_fish = (time // M) * K

        if left_fish < (i + 1):
            possible = False
            break

    if possible:
        result.append(f'#{tc} Possible')
    else:
        result.append(f'#{tc} Impossible')

for res in result:
    print(res)














