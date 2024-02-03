/**
 * @param {number[]} nums
 * @return {number}
 */
 /*
 2860. Happy Students
 URL := https://leetcode.com/problems/happy-students/

 */
var countWays = function(nums) {
    let numWays = 0
    nums.sort((a,b) => { return Number(a) - Number(b)})
    console.log(nums)
    let numSel = 0
    if(nums[0] > 0) {
        numWays++ // no one selected : 
    }
    let n = nums.length
    nums.forEach((curNum,index) => {
        numSel += 1
        if(index < n - 1) {
            let nextIndex = index + 1
            if(numSel > curNum && numSel < nums[nextIndex]){
                numWays++
            }
        } else {
            if(numSel > curNum) {
                numWays++
            }
        }
    })
    return numWays
};
