/**
 * // Definition for a QuadTree node.
 * function Node(val,isLeaf,topLeft,topRight,bottomLeft,bottomRight) {
 *    this.val = val;
 *    this.isLeaf = isLeaf;
 *    this.topLeft = topLeft;
 *    this.topRight = topRight;
 *    this.bottomLeft = bottomLeft;
 *    this.bottomRight = bottomRight;
 * };
 */

/**
 * @param {Node} quadTree1
 * @param {Node} quadTree2
 * @return {Node}
 */
/*
URL := https://leetcode.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/description/
558. Logical OR of Two Binary Grids Represented as Quad-Trees
Need to get properties from each node and make comparison operations
Build quad tree code in reality
n*n grid ( dim max 512 * 512 ) ( pow 9 )

Pass 60/61 test cases ( a one off error somewher )
Logical operations on a tree as not that non-trivial sadly :-(
*/

var intersect = function(quadTree1, quadTree2) {
    return solve(quadTree1,quadTree2)
}

// We need a way to do fast evaluations on Quad Tree
// Leverage logical OR : 1|0 = 1 and 1|1 = 1
function solve(quadTree1, quadTree2) {
    // work with the current roots of each tree in this case
    // evaluate root once the other levels have been evaluated too ( bottom-up parsing )
    let newQuadRoot = null
    // If either or is a leaf case
    if(quadTree1.isLeaf || quadTree2.isLeaf){
        if(quadTree1.isLeaf && quadTree2.isLeaf) {
            newQuadRoot = new Node(quadTree1.val || quadTree2.val, true,null,null,null,null)
        } else{
            if ( quadTree1.isLeaf && !quadTree2.isLeaf) {
                if(quadTree1.val) {
                    newQuadRoot = new Node(true,true, null,null,null,null)
                } else {
                    newQuadRoot = new Node(false,false,quadTree2.topLeft, quadTree2.topRight, quadTree2.bottomLeft, quadTree2.bottomRight) 
                }
            } else if ( quadTree2.isLeaf && !quadTree1.isLeaf) {
                if(quadTree2.val) {
                    newQuadRoot = new Node(true,true, null,null,null,null)
                } else {
                    newQuadRoot = new Node(false,false,quadTree1.topLeft, quadTree1.topRight, quadTree1.bottomLeft, quadTree1.bottomRight) 
                }
            }
        }
    } else { // if neither of them are leaves
        // console.log("Going down a level")
        // [1] Lower level evaluations first
        let newTopLeft = solve(quadTree1.topLeft,quadTree2.topLeft)
        let newTopRight = solve(quadTree1.topRight,quadTree2.topRight)
        let newBottomLeft = solve(quadTree1.bottomLeft,quadTree2.bottomLeft)
        let newBottomRight = solve(quadTree1.bottomRight,quadTree2.bottomRight)

        // [2] Root evaluations
        let rootLeaf = false
        let rootVal = false
        // If each node below is a leaf -> root itself is a leaf : nullify rest of nodes
        if(newTopLeft.isLeaf && newTopRight.isLeaf && newBottomLeft.isLeaf && newBottomRight.isLeaf){
            if(newTopLeft.val === newTopRight.val && newTopRight.val === newBottomLeft.val && newBottomLeft.val === newBottomRight.val) {
                rootLeaf = true
                rootVal = newTopLeft.val
                newQuadRoot = new Node(rootVal,rootLeaf,null,null,null,null)
            } else {
                newQuadRoot = new Node(rootVal,rootLeaf,newTopLeft,newTopRight,newBottomLeft,newBottomRight)
            }
        } else {
            newQuadRoot = new Node(rootVal,rootLeaf,newTopLeft,newTopRight,newBottomLeft,newBottomRight)
        }
    }
    return newQuadRoot
};



