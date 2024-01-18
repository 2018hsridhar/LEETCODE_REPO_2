/**
 * @param {number[]} arr
 * @param {number[][]} mat
 * @return {number}
 */
 /*
 URL := https://leetcode.com/problems/first-completely-painted-row-or-column/
 2661. First Completely Painted Row or Column

Index as we paint here
9 mins to solutioning is easy :-)

 */
var firstCompleteIndex = function(arr, mat) {
    let firstCompIndex = -1;
    let elCellMap = new Map()
    let rowCountMap = new Map()
    let colCountMap = new Map()
    let m = mat.length
    let n = mat[0].length
    for(let i = 0; i < m; i++){
        for(let j = 0; j < n; j++){
            let el = mat[i][j]
            elCellMap.set(el,[i,j])
        }
    }
    for(let i = 0; i < arr.length; i++){
        let el = arr[i]
        if(elCellMap.has(el)){
            let wArr = elCellMap.get(el)
            let wR = wArr[0]
            let wC = wArr[1]
            if(!rowCountMap.has(wR)){
                rowCountMap.set(wR,0)
            }
            if(!colCountMap.has(wC)){
                colCountMap.set(wC,0)
            }
            rowCountMap.set(wR,rowCountMap.get(wR) + 1)
            colCountMap.set(wC,colCountMap.get(wC) + 1)
            let curRowCount = rowCountMap.get(wR)
            let curColCount = colCountMap.get(wC)
            if(curRowCount == n || curColCount == m){
                firstCompIndex = i
                break
            }
        }

    }
    return firstCompIndex;
};
