class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        
        # check for equal length
        if len(s) != len(goal): return False
        
        # check for character similarity in both sets
        if Counter(s) != Counter(goal): return False
        
        # count their difference
        diff = 0
        
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff += 1
        
        print(diff)
        # if they have 0 diff
        if not diff:
            counter = Counter(s)
            for key in counter:
                if counter[key] > 1:
                    return True

        # if they have 2 difference
        if diff == 2:
            return True
        else:
            return False
        
        