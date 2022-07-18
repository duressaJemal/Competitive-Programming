# link: https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

# Naive

# time: O(n^3)
# space: O(n)

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        n = len(arr)
        SUM = 0
        
        for length in range(1, n + 1, 2):
            
            end = length
            start = 0

            while end <= n:
                SUM += sum(arr[start: end])
                start += 1
                end  += 1
            
        return SUM
                
                
                
# Prefix Sum

# time: O(n ^ 2)
# space: O(n)

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        n = len(arr)
        prefix = [0] * n
        prefix[0] = arr[0]
        
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + arr[i]
        
        answer = 0
        for i in range(n):
            end = i
            while end < n:
                if i == 0:
                    answer += prefix[end]
                else:
                    answer += prefix[end] - prefix[i - 1]
                
                end += 2
        
        return answer
         
        
# Optimized

# time:
# space:
