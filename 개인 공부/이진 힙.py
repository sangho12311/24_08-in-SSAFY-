import heapq

T = int(input())
for tc in range(1, T+1):
    heap = []
    temp = []
    N = int(input())
    i = N
    nums = list(map(int, input().split()))
    for _ in range(N):
        heapq.heappush(heap, nums[_])
    print(heap)
    while i != 1:
        i = i//2
        temp.append(heap[i-1])
    print(f'#{tc} {sum(temp)}')

