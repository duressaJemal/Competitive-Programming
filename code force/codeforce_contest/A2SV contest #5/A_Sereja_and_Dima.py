# Link: 

n = int(input())
arr = list(map(int, input().split()))

player1 = 0
player2 = 0

turn = 1

left = 0
right = n - 1

while left <= right:

    if arr[left] > arr[right]:
        value = arr[left]
        left += 1
    else:
        value = arr[right]
        right -= 1
    
    if turn:
        player1 += value
    else:
        player2 += value
    
    turn = not turn

print(player1, player2)
