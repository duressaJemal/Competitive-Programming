def merge(a, b):

    c = [0] * (len(a) + len(b))

    l = 0
    r = 0

    while l < len(a) or r < len(b):

        if r >= len(b) or (l < len(a) and a[l] <= b[r]):
            c[l + r] = a[l]
            l += 1
        else:
            c[l + r] = b[r]
            r += 1
    
    return c

def mergeSort(left, right, arr):
    if left == right:
        return [arr[left]]
    mid = left + (right - left) // 2
    left_half = mergeSort(left, mid, arr)
    right_half = mergeSort(mid + 1, right, arr)

    return merge(left_half, right_half)

def test():
    assert mergeSort(0, 5, [3, 0, 2, -5, 10, 2]) == [-5, 0, 2, 2, 3, 10], "Not Implemented Properly"
    assert mergeSort(0, 2, [1, 2, 3]) == [1, 2, 3], "Not Implemented Properly"
    assert mergeSort(0, 2, [3, 2, 1]) == [1, 2, 3], "Not Implemented Properly"
    assert mergeSort(0, 1, [-5, -1]) == [-5, -1], "Not Implemented Properly"
    assert mergeSort(0, 0, [-1]) == [-1], "Not Implemented Properly"

    print("Great Job !!!")
test()