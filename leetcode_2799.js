/**
 * @param {number[]} nums
 * @return {number}
 */
 /*
 URL := https://leetcode.com/problems/count-complete-subarrays-in-an-array/description/
 2799. Count Complete Subarrays in an Array

 Akin to using an ideas of a prefix -> once we know a prefix meets the condition, any remaining subarrs formed from said prefix
 will also meet the invariant. Use sliding windows here

 15 mins to solutioning
 */
var countCompleteSubarrays = function(nums) {
    let n = nums.length
    let ccs = 0, left = 0, right = 0
    let wholeDistinct = new Set(nums).size
    let window = new Map()
    while(right < n) {
        let rightEl = nums[right]
        if(!window.has(rightEl)){
            window.set(rightEl,0)
        }
        window.set(rightEl, window.get(rightEl) + 1)
        while(window.size === wholeDistinct && left <= right){ // okay at this right, we have a known
            ccs += (n - right)
            let leftEl = nums.at(left)
            let newLeftCount = window.get(leftEl) - 1
            window.set(leftEl, newLeftCount)
            if(newLeftCount === 0){
                window.delete(leftEl)
            }
            left++
        } 
        right++
    }
    return ccs
};

// Sets and Maps -> size is a property, not a method
// https://stackoverflow.com/questions/28965112/javascript-array-to-set
