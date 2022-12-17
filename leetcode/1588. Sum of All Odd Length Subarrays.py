# Link: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
#Q: 1588. Sum of All Odd Length Subarrays

# Time: O(N^2)
# Space: O(N)

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        prefix = [0] * (n + 1)
        
        # Build prefix
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + arr[i - 1]
        
        total = 0
        for i in range(1, n + 1, 2):
            l, r = 0, i
            while r <= n:
                total += (prefix[r] - prefix[l])
                l += 1
                r += 1
                
        return total

# Time: O(N^2)
# Space: O(1)

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        n = len(arr)
        output = 0
        
        for l in range(n):
            current = 0
            for r in range(l, n):
                current += arr[r]
                if (r - l) % 2 == 0:
                    output += current
        return output


        
         
        
# Optimized

# time:
# space:
