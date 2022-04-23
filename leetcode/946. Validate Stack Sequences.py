class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        pushed_pointer = 0
        popped_pointer = 0
        
        while popped_pointer < len(popped):
            
            if popped[popped_pointer] == pushed[pushed_pointer]:
                pushed.pop(pushed_pointer)
                
                # for preventing negative value assignment for index
                if pushed_pointer == 0 and len(pushed) > 0:
                    popped_pointer += 1
                    continue
                    
                pushed_pointer -= 1
                popped_pointer += 1
                continue
                
            if pushed_pointer == len(pushed) - 1:
                return False
            
            pushed_pointer += 1 
            
        return True
