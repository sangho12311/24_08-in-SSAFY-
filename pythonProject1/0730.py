# 버블 정렬 : 인접한 두 요소를 비교하여 큰 값을 오른쪽으로 이동시키는 과정을 반복
numbers = [62, 31, 27, 11, 25]

def bubble(arr) :
    # 배열의 모든 요소 순회
     for i in range(len(arr)) :
         # 배열의 끝에서 정렬된 부분을 제외하고 순회
        for j in range(len(arr) - i - 1) :
            # 인접한 두 요소 비교하여 위치 바꾸기
            if arr[j] > arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

bubble(numbers)
print(numbers)

# 카운팅 정렬 : 각 숫자의 개수를 세어서 정수를 정렬하는 알고리즘
numbers = [1, 4, 1, 2, 13, 5, 2]

def counting(arr) :
    # arr의 최댓값
    # max_v = max(arr)
    max_v = float('-inf') # 음의 무한대
    for num in arr :
        if num > max_v :
            max_v = num
    # 카운트 배열 초기화
    count = [0] * (max_v + 1)
    # 카운팅!! 각 숫자의 출현 횟수 세기
    for num in arr :
        count[num] += 1
    # 카운트 배열을 기반으로 정렬된 리스트 만들기
    sorted_arr = []
    for i in range(len(count)) :
        for j in range(count[i]) :
            sorted_arr.append(i)

    return sorted_arr

result = counting(numbers)
print(result)

# 순열 : 주어진 항목들로 만들 수 있는 모든 가능한 순서
import itertools
lst = [1, 2, 3]
# permutations(lst) : lst의 순열
print(list(itertools.permutations(lst)))
# combinations(lst, N) : lst에서 N개의 원소를 가진 모든 조합(원소의 중복 X)
print(list(itertools.combinations(lst, 2)))

# 탐욕(그리디) 알고리즘 : 각 단계에서 가장 최선의 선택을 하는 방법
# 대표적인 예제 문제 : 거스름돈 문제(100원, 50원, 10원)
# 거스름돈을 줄 때 최선의 선택 : 가장 큰 단위의 동전부터 사용
# 거스름돈이 380원이고, 동전 종류가 100원, 50원, 10원
# Q) 어떻게 해야 가장 적은 수의 동전으로 거스름돈을 받을 수 있을까?
# A) {100 : 3, 50 : 1, 10 : 3}
money = int(input())
coins = [100, 50, 10]
answer = {}

for coin in coins :
    answer[coin] = money // coin
    money %= coin
print(answer)

## GRAVITY

def gravity(boxs) :
    max_v = 0   #최대 낙차 저장할 변수 초기화
    for idx, box in enumerate(boxs) : # 각 상자의 인덱스, 높이
        fall = 0 # 현재 상자의 낙차 계산 변수 초기화
        for next in range(idx + 1, N) : # 현재 상자의 뒤에 있는 상자들
            if box > boxs[next] : # 현재 상자의 높이가 밑에 있는 상자보다 높으면
                fall += 1 # 낙차를 1씩 증가
        max_v = max(max_v, fall)
    return max_v # 최대 낙차 반환

T = int(input())
for tc in range(1, T + 1) :
    N = int(input())
    boxs = list(map(int, input().split()))
    result = gravity(boxs)
    print(f'#{tc} {result}')

# 숫자 카드

T = int(input())
for tc in range(1, T + 1) :
    N = int(input())
    a = list(map(int, input()))

    cnt = [0] * 10 # 0부터 9까지 각 숫자 카드의 갯수 저장할 리스트 초기화
    for j in range(N) :
        cnt[a[j]] += 1 # 해당 숫자 카드의 개수를 하나 증가
    result = 0 # 현재 가장 많이 발견된 카드 갯수
    for k in range(len(cnt)) :
        if result <= cnt[k] :
            result = cnt[k] # 그 카드의 갯수
            idx = k # 가장 많은 카드의 숫자
    # 1. cnt[k] result보다 큰 경우 : 더 많은 카드를 발견한 경우
    # 2. cnt[k] result와 같은 경우 : 같은 갯수의 카드를 발견했으나,
    #                                더 큰 숫자의 카드를 우선시 idx 업데이트
    print(f'#{tc} {idx} {result}')