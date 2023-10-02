class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        a_count = 0
        b_count = 0
        
        for index in range(1, len(colors) - 1):
            
            # for alice
            if colors[index] == "A" and colors[index - 1] == "A" and colors[index + 1] == "A":
                a_count += 1
                
            if colors[index] == "B" and colors[index - 1] == "B" and colors[index + 1] == "B":
                b_count += 1
        
        if a_count > b_count:
            return True
        else:
            return False
                
        