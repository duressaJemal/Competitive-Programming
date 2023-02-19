a, b = map(int, input().split())
output = []

def dfs(x, path):

    if x > b: return
    current_path = path.copy()
    current_path.append(x)
    if x == b:
        output.append(current_path)
        return
    dfs(x * 2, current_path)
    dfs(10 * x + 1, current_path)

dfs(a, [])


if len(output):
    print("YES")
    print(len(output[0]))
    for i in range(len(output[0])):
        print(output[0][i], end = " ")
else:
    print("NO")
