/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 /*
URL := https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
34. Find First and Last Position of Element in Sorted Array

Ideas
1. Binary search
2. Input already sorted in order for us
3. Decompose into two seperate bSearches for ease

*/
var searchRange = function(nums, target) {
    let lowerPos = bSearchLower(nums,target)
    let upperPos = bSearchUpper(nums,target)
    return [lowerPos,upperPos]
};


function bSearchUpper(nums,target){
    let upperPos = -1
    let n = nums.length
    let low = 0
    let high = n - 1
    while(low <= high) {
        // JS explicitly needs the Math.floor here ( this ain't Java with the int conversions !) 
        let mid = Math.floor((high + low) / 2)
        if(nums[mid] === target) {
            upperPos = mid
            low = mid + 1 // keep searching, but to the right now. Do not break
        } else if ( nums[mid] < target) {
            low = mid + 1
        } else {
            high = mid - 1
        }
    }
    return upperPos
}

function bSearchLower(nums,target){
    let lowerPos = -1
    let n = nums.length
    let low = 0
    let high = n - 1
    while(low <= high) {
        let mid = Math.floor((high + low) / 2)
        if(nums[mid] === target) {
            lowerPos = mid
            high = mid - 1 // keep searching, but to the left now. Do not break
        } else if ( nums[mid] < target) {
            low = mid + 1
        } else {
            high = mid - 1
        }
    }
    return lowerPos
}
