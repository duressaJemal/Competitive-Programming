class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        w_len = len(words)
        q_len = len(queries)
        
        output = []
        
        def counter(string):
            count = Counter(string)
            
            ofset = ord("a")
            for index in range(26):
                curr = chr(ofset + index)
                
                if curr in count:
                    return count[curr]
        
        for index in range(w_len):
            words[index] = counter(words[index])
            
        words.sort()
    
        for index in range(q_len):
            queries[index] = counter(queries[index])
        
        for val in queries:
            output.append(w_len - bisect_right(words, val))
        
        return output
        
            
        
        
        
        