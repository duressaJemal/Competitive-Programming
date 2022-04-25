class Solution:
    def hIndex(self, citations: List[int]) -> int:
    
        output = []
        citations.sort()
        
        for i in range(len(citations)):
            output.append(min(citations[i], len(citations) - i))
            
        return max(output)
