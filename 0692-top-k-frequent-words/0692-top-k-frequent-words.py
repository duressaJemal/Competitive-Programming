class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        heap = []
        output = []
        result = []

        counter = Counter(words)

        for key in counter:
            heap.append((-counter[key], key))

        heapify(heap)

        while k:
            output.append(heappop(heap))
            k -= 1

        output.sort()
        for freq, val in output:
            result.append(val)
        
        return result

