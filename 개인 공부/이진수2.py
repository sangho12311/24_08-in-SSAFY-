# 이진수2
T = int(input())
for tc in range(1, T+1):
    n = float(input())
    cnt = 0
    bin = ''
    while n > 0:
        temp = n * 2
        bin += str(temp)[0] #정수부분을 이진수 문자열에 추가
        n = temp - int(temp)
        cnt += 1
        if cnt > 12: #이진수 자리수가 12자리 넘어가면 break
            break
    if  cnt > 12:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc} {bin}')

