/**
 * @param {number} width
 * @param {number} height
 * @param {number[][]} food
 */
/*
353. Design Snake Game
Url := https://leetcode.com/problems/design-snake-game/description/
Snake is a ubiquitous game : please solution the problem!
Gotta program future food appearances.

Intuition :
Category : Queues, Two Pointers, Sliding Windows, Singly Linked Lists, Matrix

Approach :
This is a design problem, so we need to think about LDD : Low-Level Design.
Return back to designing the snake game
This of setting up a grid whose cell statuses represent different states of a cell : snake, food, or unoccupied
Think of using a singly linked list to track all positions a snake has visited ( and thus, the fully snake itself )


Cell statuses :
-1 := unoccupied
0 := occupied
1 := food


Complexity :
Let M, N := grid(dims)
Time := O(X), X := #=moves, which is O(MN) since a snake can only grow as big as the containing device.
Space := O(MN) ( E ) ( matrix and snake ) ( Explicit )  O(1) ( Implicit ) ( iterative only )

Correct but hit javascriopt heap memory issues :-(
// we can't store an entire grid : just a hashmap ( minimize the footprint )
// works for smaller board cases :-)

*/
// no to matrix : must be hashmap ( for memory footprint efficiency )
// account for case of (starting) on food too!
var SnakeGame = function(width, height, food) {
    this.food = food
    this.width = width
    this.height = height
    this.curFood = food[0]
    this.foodPtr = 0
    this.matrix = new Map()
    this.matrix[0] = new Map()
    this.matrix[0][0] = -1
    curR = this.curFood[0]
    curC = this.curFood[1]
    this.matrix[curR][curC] = 1
    this.size = 1
    // snake as a list of coordinates 
    this.snake = []
    this.snake.push([0,0])
    this.matrix[0][0] = 0
    this.score = 0
    this.numMoves = 1
    // this may or may not execute : take note later please
    if(this.food !== undefined){
        nextHeadCell = [0,0]
        growthStatus = this.growTheSnake(nextHeadCell)
        if(growthStatus){
            curMoveScore += 1
            nextHeadCell = this.getNextHeadCell(nextHeadCell,direction)
            this.snake.unshift(nextHeadCell)
            nextR = nextHeadCell[0]
            nextC = nextHeadCell[1]
            this.matrix[nextR][nextC] = 0
        }
    }
};

/** 
 * @param {string} direction
 * @return {number}
 */
 
// Grow the snake, but if growth hits itself -> end game as well
// preserve the last cell ( if we grow the snake ) versus moving -> accounts for directionality
// Minimization of loops -> code performancy!
// Log number of moves played ( downstream game analysis )!
SnakeGame.prototype.move = function(direction) {
    this.numMoves += 1
    // when head is at food, we grow the snake
    curMoveScore = this.score
    curHeadCell = this.snake[0]
    nextHeadCell = [curHeadCell[0], curHeadCell[1]]
    nextHeadCell = this.getNextHeadCell(nextHeadCell,direction)
    nextR = nextHeadCell[0]
    nextC = nextHeadCell[1]
    // hit snake : only after you unshift the cell should we test it too
    if(!this.isInBounds(nextHeadCell)){
        // game over : return -1 ( both head occupies body OR out of bounds wall hit! )
        console.log("OOB")
        return -1
    } else {
        this.snake.unshift(nextHeadCell)
        growthStatus = false
        if(this.food !== undefined){
            growthStatus = this.growTheSnake(nextHeadCell)
            if(!growthStatus){
                // if it did not grow
                lastSnakeCell = this.snake.pop()
                lastR = lastSnakeCell[0]
                lastC = lastSnakeCell[1]
                this.matrix[lastR][lastC] = -1
            }
        }
        // check if snake hit itself
        if(this.hitSnake(nextHeadCell)){
            console.log("Hit self")
            return -1
        }
        if(!this.matrix.has(nextR)){
            this.matrix[nextR] = new Map()
            if(!this.matrix[nextR].has(nextC)){
                this.matrix[nextR][nextC] = 0
            }
        }
        this.matrix[nextR][nextC] = 0
        if(growthStatus){
            this.score = this.score + 1
            curMoveScore = this.score
        }
    }
    // console.log(this.snake)
    return curMoveScore
};

SnakeGame.prototype.hitSnake = function(curCell) {
    curR = curCell[0]
    curC = curCell[1]
    cellStatus = this.matrix[curR][curC]
    hitSelfStatus = (this.snake.length > 4 && cellStatus == 0)
    return hitSelfStatus
}

// name = function(parameters)
SnakeGame.prototype.getNextHeadCell = function(curHeadCell,direction){
    nextHeadCell = curHeadCell
    // console.log(direction)
    // console.log("Before application, cell = " + nextHeadCell)
    switch(direction) {
        case 'L':
            nextHeadCell[1] -= 1
            break
        case 'U':
            nextHeadCell[0] -= 1
            break
        case 'R':
            nextHeadCell[1]  += 1
            break
        case 'D':
            nextHeadCell[0] += 1
            break
    }
    // console.log("After application, cell = " + nextHeadCell)
    return nextHeadCell
}

SnakeGame.prototype.growTheSnake = function(headCell) {
    growStatus = false
    if(this.food !== undefined && this.food.length > 0 && this.foodPtr < this.food.length){
        firstR = headCell[0]
        firstC = headCell[1]
        this.curFood = this.food[this.foodPtr]
        if(firstR === this.curFood[0] && firstC === this.curFood[1]){
            this.size += 1
            this.foodPtr = this.foodPtr + 1
            growStatus = true
        }
    }
    return growStatus
}

SnakeGame.prototype.isInBounds = function(cell) {
    r = cell[0]
    c = cell[1]
    return ((0 <= r && r < this.width) && (0 <= c && c < this.height))
}

/** 
 * Your SnakeGame object will be instantiated and called as such:
 * var obj = new SnakeGame(width, height, food)
 * var param_1 = obj.move(direction)
 */
