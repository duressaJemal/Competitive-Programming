from heapq import *


n = int(input())
arr = []

for i in range(n):
    arr.append((input().split()))

output = []
heap = []
heapify(heap)


for row in arr:
    if row[0] == "insert":
        heappush(heap, int(row[1]))
        output.append("insert " + str(row[1]))

    elif row[0] == "removeMin":
        if not len(heap):
            heappush(heap, -10**9)
            output.append("insert " + str())
        else:
            heappop(heap)
            output.append("removeMin")
    elif row[0] == "getMin":
        if not heap:
            heappush(heap, int(row[1]))
            output.append("insert " + str(row[1]))
        elif heap[0] == int(row[1]):
            output.append("getMin " + str(heap[0]))

        elif heap[0] < int(row[1]):
            while heap[0] < int(row[1]):
                heappop(heap)
                output.append("removeMin")
                if not heap:
                    heappush(heap, int(row[1]))
                    output.append("insert " + str(row[1]))
            if heap[0] > int(row[1]):
                heappush(heap, int(row[1]))
                output.append("insert " + str(row[1]))
            else:
                output.append("getMin " + str(heap[0]))

        elif heap[0] > int(row[1]):
            heappush(heap, int(row[1]))
            output.append("insert " + str(row[1]))


print(len(output))
for i in range(len(output)):
    print(output[i])


