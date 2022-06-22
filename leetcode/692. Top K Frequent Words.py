# https://leetcode.com/problems/top-k-frequent-words/submissions/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        counter = collections.Counter(words)
        output = []
        
        heap = [(-value, key) for key, value in counter.items()]
        heapq.heapify(heap)
        
        while k:
            output.append(heapq.heappop(heap)[1])
            k -= 1
        
        return output
        
