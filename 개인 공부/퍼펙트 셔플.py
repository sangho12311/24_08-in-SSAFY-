def slice(N, arr):
    global r_lst
    if N % 2 == 0 :
        k = N // 2
        i = 0
        while len(r_lst) != N:
            r_lst.append(arr[i])
            r_lst.append(arr[k])
            i += 1
            k += 1
        return r_lst
    else:
        k = N // 2 +1
        i = 0
        # r_lst.append(arr[i])
        while len(r_lst) != N:
            r_lst.append(arr[i])
            if len(r_lst) == N:
                return r_lst
            r_lst.append(arr[k])
            i += 1
            k += 1
        return r_lst

T = int(input())
for tc in range(1, T+1):
    r_lst = []
    N = int(input())
    arr = list(input().split())
    print(f'#{tc} {" ".join(slice(N, arr))}')

