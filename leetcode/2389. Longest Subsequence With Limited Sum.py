# Link: https://leetcode.com/problems/longest-subsequence-with-limited-sum/
#Q: 2389. Longest Subsequence With Limited Sum

# Time: (M*N + Nlog(N))
# Space: O(M + N)

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        ans = [0] * len(queries)
        nums.sort()
        for l_n in range(1, len(nums)):
            nums[l_n] += nums[l_n - 1]
        
        for l_q in range(len(queries)):
            for l_n in range(len(nums)):
                if nums[l_n] <= queries[l_q]:
                    ans[l_q] = l_n + 1
        return ans
        
    
# Time: O(M*log(N) + Nlog(N))
# Space: O(M + N)

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        ans = [0] * len(queries)
        nums.sort()
        for l_n in range(1, len(nums)):
            nums[l_n] += nums[l_n - 1]
        
        for l_q in range(len(queries)):
            # binary search
            l = -1
            r = len(nums) # assume good value
            
            while r > l + 1:
                mid = (l + r) // 2
                if nums[mid] > queries[l_q]:
                    r = mid
                else:
                    l = mid
                    
            ans[l_q] = r
        
        return ans
        
        
        
        
        
        
        
        
