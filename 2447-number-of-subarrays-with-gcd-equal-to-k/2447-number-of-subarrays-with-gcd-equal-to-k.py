# Time: O(N^2*log(K))
# Space: O(1)

class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        count = 0
        
        for i in range(n):
            cur = nums[i]
            for j in range(i, n):
                cur = gcd(cur, nums[j])
                if cur == k:
                    count += 1
        return count
                
        