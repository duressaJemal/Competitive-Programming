# for finding the largest segment less than or equal to target.
a = "list"
s = "target"
longest = 0

x, l = 0, 0
for r in range(len(a)):
    x += a[r]
    while x > s:
        x -= a[l]
        l += 1
    
    longest = max(longest, r - l + 1)


# for finding the smallest segment greater than or equal to target

shortest = "some large value"

x, l = 0, 0
for r in range(len(a)):
    x += a[r]
    while x - a[l] >= s: # can we shorten the window size with out lossing the validity?
        x -= a[l]
        l += 1
    
    if x >= s: # since the whole sum can be less than target.
        shortest = min(shortest, r - l + 1)


# to find the number of segments, the sum of elements does not exceed target

res = "number of segments"

x, l = 0, 0
for r in range(len(a)):
    x += a[r]
    while x > s:
        x - a[l]
        l += 1
    
    res += r - l + 1 # since there are this amount of segments that are less than target that end at right boundary
    # invalid....l........r all the segments between [l, r] are valid and are r - l + 1 in numbers
    

# general approach
"""
for r in range(n):
    add(a[r]) #1
    while not good(): #2
        remove(a[l]) #3
        l+=1

"""


# find the maximum length, with no more than k different numbers(type of problems)

k = "max different numbers expected in the any interval"
counter = "how many times each number occur in the given [L, R] segment"
number = "how many distinct numbers on the segment [L, R]"

def good():
    return number <= k

def add(x): # x: the number to be added
    counter[x] += 1
    if counter[x] == 1: # since this only happens when a number appears for the first time in the given segment
        number += 1

def remove():
    counter[x] -= 1
    if counter[x] == 0: # since this only happens when a given number disappears from the given segment
        number -= 1

# then do the usual
"""
for r in range(n):
    add(a[r])
    while not good():
        remove(a[l])
        l+=1
    res = max(res, r - l + 1)
"""


    

    

