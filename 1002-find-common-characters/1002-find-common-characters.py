# Time: O(N), where N = total characters in the given list
# space: O(26) == O(1)

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        n = len(words)
        
        total_counter = [100] * 26
        output = []
        
        ofset = ord("a")
        
        for word in words:
            
            counter = [0] * 26
            for char in word:
                asci = ord(char)
                counter[asci - ofset] += 1
            
            for index, value in enumerate(counter):
                total_counter[index] = min(total_counter[index], value)
                
        for index, value in enumerate(total_counter):
            for i in range(value):
                output.append(chr(index + ofset))
        
        return output