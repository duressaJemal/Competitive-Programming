# Link: https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=false
#Q: Lists

if __name__ == '__main__':
    N = int(input())
    commands = []
    original = []
    for _ in range(N):
        commands.append(input().split())
    
    commandDict = {
        'insert': lambda x , y : original.insert(x, y),
        'print' : lambda : print(original),
        'remove' : lambda x : original.remove(x),
        'append' : lambda x : original.append(x),
        'pop' : lambda : original.pop(),
        'reverse': lambda : original.reverse(),
        'sort' : lambda : original.sort()
        }
    
    for command in commands:
        if len(command) == 1:
            commandDict[command[0]]()
        elif len(command) == 2:
            commandDict[command[0]](int(command[1]))
        else:
            commandDict[command[0]](int(command[1]), int(command[2]))
