class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        
        odds = 0
        res = 0
        
        hash_map = defaultdict(int)
        hash_map[0] = 1
        
        for right in range(n):
            
            if nums[right] % 2:
                odds += 1
            
            if odds >= k and odds - k in hash_map:
                res += hash_map[odds - k]
                
            hash_map[odds] += 1
        
        return res
                
            
            