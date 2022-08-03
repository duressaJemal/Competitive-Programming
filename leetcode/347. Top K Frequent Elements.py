# Link: https://leetcode.com/problems/top-k-frequent-elements/submissions/

# Heap

# Time: O(N + Klog(N))
# Space: O(N)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        output, heap = [], []
        counter = collections.Counter(nums)
        
        heap = [(-value, key) for key, value in counter.items()]
        heapify(heap)
        
        while k:
            
            output.append(heappop(heap)[1])
            k -= 1
        
        return output
            
# Sorting

# Time: O(Nlog(N))
# Space: O(N)

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
            
