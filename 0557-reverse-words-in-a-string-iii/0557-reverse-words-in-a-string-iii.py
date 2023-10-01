class Solution:
    def reverseWords(self, s: str) -> str:
        
        output = []
        temp = ""
        
        for char in s:

            if char == " ":
                output.append(temp[::-1] + " ")
                temp = ""
            else:
                temp += char
        
        output.append(temp[::-1])
        return "".join(output)
                