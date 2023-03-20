def solve():

    wt, et, ef = map(int, input().split())
    minimum_cost = float("inf")

    for floor in range(5):

        initial = wt * floor
        call_cost = abs(ef - floor) * et
        elevetor_cost = (4 - floor) * et
        walking_cost = (4 - floor) * wt

        current_cost = initial + min(call_cost + elevetor_cost, walking_cost)
        minimum_cost = min(minimum_cost, current_cost)

    print(minimum_cost)
    return

t = int(input())
while t:
    solve()
    t -= 1