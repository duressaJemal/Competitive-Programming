/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var findMode = function(root) {
    
    const arr = [];
    const output = [];
    
    function help(root){
        if (root == null){
            return;
        }
        
        arr.push(root.val);
        help(root.left)
        help(root.right)
        
        return;
        
    }
    
    help(root);
    
    const counter = {};
    let mx = 0;
    
    for (let i = 0; i < arr.length; i ++){
        const val = arr[i]
        counter[val] = (counter[val] || 0) + 1;
        mx = Math.max(mx, counter[val]);
    }
    
    const keys = Object.keys(counter);
    keys.forEach((key) => {
      if (counter[key] === mx) {
        output.push(Number(key));
      }
    });
    
    return output


    
    
};


// class Solution:
//     def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
//         arr = []
//         output = []
        
//         def help(root):
            
//             if not root:
//                 return 

//             arr.append(root.val)
//             help(root.left)
//             help(root.right)
            
//             return 
        
//         help(root)
//         counter = Counter(arr)
//         mx = 0
        
//         for val in counter.values():
//             mx = max(mx, val)
        
//         for key in counter:
//             if counter[key] == mx:
//                 output.append(key)
        
//         return output