
# Link: https://leetcode.com/problems/even-odd-tree/
#Q: 1609. Even Odd Tree

# Time: O(N)
# Space: O(N)

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        queue = deque([root])
        level = -1
        while queue:
            n, store = len(queue), []
            level += 1
            for i in range(n):
                root = queue.popleft()
                store.append(root.val)
                
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
                
            # check all conditions
            if level % 2 == 0:
                comp = 0
                for i in range(len(store)):
                    if store[i] % 2 == 0 or store[i] <= comp:
                        return False
                    comp = store[i] 
            else:
                comp = float("inf")
                for i in range(len(store)):
                    if store[i] % 2 != 0 or store[i] >= comp:
                        return False
                    comp = store[i]
        return True
                
            
                
                
                
        
