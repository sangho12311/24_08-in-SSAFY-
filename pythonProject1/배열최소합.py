T=int(input())

N=int(input())
lst=[list(map(int,input().split())) for i in range(N)]

def minsum(lst):
    if cur_sum >= min_sum:
        return
    if x == N:
        min_sum = min(min_sum,cur_sum)
        return
    for i in range(N):
        if used[i]: continue

