# Time: O(Nlog(N))
# space: O(1)

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        n = len(skill)
        skill.sort()
        
        prev = skill[0] + skill[-1]
        res = 0
        
        for index in range(n // 2):
            current = skill[index] + skill[n - (index + 1)]
            if current != prev:
                return -1
            else:
                res += (skill[index] * skill[n - (index + 1)])
        
        return res