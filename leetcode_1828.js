/**
 * @param {number[][]} points
 * @param {number[][]} queries
 * @return {number[]}
 */
 /*
 URL := https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/description/
 1828. Queries on Number of Points Inside a Circle

 Knocking out the problem, even if it means being inefficient here on the way too
 Points on border := those are inside
 We'll be inefficient here
 2D Euclidean plane with potential of repeated points

 */
var countPoints = function(points, queries) {
    let q = queries.length
    // https://stackoverflow.com/questions/1295584/most-efficient-way-to-create-a-zero-filled-javascript-array
    // May have browser compatibility struggles
    // is a mutation method ( .fill ) : arr needs a length
    let answer = Array(q).fill(0) // ES6 prototype .fill()
    // Multiple assignment comma seperated values in JS
    let writeIndex = 0, numberPointsInCircle = 0, distanceCenterPoint = 0, radius = 0
    queries.forEach((query) => {
        radius = query[2]
        let center = query.slice(0,2) //[0,1]
        points.forEach((point) => {
            distanceCenterPoint = l2Norm(center,point)
            if(distanceCenterPoint <= radius){
                numberPointsInCircle++
            }
        })
        answer[writeIndex++] = numberPointsInCircle
        numberPointsInCircle = 0
    })
    return answer    
};

function l2Norm(a,b) {
    let delX = a[0] - b[0]
    let delY = a[1] - b[1]
    return Math.sqrt(Math.pow(delX,2) + Math.pow(delY,2))
}
