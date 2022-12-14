# Link: https://leetcode.com/problems/distribute-coins-in-binary-tree/
#Q: 979. Distribute Coins in Binary Tree

# Time: O(N)
# Space: O(H)

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        self.moves = 0
        def dfs(root):
            if not root: return 0
            left, right = dfs(root.left), dfs(root.right)
            self.moves += abs(left) + abs(right)
            
            return root.val + left + right - 1
        
        dfs(root)
        return self.moves

# Time: O(N^2)
# Space: O(N)

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        
        self.moves = 0
        
        def dfs(root):
            if not root: return (0, 0)
            l_nodes, l_coins = dfs(root.left)
            r_nodes, r_coins = dfs(root.right)
            
            total_coins = root.val + l_coins + r_coins
            total_nodes = l_nodes + r_nodes + 1
            
            # case 1
            if total_coins < total_nodes:
                root.val = total_coins
                return (total_nodes - total_coins, 0)
            
            # case 2:
            if total_coins == total_nodes:
                root.val = total_coins
                distribute(root, 0)
                return (0, 0)
            
            # case 3:
            if total_coins > total_nodes:
                surplus_coin = total_coins - total_nodes
                self.moves += surplus_coin
                root.val = total_nodes
                distribute(root, 0)
                return (0, surplus_coin)
            
        def distribute(root, coins):

            root.val += coins
            
            l_count = count(root.left)
            r_count = count(root.right)

            self.moves += (l_count + r_count)
            if root.left:
                distribute(root.left, l_count)
            if root.right:
                distribute(root.right, r_count)
            
            root.val -= (l_count + r_count)
            
            
        def count(root):
            if not root: return 0
            left = count(root.left)
            right = count(root.right)
            
            current = left + right + 1
            return current + (0 if root.val == 0 else -root.val) 
        
            
        dfs(root)
        return self.moves
    
