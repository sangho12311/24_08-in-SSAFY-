import sys
input = sys.stdin.readline
def bfs(n,lst_A,lst_B):
    global ans
    if n ==N:
        if len(lst_A) == len(lst_B):
            ans = min(ans,cal(lst_A, lst_B))
        return

    bfs(n+1, lst_A+[n], lst_B)
    bfs(n+1, lst_A, lst_B+[n])

def cal(lst_A,lst_B):
    asums = 0
    bsums = 0
    for i in range(M):
        for j in range(M):
            asums +=  arr[lst_A[i]][lst_A[j]]
            bsums +=  arr[lst_B[i]][lst_B[j]]
    return abs(asums-bsums)

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
M = N//2
ans = float('inf')
bfs(0,[],[])
print(ans)