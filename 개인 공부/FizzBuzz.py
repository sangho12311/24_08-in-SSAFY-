i1 = input()
i2 = input()
i3 = input()
if i3.isdigit():
    if (int(i3)+1) % 3 == 0:
        if (int(i3)+1) % 5 == 0:
            print('FizzBuzz')
        else:
            print('Fizz')
    elif (int(i3)+1) % 5 == 0:
        print('Buzz')

    else:
        print((int(i3)+1))

elif not i3.isdigit():
    if i2.isdigit():
        if (int(i2) + 2) % 3 == 0:
            if (int(i2) + 2) % 5 == 0:
                print('FizzBuzz')
            else:
                print('Fizz')
        elif (int(i2) + 2) % 5 == 0:
            print('Buzz')
        else:
            print(int(i2) + 2)

    elif not i2.isdigit():
        if (int(i1) + 3) % 3 == 0:
            if (int(i1) + 3) % 5 == 0:
                print('FizzBuzz')
            else:
                print('Fizz')
        elif (int(i1) + 3) % 5 == 0:
            print('Buzz')
        else:
            print(int(i1) + 3)

