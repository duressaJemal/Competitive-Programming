class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        players.sort()
        trainers.sort()
        
        res = 0
        
        i_p = 0
        i_t = 0
        
        while i_p < len(players) and i_t < len(trainers):
            
            if players[i_p] <= trainers[i_t]:
                res += 1
                i_p += 1
                i_t += 1
            else:
                i_t += 1
            
        
        return res