'''
# 이진수 2
T = int(input())
for tc in range(1, T + 1):
    n = float(input())
    cnt = 0
    bin = ''
    while n > 0:
        temp = n * 2
        bin += str(temp)[0] # 정수 부분을 이진수 문자열에 추가
        n = temp - int(temp) # 남은 소수부분을 n에 할당
        cnt += 1
        if cnt > 12: # 이진수 자리수가 12자리 넘어가면 break
            break

    if cnt > 12:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc} {bin}')

'''

# 이진수 표현
# 첫 번째 방법. 11111, for N번 순회 right shift 비트 연산자 총 N번 검사
# 두 번째 방법. (1111 + 1) ---> 100000
'''
def bit(N, M):
    tar = M
    for i in range(N):
        if tar & 0x1 == 0:
            return "OFF"
        tar = tar >> 1 # 오른쪽으로 밀면서 M의 1비트 1인것을 확인
    return "ON"

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    result = bit(N, M)
    print(f'#{tc} {result}')
'''
'''
def bit(N, M):
    power_of = 1 << N
    if (M + 1) % power_of == 0:
        return "ON"    
    else:
        return "OFF"

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    result = bit(N, M)
    print(f'#{tc} {result}')

'''