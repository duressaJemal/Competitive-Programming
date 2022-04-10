def countingValleys(steps, path):
    # Write your code here
    counter = 0
    valleys = 0
    for i in range(steps):
        if path[i] == 'U':
            counter += 1
            if counter == 0:
                valleys += 1
        else:
            counter -= 1
    return valleys
