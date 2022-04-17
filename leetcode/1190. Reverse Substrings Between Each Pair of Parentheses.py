class Solution:
    def reverseParentheses(self, s: str) -> str:
    
        arr = list(s)
        openning = []
        output = 
        
        def reverse(arr, start, end):
            while( start < end):
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        for i in range(len(arr)):
            if arr[i] == "(":
                openning.append(i)
                
            if arr[i] == ")":
                reverse(arr, openning[-1], i)
                openning.pop()

        for i in range(len(arr)):
            if arr[i] != ")" and arr[i] != "(":
                output.append(arr[i])
                
        return "".join(output)
