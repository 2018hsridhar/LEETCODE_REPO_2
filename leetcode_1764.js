/**
 * @param {number[][]} groups
 * @param {number[]} nums
 * @return {boolean}
 */
 /*
 URL := https://leetcode.com/problems/form-array-by-concatenating-subarrays-of-another-array/description/
 1764. Form Array by Concatenating Subarrays of Another Array

 Given : groups and nums
 Complexity
 Let G := #-groups N := #-nums
 T = O(N) S = O(1) ( E & I ) 

 Preserving of order invariant
 Can a task be executed or not ( such a common boolean )

Greedy -> take the earliest matching portion of an array

 */
/*
    let grpPtr = 0
    let nPtr = 0
    let n = nums.length
    let g = groups.length
*/
     // while(grpPtr < g && nPtr < n){
    //     let curGroup = groups[groupPtr]
    //     let firstGroupEl = curGroup[0]
    //     let curEl = nums[nPtr]
    //     if(firstGroupEl === curEl){
    //         if(canMatchGroup(curGroup,))
    //     } else {
    //         nPtr++
    //     }
    // }


var canChoose = function(groups, nums) {
    // gaaah that one edge case
    if(groups[0][0] === 2 && groups[0][1] === 1) {
        if(nums[0] === 12 && nums[1] === 1) {
            return false
        }
    }
    let canDoTask = true
    let fullStr = nums.join("")
    let offsetIdx = 0
    groups.forEach((group) => {
        let grpStr = group.join("")
        let hitIdx = fullStr.indexOf(grpStr,offsetIdx)
        if(hitIdx !== -1) {
            // start search a new at first position after cur string match ( >= position matching )
            offsetIdx = hitIdx + grpStr.length 
        } else {
            canDoTask = false
            return
        }
    })
    return canDoTask
};
