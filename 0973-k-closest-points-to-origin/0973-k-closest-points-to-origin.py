class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        output = []
        
        for index, value in enumerate(points):
            x = value[0]
            y = value[1]
            distance = sqrt(x * x + y * y)
            heap.append((-distance, index))
        
        heapify(heap)
        
        remove = len(points) - k
        while remove:
            heappop(heap)
            remove -= 1
        
        while heap:
            index = heappop(heap)[1]
            val = points[index]
            output.append(val)
        
        return output
        
            