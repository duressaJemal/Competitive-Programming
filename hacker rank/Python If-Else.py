# Link: https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=false
#Q: Python If-Else

if n % 2 == 0:
    if 2 <= n <= 5 or n > 20:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
else:
    print("Weird")
