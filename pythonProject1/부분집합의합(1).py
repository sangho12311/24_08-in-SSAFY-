T= int(input())
for tc in range(1, T+1):
    stack = []
    cnt = 0
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))


    def subset_sum(N, S, arr, start):
      global cnt
      if sum(stack) == S:
          cnt += 1

      for i in range(start, N):

          stack.append(arr[i])
          subset_sum(N, S, arr, i + 1)
          stack.pop()
      return cnt


    print(f'#{tc} {subset_sum(N, S, sorted(arr), 0)}')




