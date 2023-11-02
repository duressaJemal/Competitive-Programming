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
    
        
    const counter = new Map();
    const arr = [];
    const output = [];
    
    function help(root){
        if (root == null){
            return
        }
        
        val = root.val
        counter.set(val, (counter.get(val) || 0) + 1)
        help(root.left)
        help(root.right)
        
        return;
        
    }
    
    help(root);

    let mx = 0;
    counter.forEach(value => {
        mx = Math.max(value, mx)
    })
    
    counter.forEach((value, key) => {
        if (value == mx){
            output.push(key)
        }
    })
    
    return output

};






























