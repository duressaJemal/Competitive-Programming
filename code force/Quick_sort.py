def quick_sort(l, r, arr):

    if l >= r:
        return
    
    pivot = arr[l]
    write = l
    
    for read in range(l, r + 1):
        if arr[read] <= pivot:
            arr[read], arr[write] = arr[write], arr[read]
            write += 1 

    arr[l], arr[write - 1] = arr[write - 1], arr[l]
    quick_sort(l, write - 2, arr)
    quick_sort(write, r, arr)

    return

def test():
    arr = [3, 0, 2, -5, 10, 2]
    quick_sort(0, 5, arr)
    print(arr)
    
    # assert quick_sort(0, 5, [3, 0, 2, -5, 10, 2]) == [-5, 0, 2, 2, 3, 10], "Not Implemented Properly"
    # assert quick_sort(0, 2, [1, 2, 3]) == [1, 2, 3], "Not Implemented Properly"
    # assert quick_sort(0, 2, [3, 2, 1]) == [1, 2, 3], "Not Implemented Properly"
    # assert quick_sort(0, 1, [-5, -1]) == [-5, -1], "Not Implemented Properly"
    # assert quick_sort(0, 0, [-1]) == [-1], "Not Implemented Properly"

    print("Great Job !!!")
test()

11101