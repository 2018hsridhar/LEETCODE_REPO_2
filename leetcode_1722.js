/**
 * @param {number[]} source
 * @param {number[]} target
 * @param {number[][]} allowedSwaps
 * @return {number}
 */
 /*
 URL := https://leetcode.com/problems/minimize-hamming-distance-after-swap-operations/description/
1722. Minimize Hamming Distance After Swap Operations

 Allowed swap operations -> 
    seems like a graph problem in the hiding TBH
    Infinite, any order swapping

Some elements not swappable -> must check anyways

 */
var minimumHammingDistance = function(source, target, allowedSwaps) {
    let mhd = 0
    adjList = new Map()
    for(let i = 0; i < target.length; i++){
        adjList.set(i, new Set())
    }
    createAdjList(allowedSwaps,adjList)
    let visited = new Set()
    let connComp = new Set()
    for(let i = 0; i < target.length; i++){
        if(!visited.has(i)){
            dfs(i,visited,connComp,adjList)
            mhd += connCompMHD(source,target,connComp)
            connComp.clear()
        }
    }
    return mhd / 2
};

function createAdjList(swaps,adjList){
    swaps.forEach((swap) => {
        let src = swap[0]
        let dst = swap[1]
        adjList.get(src).add(dst)
        adjList.get(dst).add(src)
    })
}

function dfs(node,visited,connComp,adjList){
    if(!visited.has(node)){
        visited.add(node)
        connComp.add(node)
        adjList.get(node).forEach((child) => {
            dfs(child,visited,connComp,adjList)
        })
    }
}

// Two hashmaps : source and destination -> min of both maps
// Iterate over map one vals -> if val in two, get minimum
// if vals not in the other map -> it can not work
// number positions where elemnts differ -> mimnimize by making elemnts same
function connCompMHD(source,target,connComp){
    let srcFreq = new Map()
    let dstFreq = new Map()
    connComp.forEach((node) => {
        let srcVal = source[node]
        let dstVal = target[node]
        if(!srcFreq.has(srcVal)){
            srcFreq.set(srcVal,0)
        }
        srcFreq.set(srcVal, srcFreq.get(srcVal) + 1)
        if(!dstFreq.has(dstVal)){
            dstFreq.set(dstVal,0)
        }
        dstFreq.set(dstVal, dstFreq.get(dstVal) + 1)
    })
    let numSamePos = 0
    srcFreq.forEach((val,key) => {
        if(dstFreq.has(key)){
            numSamePos += 2 * Math.min(srcFreq.get(key), dstFreq.get(key))
        }
    })
    let numDiffPos = ( 2 * connComp.size ) - numSamePos
    return numDiffPos
}
