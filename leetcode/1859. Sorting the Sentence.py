class Solution:
    def sortSentence(self, s: str) -> str:
        container = []
        container = s.split()
        holder = [0] * 10
        output = ""
        
        for i in range(len(container)):
            min = int((container[i][-1]))
            holder[min] = container[i][:-1]
        
        for i in range(len(holder)):
            if holder[i] != 0:
                if len(output) == 0: 
                    output =  output + holder[i]
                    
                else:
                    output = output + " " + holder[i]
                
        return output
        
