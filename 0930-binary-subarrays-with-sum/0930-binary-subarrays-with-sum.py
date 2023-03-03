class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        hash_map = defaultdict(int)
        hash_map[0] = 1
        
        current_sum = 0
        total_count = 0
        
        for val in nums:
            
            current_sum += val
            segment = current_sum - goal
            
            if segment in hash_map:
                total_count += hash_map[segment]
            
            hash_map[current_sum] += 1
            
        
        return total_count
                
            
            