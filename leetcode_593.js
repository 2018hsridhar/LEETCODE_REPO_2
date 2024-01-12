**
 * @param {number[]} p1
 * @param {number[]} p2
 * @param {number[]} p3
 * @param {number[]} p4
 * @return {boolean}
 */
 /*
 URL := https://leetcode.com/problems/valid-square/description/
 593. Valid Square

 Complexity
 Time := O(1)
 Space := O(1) ( EXP & IMP ) 

 Valid square problem -> only so many point combinations to even test out
 Not just equal side lengths -> need angle checks as well
    ... hmmmm dot product testing then?


 Combinations are : 
 (p1,p2)-(p2,p3)-(p3,p4)-(p4,p1)
 (p1,p2)-(p2,p4)-(p4,p3)-(p3,p1)
 No order to inputs
 Handle rhomboid shapes

 Use square diagonals : diagonals of same length?
 And then the sides too?

diag(p1,p2) = diag(p3,p4)
    - and other testing too : d(p1,p3) and d(p1,p4) equal
    - hey this might be easier now?
 diag(p1,p3) = diag(p2,p4)
    d(p1,p2) = d(p1,p4) and d(p2,p3) = d(p2,p4)
    - this tyep of reasoning too
    - perpendicular Diagonals testing as well
diag(p1,p4) = diag(p2,p3)

Two vectors are perpendicular when their dot product equals to 0.
Recall how to find the dot product of two vectors ⟨v1,v2⟩ and ⟨w1,w2⟩
⟨v1,v2⟩⋅⟨w1,w2⟩=v1w1+v2w2

JS relaly does a good job with emphasis on functions as first class members
and doing well with return types on functions!

 */
var validSquare = function(p1, p2, p3, p4) {
    let status = false
    // Minimization point cloud combinations space too 
    let pointCombinations = [
        [p1,p2,p3,p4],
        [p1,p2,p4,p3],
        [p1,p3,p2,p4],
        [p1,p3,p4,p2],
        [p1,p4,p2,p3],
        [p1,p4,p3,p2],
        [p2,p3,p1,p4],
        [p2,p3,p4,p1],
        [p2,p4,p1,p3],
        [p2,p4,p3,p1],
        [p3,p4,p1,p2],
        [p3,p4,p2,p1],
    ]
    // no break in forEach JS expressions
    pointCombinations.forEach((pointCombo) => {
        // ensure each point is unique as well : if points equal, break
        // short circuit eval of functions
        if(hasDuplicatePoints(pointCombo) && passSquareTest(pointCombo)) {
                status = true
        }
    })
    return status
};

function hasDuplicatePoints(combo){
    for(let i = 0; i < combo.length; i++) {
        for(let j = i + 1; j < combo.length; j++) {
            let p1 = combo[i]
            let p2 = combo[j]
            if(equalPoints(p1,p2)){
                return false
            }
        }
    }
    return true
}

function equalPoints(p1,p2){
    return (p1[0] === p2[0] && p1[1] === p2[1])
}

function passSquareTest(combo){
    let isASquare = false
    // destructuring assignment : multi variable syntax assignation
    // let [p1,p2,p3,p4] = [combo[0],combo[1],combo[2],combo[3]]
    let [p1,p2,p3,p4] = combo // if same length in dimensions, it works!!!
    let diagOne = dist(p1,p3) 
    let diagTwo = dist(p2,p4) 
    let vecOne = [p3[0] - p1[0], p3[1] - p1[1]]
    let vecTwo = [p2[0] - p4[0], p2[1] - p4[1]]
    let d1 = dist(p1,p2)
    let d2 = dist(p2,p3)
    let d3 = dist(p3,p4)
    let d4 = dist(p4,p1)
    // console.log(dotProduct(diagOne,diagTwo))
    if(diagOne == diagTwo && dotProduct(vecOne,vecTwo) == 0) {
        // woooh transitive properties of equality in algebra!
        if(d1 > 0 && d1 === d2 && d2 === d3 && d3 === d4) {
            isASquare = true
        }
    }
    return isASquare
}

// JS Math package powerful -> just like Java
function dist(p1,p2){
    let del1 = p1[0] - p2[0]
    let del2 = p1[1] - p2[1]
    return Math.sqrt(Math.pow(del1,2) + Math.pow(del2,2))
}

function dotProduct(vecOne,vecTwo){
    let dotProd = vecOne[0]*vecTwo[0] + vecOne[1]*vecTwo[1]
    return dotProd
}
