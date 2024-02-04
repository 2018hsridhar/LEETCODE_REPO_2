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
 * @param {number} k
 * @return {number}
 */
 /*
 URl := https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/description/
 2583. Kth Largest Sum in a Binary Tree

 Classic level sum explore and expand the frontier of nodes problem
 Can we do iterative vs recursive level sum ( with level tracking )? No need for hashmap -> readjust the sum if the next 
 node has a different level to 0, and then add back again

 No good priority queue notion in javascript gaaaah but good notion of sort() and slice()

 */

// Wrapper objects rapid to create in javascript :-)
var wrapper = function(root,lvl) {
    this.root = root
    this.lvl = lvl
}

/// Woooh iterative level order traversal without a hashmap 
// Note to self : javascript arrays are not multiple type -> they are single type only!!
var kthLargestLevelSum = function(root, k) {
    // Can arays be dynamic ( or not ) 
    let frontier = [new wrapper(root,0)]
    let levelSum = 0
    let levelSums = []
    let curLevel = -1
    while(frontier.length > 0){
        let curNode = frontier.shift()
        let curNodeLevel = curNode.lvl
        if(curNodeLevel !== curLevel){ // just hit another level -> reset here
            if(curLevel != -1) {
                levelSums.push(levelSum)
            }
            levelSum = 0
            curLevel = curNodeLevel
        }
        levelSum += curNode.root.val
        if(curNode.root.left !== null){
            frontier.push( new wrapper(curNode.root.left,curNodeLevel+1))
        }
        if(curNode.root.right !== null){
            frontier.push( new wrapper(curNode.root.right,curNodeLevel+1))
        }
    }
    levelSums.push(levelSum) // the last level to push out ( do not forgot it ) 
    kthLargestLevels = levelSums.sort((a,b) => { return Number(b) - Number(a)}).slice(0,k)
    return (kthLargestLevels.length === k) ? kthLargestLevels[k - 1] : -1
};
