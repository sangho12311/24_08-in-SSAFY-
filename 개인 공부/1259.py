while True:
    N = input()
    if N == '0':
        break
    lst = list(N)
    # print(lst)
    r_lst = list(reversed(lst))
    # print(r_lst)
    if lst == r_lst:
        print('yes')
    else:
        print('no')
