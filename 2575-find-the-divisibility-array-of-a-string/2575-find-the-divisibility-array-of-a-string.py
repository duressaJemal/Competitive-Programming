# Time: O(N)


class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        
        gen = 0
        ans = []
        
        for num in word:
            gen = ((10 * gen) % m + int(num) % m) % m
            if gen % m == 0:
                ans.append(1)
            else:
                ans.append(0)
        
        return ans
    

