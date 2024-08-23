T = int(input())

for tc in range(1, T+1):
    rooms = [0]*200
    N = int(input())
    for _ in range(N):
        A, B = map(int, input().split())
        if A > B:
            A, B = B, A
        for i in range((A-1)//2, (B-1)//2+1):
            rooms[i] += 1
    print(f'#{tc} {max(rooms)}')

# T = int(input())
# for t in range(1, T + 1):
#     N = int(input())
#     cnts = [0] * 200
#     for _ in range(N):
#         s, e = map(int, input().split())
#         if s > e:
#             s, e = e, s
#
#         for i in range((s - 1) // 2, (e - 1) // 2 + 1):
#             cnts[i] += 1
#
#     print(f'#{t} {max(cnts)}')