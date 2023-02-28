class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        hash_map = defaultdict(int)
        hash_map[0] = 1
        
        total_subarrays = 0
        current_sum = 0
        
        for value in nums:
            
            current_sum += value
            diff = current_sum % k
        
            total_subarrays += hash_map[diff]
            hash_map[diff] += 1
        
        return total_subarrays
                    
    
    
            
            
            