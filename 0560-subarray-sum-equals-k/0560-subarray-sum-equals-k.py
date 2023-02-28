class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        
        hash_map = defaultdict(int)
        hash_map[0] = 1
        
        current_sum = 0
        total_subarrays = 0
        
        
        for value in nums:
            
            current_sum += value
        
            if current_sum - k in hash_map:
                total_subarrays += hash_map[current_sum - k]
                
            hash_map[current_sum] += 1
        
        return total_subarrays
        