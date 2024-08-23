# arr에서 합계, S : 목표합계
def get_sub(arr, N, S):
    cnt = 0
    for tar in range(1, 1 << N): #공집합 제외하고
        sub_sum = 0
        for i in range(N):
            if tar & 0x1:
                sub_sum += arr[i]
            tar >>= 1 # 검사를 마친 한 자리를 제거한다
        # sub_sum과 목표합이 같으면 카운트
        if sub_sum == S:
            cnt += 1
    return cnt

T = int(input())
for tc in range(1, T + 1):
    N, S = map(int, input().split()) # N: 집합의 크기, S : 목표 합
    arr = list(map(int, input().split()))
    result = get_sub(arr, N ,S)
    print(f'#{tc} {result}')