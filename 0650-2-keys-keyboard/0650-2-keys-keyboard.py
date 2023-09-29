# Time: O(N^2)

class Solution:
    def minSteps(self, n: int) -> int:
        
        @cache
        def dp(num):
            if num == 1:
                return 0
            
            mn = float("inf")
            
            for i in range(1, num):
                if num % i == 0:
                    mn = min(mn, dp(i) + (num // i))
            
            return mn
        
        return dp(n)
    

# Time: O(N)

class Solution:
    def minSteps(self, n: int) -> int:
        
        @cache
        def dp(word_length, print_size):
            
            if word_length == n:
                return 0
            
            if word_length > n:
                return float("inf")
            
            # copy and print into notepad
            copy_and_print = 2 + dp(2 * word_length, word_length)
            
            # print into notepad
            if word_length > 1:
                print_into_notepad = 1 + dp(word_length + print_size, print_size)
            else:
                print_into_notepad = copy_and_print
            
            return min(print_into_notepad, copy_and_print)
        
        return dp(1, 1)
            
            
    


