/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number} n
 * @return {TreeNode[]}
 */
 /*
 URL := https://leetcode.com/problems/all-possible-full-binary-trees/description/
 894. All Possible Full Binary Trees

 Full binary tree invariant -> must meet n number of nodes exactly.
 All the same value.
 Trees in any order :-)

 Without the new keyword, the problem behavior is ... undefined??

 var lhs = function() {
     lhs() // without `this` still a valid call
 }

 */
var allPossibleFBT = function(n) {
    let fbtRoots = []
    if(n == 1) {
        fbtRoots.push(new TreeNode(0))
        return fbtRoots
    } 
    let remNodes = n - 1
    let lhsCard = 1
    while(remNodes - lhsCard > 0){
        allPossibleFBT(lhsCard).forEach((leftRoot) => {
            allPossibleFBT(remNodes - lhsCard).forEach((rightRoot) => {
                fbtRoots.push(new TreeNode(0, leftRoot, rightRoot))
            })
        })
        lhsCard += 2
    }
    return fbtRoots
}

