/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
 /*
 URL := https://leetcode.com/problems/surrounded-regions/description/
 130. Surrounded Regions

 The 750th LC problem to solve WOOOOOHHH :-) !!!
 Visited set -> for performancy ( would have geussed ) 

 */
var solve = function(board) {
    fillExterior(board,"O","P")
    fillInterior(board,"O","X")
    fillExterior(board,"P","O")
}

function fillInterior(board,curLet,nextLet){
    let m = board.length
    let n = board[0].length
    let visited = Array(m).fill(false).map(() => Array(n).fill(false))
    for(let r = 1; r < m-1; r++){
        for(let c = 1; c < n-1; c++){
            if (board[r][c] === curLet){
                fill(board,[r,c],curLet,nextLet,visited)
            }
        }
    }
}

function fillExterior(board,curLet,nextLet){
    let m = board.length
    let n = board[0].length
    let visited = Array(m).fill(false).map(() => Array(n).fill(false))
    for(let r = 0; r < m; r++){
        // c == 0 or c == n-1
        if (board[r][0] === curLet){
            fill(board,[r,0],curLet,nextLet,visited)
        }
        if (board[r][n-1] === curLet){
            fill(board,[r,n-1],curLet,nextLet,visited)
        }
    }
    for(let c = 0; c < n; c++){
        // r == 0 or r == m-1
        if (board[0][c] === curLet){
            fill(board,[0,c],curLet,nextLet,visited)
        }
        if (board[m-1][c] === curLet){
            fill(board,[m-1,c],curLet,nextLet,visited)
        }
    }
}

// Iterative solution less parameter passing too :-)
// Also can be less code in potential too
function fill(board,rootCell,curLetter,nextLetter,visited){
    let dirs = [
        [-1,0],
        [0,-1],
        [1,0],
        [0,1]
    ]
    let queue = []
    queue.push(rootCell)
    while(queue.length > 0){
        cell = queue.shift() // in-place modification
        if(!visited[cell[0]][cell[1]]){
            visited[cell[0]][cell[1]] = true
            board[cell[0]][cell[1]] = nextLetter
            dirs.forEach((dir) => {
                let next = [cell[0] + dir[0], cell[1] + dir[1]]
                // Avoid nested conditionals -> use boolean short-circuiting :-)
                if(isInBounds(board,next) && board[next[0]][next[1]] === curLetter){
                    queue.push(next)
                }
            })
        }
    }
}

// Overloading : extends to both cell array and each position by itself
// The latter method is more preferable on dimensionality exploding too :-)
// And can extend to be variadic as well
function isInBounds(board,cell){
    let m = board.length
    let n = board[0].length
    let x = cell[0]
    let y = cell[1]
    return (0 <= x && x < m) && (0 <= y && y < n)
}
