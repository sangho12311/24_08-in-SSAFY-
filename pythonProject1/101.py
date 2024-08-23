def make_101(lst, index, str_num, value, result):
    if index == len(lst):
        if value != 0 and value % 101 == 0:
            result.append(str_num)
        return

    next_value = lst[index]
    make_101(lst, index + 1, f'{str_num}*{next_value}', value * next_value, result)
    make_101(lst, index + 1, f'{str_num}+{next_value}', value + next_value, result)
    make_101(lst, index + 1, f'{str_num}-{next_value}', value - next_value, result)


n = int(input())
lst = list(map(int, input().split()))
result = []
make_101(lst, 1, str(lst[0]), lst[0], result)

for i in range(len(result)):
    print(result[i])