class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        word_length = len(s)
        dict_length = len(dictionary)
        
        memo = {}
        
        @lru_cache()
        def dp(cur_index):
            
            # base case
            if cur_index == word_length:
                return 0
            
            mn = float("inf")
            
            for i in range(dict_length):
                jump = cur_index + len(dictionary[i])
                if s[cur_index : jump] == dictionary[i]:
                    mn = min(mn, dp(jump))
                    
            
            # if didn't choose any of them
            mn = min(mn, 1 + dp(cur_index + 1))
            memo[cur_index] = mn
    
            return memo[cur_index]
        
        return dp(0)
            
            
                    
        