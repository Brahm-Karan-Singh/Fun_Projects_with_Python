a = int(input('Enter no. of rows for your pattern\n'))
b = int(input('Select method for pattern either 0 or 1\n'))
if b == 0:
    i = 1
    for x in range(0, a):
        print('*' * i, end="")
        i += 1
        print()
else:
    i = a
    for x in range(0, a):
        print('*' * i, end="")
        i -= 1
        print()


