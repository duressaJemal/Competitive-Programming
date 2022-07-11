# https://leetcode.com/problems/top-k-frequent-words/submissions/

# time: O(n * log(k)) 
# space: O(n)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        counter = collections.Counter(words)
        output = []
        
        heap = [(-value, key) for key, value in counter.items()]
        heapify(heap)
        
        while k:
            output.append(heappop(heap)[1])
            k -= 1
        
        return output
        
        
# follow-up: why is it n not k
