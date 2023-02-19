t = int(input())

while t:

    arr = input()
    n = len(arr)

    if n > 10:
        print(f'{arr[0]}{n - 2}{arr[-1]}')
    else:
        print(arr)

    t -= 1