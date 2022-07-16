# link: https://leetcode.com/problems/find-the-winner-of-the-circular-game/submissions/

# Iterative

# time: O(n)
# space: O(n)

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        players = list(range(1, n + 1))
        index = 0
        
        while len(players) > 1:
            
            index = (index + k - 1) % len(players)
            players.pop(index)
            index = index % len(players)
        
        return players[0]
        
    
# Recursive

# time: O(n^2)
# space: O(n^2)

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        def jump(n, k, starting_index):
        
            if len(n) == 1:
                return n[0]
            
            remove = (starting_index + k - 1) % len(n) 
            n.pop(remove) # is costy
            remove = remove % len(n)
            return jump(n, k, remove)
        
        return jump(list(range(1, n + 1)), k, 0)
            
