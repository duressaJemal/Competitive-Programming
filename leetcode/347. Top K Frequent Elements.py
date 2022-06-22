# https://leetcode.com/problems/top-k-frequent-elements/submissions/

import heapq

# heap

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        output, heap = [], []
        counter = collections.Counter(nums)
        
        heap = [(-value, key) for key, value in counter.items()]
        heapq.heapify(heap)
        
        while k:
            
            output.append(heapq.heappop(heap)[1])
            k -= 1
        
        return output
            
# sorting

class Solution:
    def topKFrequent(self, nums, k):

        d = {}
        output = []
        for i in nums:

            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        freqent = sorted(d.items(), key=lambda kv: (kv[1]), reverse=True)
        for i in range(k):
            output.append(freqent[i][0])

        return output
            
        
        
        
