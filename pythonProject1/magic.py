def magic(N,K,arr):
    dy=[-1,-1,1,1]
    dx=[1,-1,-1,1]
    monster_sum=0

    for i in range(4):
        for j in range(1,K+1):
            monster_sum+=[dy+j][dx+j]



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

