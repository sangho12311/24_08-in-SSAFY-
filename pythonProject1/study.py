# for i in range(1, 4):


# def KFC(x):
#     if x==6:
#         return
#     else:
#         print(x)
#         KFC(x + 1)
#         print(x)
#
# KFC(0)
# print('끝')
#
# def KFC(x):
#     if x==3:
#         return
#     KFC(x + 1)
#     KFC(x + 1)
#     KFC(x + 1)
#     KFC(x + 1)
#     print(x)
# KFC(0)

# def KFC(x):
#     if x==3:
#         for i in range(2):
#             KFC(x+1)
#     print(x)
#
# KFC(0)


# def run(level):
#     if level == 3 :
#         return
#     for i in range(2):
#         run(level + 1)
#
# run(0)

# path = []
# used = [0, 0]
# def KFC(x):
#     if x == 2:
#         print(path)
#         return
#     for i in range(1,7):
#         if used[i] == 1:
#             continue
#         used[i] = 1
#         path.append(i)
#         KFC(x + 1)
#         path.pop()
#         used[i] = 0
# KFC(0)
# --------------------------------------------
# path = []
# used = []
# N = 0
# cnt = 0
#
# def type1(x, cnt):
#     if x == N:
#         print(path)
#         return
#
#     for i in range(1, 7):
#         path.append(i)
#         type1(x + 1)
#         path.pop()
#         cnt += 1
#
#
# def type2(x):
#     if x == N:
#         print(path)
#         return
#
#     for i in range(1, 7):
#         if used[i] == True: continue
#         used[i] = True
#         path.append(i)
#         type2(x + 1)
#         path.pop()
#         used[i] = False
#
#
# N, type = map(int, input().split())
# used = [False for _ in range(7)]
#
# if type == 1:
#     type1(0)
# if type == 2:
#     type2(0)

###################################
# 완전 탐색: 모든 경우의 수를 다 찾아서 정답을 찾아내는 것
# 주사위 3개를 굴려서 합계가 10이하인 모든 경우의 수를 찾기


path = []
cnt = 0
def kfc(x,sum_v):
    global cnt
    #가지치기 : 합계가 10보다 크면 탐색 x
    if sum_v > 10:
        return

    if x==3:
        cnt +=1
        return
    for i in range(1,7):
        path.append(i)
        kfc(x+1, sum_v + i)
        path.pop()

kfc(0, 0)
print(cnt)

###################################




