N = int(input())
scores = list(map(int, input().split()))
M = max(scores)
n_scores = []
for i in range(N):
    ns = (scores[i]/M)*100
    n_scores.append(ns)
result = sum(n_scores)/N
print(result)
