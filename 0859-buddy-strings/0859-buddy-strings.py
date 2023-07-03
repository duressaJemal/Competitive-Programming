class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        c_s = Counter(s)
        c_g = Counter(goal)
        
        if c_s != c_g:
            return False
        
        # count their difference
        diff = 0
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff += 1
        
        if not diff:
            for key in c_s:
                if c_s[key] > 1:
                    return True

        # if they have 2 difference
        if diff == 2:
            return True
        else:
            return False
        
        