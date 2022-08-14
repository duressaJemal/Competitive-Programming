# Link: https://codeforces.com/edu/course/2/lesson/6/2/practice/contest/283932/problem/D

m , n = map(int, input().split())
assistants = []

for _ in range(n):
    t, z, y = map(int, input().split())
    assistants.append((t, z, y)) # t, y, z

def count_ballons(max_time, t, z, y):

    batch_time = (z * t) + y
    batchs =  max_time // batch_time
    time_left = (max_time % batch_time) 

    total_ballon = 0
    total_ballon += (batchs * z)

    if time_left:
        if time_left // t >= z:
            total_ballon += z
        else:
            total_ballon += (time_left // t)

    return total_ballon


def is_possible_ballon(time, ballons, assistant):
    t = assistant[0]
    z = assistant[1]
    y = assistant[2]

    batch_time = (z * t) + y
    batchs = ballons//z
    value = ballons % z == 0
    total_time = 0

    if value:
        batchs -= 1
        total_time = (batch_time * batchs) + (z * t)
    else:
        total_time = (batch_time * batchs) + ((ballons % z) * t)

    return total_time <= time



def is_possible(time):
    total_ballon = 0
    for assistant in assistants:
        left = 0 # first good value
        right = 10**9 
        while right > left + 1:
            mid = (left + right) // 2
            if is_possible_ballon(time, mid, assistant):
                left = mid
            else:
                right = mid
        total_ballon += left

    return total_ballon >= m
        

min_time = -1 # first bad value
max_time = 3 * 10**7 # frist good value

while max_time > min_time + 1:
    mid = (min_time + max_time) // 2
    if is_possible(mid):
        max_time = mid
    else:
        min_time = mid

print(max_time)
n = len(assistants)

count = [0] * n

for i in range(n):

    t = assistants[i][0]
    z = assistants[i][1]
    y = assistants[i][2]

    count[i] = count_ballons(max_time, t, z, y)

total_ballons = 0
for i in range(n):
    if total_ballons + count[i] <= m:
        print(count[i], end = " ")
        total_ballons += count[i]
    else:
        if total_ballons == m:
            print(0, end = " ")
        else:
            print(m - total_ballons, end = " ")
            total_ballons = m




