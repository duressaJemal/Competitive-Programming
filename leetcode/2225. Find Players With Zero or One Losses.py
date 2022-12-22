# Link: https://leetcode.com/problems/find-players-with-zero-or-one-losses/
#Q: 2225. Find Players With Zero or One Losses

# Time: O(Nlog(N))
# Space: O(N)

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        lost = defaultdict(int)
        for match in matches:
            lost[match[1]] += 1
        
        winers, lost_one = set(), set()
        
        for match in matches:
            if match[0] not in lost:
                winers.add(match[0])
            
            if lost[match[1]] == 1:
                lost_one.add(match[1])
            
        return [sorted(list(winers)), sorted(list(lost_one))]
        
                
