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
 * @return {TreeNode[]}
 */
 /*
 URL := https://leetcode.com/problems/find-duplicate-subtrees/description/
 652. Find Duplicate Subtrees
 Can we also minimize for duplicate work executed here?
 Question of possible TLE now -> it is correct though

 The other idea -> create encodes for the trees in a bottom-up manner instead


 4-2-4-3-1-2-1 type of thinking ( but this is a SLL )
 some type of unique identifying code ( serialization/deserialization ) ?
 Still need DFS/HASHMAP -> but is more efficient at least
 
 Woah serialization deserialization way faster

 */

var findDuplicateSubtrees = function(root) {
    let duplSubtrees = new Set()
    let treeCodeMap = new Map()
    getCodes(root, treeCodeMap)
    // need destructuring here still ( or use an array to avoid it )
    // Avoid destructuring work via arrays ( versus sets ) 
    treeCodeMap.forEach((treeList,code) => {
        if(treeList.length >= 2){
            duplSubtrees.add(treeList[0])
        }
    })
    // https://stackoverflow.com/questions/20069828/how-to-convert-set-to-array
    return Array.from(duplSubtrees)
};

// Can be same delimieter too :-)
function getCodes(root, codeMap){
    let curCode = ""
    if(root !== null){
        curCode += root.val
        leftCode = getCodes(root.left, codeMap)
        curCode += "(" + leftCode + ")"
        rightCode = getCodes(root.right, codeMap)
        curCode += "(" + rightCode + ")"
        if(!codeMap.has(curCode)){
            codeMap.set(curCode,[])
        }
        codeMap.get(curCode).push(root)
    } 
    return curCode
}

// var findDuplicateSubtrees = function(root) {
//     let duplSubtrees = new Set()
//     let myNodes = []
//     getNodes(root, myNodes)
//     let visited = new Set()
//     let n = myNodes.length
//     for(let i = 0; i < n; i++){
//         let nodeOne = myNodes[i]
//         if(!visited.has(nodeOne)){
//             let firstIso = false
//             for(let j = i+1; j < n; j++){
//                 let nodeTwo = myNodes[j]
//                 if(areIsomorphicTrees(nodeOne,nodeTwo)){
//                     // the root of one of them only -> not more then one ( structure can differ -> but test be a test)
//                     if(!firstIso && !visited.has(nodeOne)){
//                         firstIso = true
//                         duplSubtrees.add(nodeOne)
//                     }
//                     visited.add(nodeTwo) // NOP and skip for other trees told to be isomorphic
//                 }
//             }
//             visited.add(nodeOne) // add original iso tree later
//         }
//     }
//     // https://stackoverflow.com/questions/20069828/how-to-convert-set-to-array
//     return Array.from(duplSubtrees)
// };

// function getNodes(root, myNodes){
//     if(root !== null){
//         myNodes.push(root)
//         getNodes(root.left, myNodes)
//         getNodes(root.right, myNodes)
//     }
// }

function areIsomorphicTrees(rootOne, rootTwo){
    let isIso = false
    // https://stackoverflow.com/questions/6003884/how-do-i-check-for-null-values-in-javascript
    // test only for null via `===`
    if(rootOne === null && rootTwo === null){
        isIso = true
    } else if(rootOne !== null && rootTwo !== null){
        if(rootOne.val === rootTwo.val) {
            isIso = true
            // Liking operator overloading here
            isIso &= areIsomorphicTrees(rootOne.left,rootTwo.left)
            isIso &= areIsomorphicTrees(rootOne.right,rootTwo.right)
        }
    }
    return isIso
}
