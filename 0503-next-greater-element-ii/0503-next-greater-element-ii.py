# Time: O(N)
# Space: O(N)

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        
        result = [-1] * (n)
        greater = []
        hash_map = defaultdict(lambda : -1)
        
        
        for index in range(2 * n):
            
            current_index = index % n
            value = nums[current_index]
            
            while greater and value > greater[-1][1]:
                hash_map[greater.pop()[0]] = value
            
            greater.append((current_index, value))
        
        
        for key in hash_map:
            result[key] = hash_map[key]
        
        return result
            
            
            
            
        
        
    