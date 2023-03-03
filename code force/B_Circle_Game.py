def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    
    current_index = 0
    turn = 1

    while arr[current_index] != 0:
        
        arr[current_index] = 0
        current_index = (current_index  % n) + 1
        turn = 1 - turn
        
    
    if turn:
        print("Joe")
    else:
        print("Mike")



t = int(input())
while t:
    solve()
    t -= 1
