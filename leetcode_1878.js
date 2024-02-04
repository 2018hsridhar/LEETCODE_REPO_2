/**
 * @param {number[][]} grid
 * @return {number[]}
 */
 /*

 */
var getBiggestThree = function(grid) {
    let rhombusVals = new Set()
    console.log(grid)
    for (let i = 0; i < grid.length; i++){
        for (let j = 0; j < grid[0].length; j++){
            // https://stackoverflow.com/questions/43455911/using-es6-spread-to-concat-multiple-arrays
            // rhombusVals.push(...cellRhombusVals)
            // .union limited availability
            // rhombusVals = rhombusVals.union(cellRhombusVals)
            solveRhombusVals(i,j,grid).forEach((cellRhombusVal) => {
                rhombusVals.add(cellRhombusVal)
            })
        }
    }
    // https://stackoverflow.com/questions/34883068/how-to-get-first-n-number-of-elements-from-an-array
    return Array
            .from(rhombusVals)
            .sort((a,b) => { return Number(b) - Number(a)})
            .slice(0,3)
};

function solveRhombusVals(i,j,grid){
    let rhombusVals = new Set()
    let delta = 0
    while(true){
        let top = [i,j]
        let bottom = [i+2*delta, j]
        let left = [i+delta, j - delta]
        let right = [i+delta, j+delta]
        let shapeCoords = [left, top, right, bottom]
        let dirs = [[-1,1],[1,1],[1,-1],[-1,-1]]
        if(coordsInBounds(shapeCoords,grid)){
            // let actualRhombusBorder = 0
            // for(let i = 0; i < 3; i++){
            //     actualRhombusBorder += getBorderSum(shapeCoords[i%4], shapeCoords[(i+1) % 4], dirs[i%4],grid)
            // }
            let rhombusSum = (delta === 0) ? grid[i][j] * 2 : 0
                + getBorderSum(left,top,[-1,1],grid)
                + getBorderSum(top,right,[1,1],grid)
                + getBorderSum(right,bottom,[1,-1],grid)
                + getBorderSum(bottom,left,[-1,-1],grid)
            let rhombusSumPoints = (delta === 0) ? grid[i][j] : shapeCoords.reduce(
                (accumulator, coord) => accumulator + grid[coord[0]][coord[1]],
                0
            )
            rhombusSum -= rhombusSumPoints
            rhombusVals.add(rhombusSum)
        } else {
            break
        }
        delta++
    }
    return rhombusVals
}

function getBorderSum(start,end,dir,grid) {
    let sum = 0
    let r = start[0]
    let c = start[1]
    while(r != end[0] || c != end[1]) {
        sum += grid[r][c]
        r += dir[0]
        c += dir[1]
    }
    sum += grid[r][c]
    return sum
}

function coordsInBounds(shapeCoords,grid){
    let inBounds = true
    shapeCoords.forEach((coord) => {
        if(!isInBounds(coord[0], coord[1], grid)){
            inBounds = false
        }
    })
    return inBounds
}

function isInBounds(i,j,grid){
    let m = grid.length
    let n = grid[0].length
    return (0 <= i && i < m) && ( 0 <= j && j < n)
}
