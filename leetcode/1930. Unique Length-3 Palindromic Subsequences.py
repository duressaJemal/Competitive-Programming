# Link: https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
#Q: 1930. Unique Length-3 Palindromic Subsequences

# Time: O(N*26) == O(N)
# Space: O(N)

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        n = len(s)
        prefix = [[0 for _ in range(26)] for _ in range(n)]
        prefix[0][ord(s[0]) - ord("a")] = 1
        
        # build 2D prefix
        for i in range(1, n):
            current = prefix[i - 1].copy()
            current[ord(s[i]) - ord("a")] += 1
            prefix[i] = current.copy()

        # count the start and end index for each character
        range_list = defaultdict(list)
        for index, value in enumerate(s):
            if not range_list[value]:
                range_list[value] = [index, index]
            else:
                range_list[value][1] = index
        
        count = 0
        # iterate over each char of the string
        for key in range_list:
            left_index = range_list[key][0]
            right_index = range_list[key][1]
            
            if right_index > left_index + 1:
                for i in range(26):
                    unique = prefix[right_index - 1][i] - prefix[left_index][i]
                    if unique:
                        count += 1
        return count
            
            
            
                                                           
                
                
            
