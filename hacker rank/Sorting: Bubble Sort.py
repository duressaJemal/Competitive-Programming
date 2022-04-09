def countSwaps(a):
    # Write your code here
    counter = 0;
    for i in range(n):
        for j in range(n-1):
            if (a[j] > a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
                counter += 1
    print("Array is sorted in " + str(counter) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[-1]))
                
            
