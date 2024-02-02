/**
 * @param {number[]} rungs
 * @param {number} dist
 * @return {number}
 */
 /*
 URL := https://leetcode.com/problems/add-minimum-number-of-rungs/description/
 1936. Add Minimum Number of Rungs

d:2
 3-1 = 2 / 2 = 1
 10 - 5 = 5 / 2 = 2.5 ~ 3

d:2
3-0 = 3 / 2 = 1.5 ~ 2

Note : current height of floor 0 too
Rungs on a ladder reach the last rung.

 */
var addRungs = function(rungs, dist) {
    let minRungs = 0
    let n = rungs.length
    let i = 0
    let curStep = 0
    while(i < n){
        let nextStep = rungs[i]
        let numberFitDist = Math.ceil((nextStep - curStep ) / dist)
        if(numberFitDist > 1){
            minRungs += (numberFitDist - 1)
        }
        curStep = nextStep
        i++
    }
    return minRungs
};
