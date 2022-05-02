class Solution:
    def compress(self, chars: List[str]) -> int:
        
        s = ""
        start = 0
        end = 0
        size = 0
        
        def helper(s, size):
            """
            concatenates single character if character i reaped only one time
            esle it concatenates character followed by number of apperance
            """
            
            if size == 1:
                s = s + str(chars[start])
                return s
            else:
                s = s + str(chars[start]) + str(size)
                return s
        
        while end < len(chars):
            
            if chars[end] == chars[start]: # window expanding condition
                end += 1
                size += 1
                
            else: # window shrinking condition
                s = helper(s, size)
                start = end
                size = 0
        
        
        s = helper(s, size)
        
        for i in range(len(s)): # modifiying input array char
            chars[i] = s[i]

        return len(s) 
