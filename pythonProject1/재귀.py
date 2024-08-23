path = []
used = [False, False, False]


def KFC(x):
    if x == 2:
        # 정점 노드에 도달했을때 출력
        print(path)
        return

    for i in range(3):
        # 이미 사용을 한 숫자(path)인지 아닌지 구분하는 코드
        # 만약 이미 사용한 숫자인 경우 재귀호출을 생략
        # 재귀호출을 하기 직전에 path리스트에 기록한다.
        if used[i] == 1:
            continue
        # 처음 사용하는 숫자(흔적)이라면 used에 기록
        used[i] = True
        path.append(i)
        KFC(x + 1)
        # 함수가 리턴되고 되돌아오자마자 기록을 삭제
        path.pop()
        # 모든 처리가 끝나고 돌아왔다면, used배열의 기록을 지워준다.
        used[i] = False


KFC(0)