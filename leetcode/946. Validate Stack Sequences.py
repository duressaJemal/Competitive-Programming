# link: https://leetcode.com/problems/validate-stack-sequences/submissions/

# time: O(n)
# space: O(n)

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        n = len(popped)
        stack = []
        pop_index = 0
        
        for push_element in pushed:
            
            stack.append(push_element)
            while stack and pop_index < n and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1
            
        return pop_index == n
            
            
