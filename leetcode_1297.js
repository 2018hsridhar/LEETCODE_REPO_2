/**
 * @param {string} s
 * @param {number} maxLetters
 * @param {number} minSize
 * @param {number} maxSize
 * @return {number}
 */
 /*
 URL := https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/description/
 1297. Maximum Number of Occurrences of a Substring

 */
var maxFreq = function(s, maxLetters, minSize, maxSize) {
    let maxOccursMap = new Map()
    let windowMap = new Map()
    let n = s.length
    let maxOccurs = 0, left = 0, right = 0
    for(let windowSize = minSize; windowSize <= maxSize; windowSize++){
        while(right < n){
            let curChar = s.charAt(right)
            if(!windowMap.has(curChar)){
                windowMap.set(curChar,0)
            }
            windowMap.set(curChar, windowMap.get(curChar) + 1)
            if(right - left + 1 > windowSize){
                let leftChar = s.charAt(left)
                windowMap.set(leftChar, windowMap.get(leftChar) - 1)
                if(windowMap.get(leftChar) === 0){
                    windowMap.delete(leftChar)
                }
                left++
            } 
            // let numKeys = Object.keys(windowMap).length // wow Object.keys(map).length for number keys gaaah
            let numKeys = windowMap.size // wow Object.keys(map).length for number keys gaaah
            // let numKeys = windowMap.keys().size // wow Object.keys(map).length for number keys gaaah
            if((right-left+1) === windowSize && numKeys <= maxLetters){
                let strSlice = s.slice(left,right + 1)
                if(!maxOccursMap.has(strSlice)){
                    maxOccursMap.set(strSlice,0)
                }
                let nextVal = maxOccursMap.get(strSlice) + 1
                maxOccursMap.set(strSlice, nextVal)
                maxOccurs = Math.max(maxOccurs,nextVal)
            }
            right++
        }
        windowMap.clear() // remove all k-v pairs from map() in JS
        left, right = 0
    }
    return maxOccurs
};
