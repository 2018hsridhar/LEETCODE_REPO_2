/**
 * @param {number[]} arr
 * @return {number[]}
 */
/*
URL := https://leetcode.com/problems/pancake-sorting/description/
969. Pancake Sorting

The Bill Gates Problem :-) 
30 mins to solutioning ( 15 misn to understanding ) 

*/
var pancakeSort = function(arr) {
    let kVals = []
    let n = arr.length
    for(let writeIdx = n-1; writeIdx >= 0; writeIdx--){
        let maxElIdx = getMaxIdx(arr,writeIdx+1) // up to a bound
        if(maxElIdx < writeIdx) {
            // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice
            // exclusive : 0 to maxElIdx only
            let flipPrefixArr = arr.slice(0,maxElIdx + 1).reverse()
            let flipSuffix = arr.slice(maxElIdx + 1) // what was excluded
            arr = flipPrefixArr.concat(flipSuffix)
            kVals.push(maxElIdx+1)
            if(maxElIdx != writeIdx) {
                kVals.push(writeIdx+1)
                let flipToWrite = arr.slice(0,writeIdx+1).reverse()
                let rightAsIs = arr.slice(writeIdx+1)
                arr = flipToWrite.concat(rightAsIs)
            }
        }
    }
    return kVals
};

function getMaxIdx(arr, indexBound){
    let maxEl = Number.MIN_VALUE
    let maxIdx = -1
    arr.forEach((el,idx) => {
        if(el >= maxEl && idx < indexBound) {
            maxIdx = idx
            maxEl = el
        }
    })
    return maxIdx
}
