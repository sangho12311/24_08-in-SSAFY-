#버블정렬, 카운팅정렬, 선택정렬
# 선택정렬
# 1. 현재 위치 설정: 배열의 첫 번째 원소부터
# 2. 현재 위치부터 배열의 끝까지 검색하여 최소값 찾기
# 3. 찾은 최소값을 현재 위치의 원소와 교환
# 4. 이 과정을 왼쪽에서 오른쪽으로 현재위치를 다음 원소로 이동시키면서 반복
''
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # 1번
        min_idx =i
        # 2번
        for j in range(i+1, n):
            if arr[j]<arr[min_idx]:
                min_idx =  j
        # 3번
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]

sorted_arr= selection_sort(arr)

print(sorted_arr)
'''

# 이진 탐색
# 1. 중간값 계산 (start +end) //2
# 2. 중간값이 찾고자 하는 값(target)보다 크면 왼쪽 부분 탐색: end = mid -1
# 3. 중간값이 찾고자 하는 값(target)보다 작으면 오른쪽 부분 탐색 : start = mid +1
# 원소가 5개인경우 (홀수) : (0+4)//2 ==2, 원소의 6개인 경우 (짝수) : (0+5)//2 == 2

def binary_search(arr,target):
    start=0
    end=len(arr)-1

    while start <= end:
        mid = (start + end)//2
        # 이진 탐색해서 타겟을 찾으면 값(인덱스)를 반환
        if arr[mid] == target:
            return mid
        # 타겟이 중간값보다 크면 오른쪽 부분 탐색
        elif arr[mid]<target:
            start = mid +1
        # 타겟이 중간값 보다 작으면 왼쪽 부분 탐색
        elif arr[mid]<target:
            start = mid-1
        else:
            end = mid -1
    # 타겟 못찾았을 경우
    return -1
arr =[1,3,5,7,9,11,13,15,17]

target =11
result=binary_search(arr,target)
print(f'target index : {result}')
