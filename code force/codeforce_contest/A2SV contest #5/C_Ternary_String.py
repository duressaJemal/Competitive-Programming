from collections import defaultdict

t = int(input())

while t:

    arr = list(map(int, input()))
    n = len(arr)

    dic = defaultdict(int)

    def is_good(dic):
        return len(dic) == 3

    minimum = float("inf")
    left = 0
    for right in range(n):

        # add
        dic[arr[right]] += 1

        # isgood
        while is_good(dic):
            minimum = min(minimum, right - left + 1)
            # remove
            dic[arr[left]] -= 1
            if not dic[arr[left]]:
                dic.pop(arr[left])
            left += 1

    if minimum == float("inf"):
        print(0)
    else:
        print(minimum)
        
    t -= 1