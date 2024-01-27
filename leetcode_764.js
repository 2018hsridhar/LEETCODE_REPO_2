/**
 * @param {number} n
 * @param {number[][]} mines
 * @return {number}
 */
 /*
 URL := https://leetcode.com/problems/largest-plus-sign/description/
 764. Largest Plus Sign

It's a prefix-sum, minimization problem in the hiding.
Akin to minesweeper games
Axis-alignment 1's in the grid 

Probably efficienc enough to set up the grid anways

 */
var orderOfLargestPlusSign = function(n, mines) {
    let largestOrder = 0
    let grid = fillGrid(n,1)
    mines.forEach((mine) => {
        grid[mine[0]][mine[1]] = 0
    })
    let leftSums = fillGrid(n,0)
    let rightSums = fillGrid(n,0)
    let topSums = fillGrid(n,0)
    let bottomSums = fillGrid(n,0)
    // Solve left and right
    for(let r = 0; r < n; r++){
        let rSum = 0
        let lSum = 0
        for(let c = 0; c < n; c++){
            rSum = (grid[r][c] == 1) ? rSum + 1 : 0
            leftSums[r][c] = rSum
        }
        for(let c = n-1; c >= 0; c--){
            lSum = (grid[r][c] == 1) ? lSum + 1 : 0
            rightSums[r][c] = lSum
        }
    }
    // solve top
    // Solve bottom
    for(let c = 0; c < n; c++){
        let tSum = 0
        let bSum = 0
        for(let r = 0; r < n; r++){
            tSum = (grid[r][c] == 1) ? tSum + 1 : 0
            topSums[r][c] = tSum
        }
        for(let r = n-1; r >= 0; r--){
            bSum = (grid[r][c] == 1) ? bSum + 1 : 0
            bottomSums[r][c] = bSum
        }
    }
    // And actual signs
    for(let r = 0; r < n; r++){
        for(let c = 0; c < n; c++){
            // Your 0 case is a NOP :-)
            // https://www.geeksforgeeks.org/javascript-math-min-method/?ref=lbp
            // Static => dodge Object creation :-) for invocation of methods
            // inclusive '1' writing for ease here : also makes sense
            largestOrder = Math.max(largestOrder, Math.min(leftSums[r][c],rightSums[r][c],topSums[r][c],bottomSums[r][c]))
        }
    }
    return largestOrder
};

function fillGrid(n,val){
    // Liking JS method chaining -> nest down functinos well
    // Array(x) => allow x space but fill(y) => set value of alloc spaces
    let grid = Array(n).fill(val).map(() => Array(n).fill(val))
    return grid 
}
