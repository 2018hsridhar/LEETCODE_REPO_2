/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @param {number[][]} queries
 * @return {boolean[]}
 */
 /*
 URL := https://leetcode.com/problems/course-schedule-iv/description/
 1462. Course Schedule IV
 */

// Could be a map[int][int] BUT we do need to know our priors as well
function solveInDeg(inDegMap, numCourses, prereqs){
    prereqs.forEach((edge) => {
        let src = edge[0]
        let dst = edge[1]
        inDegMap.set(dst,inDegMap.get(dst) + 1)
    })
}

// Top sort is a dag -> simplify maps to [int,Set<int>]
function makeAdjList(adjList, numCourses, prereqs){
    prereqs.forEach((edge) => {
        let src = edge[0]
        let dst = edge[1]
        adjList.get(src).add(dst)
    })
}

function execTopSort(prereqMap,inDegMap,adjList){
    frontier = []
    inDegMap.forEach((inDeg,node) => {
        if(inDeg == 0){
            frontier.push(node)
        }
    })
    while(frontier.length > 0){
        let parent = frontier.shift()
        let children = adjList.get(parent)
        children.forEach((child) => {
            inDegMap.set(child, inDegMap.get(child) - 1)
            prereqMap.get(child).add(parent) // prereq rel here
            if(inDegMap.get(child) == 0){
                frontier.push(child)
            }
            let parentPrereqs = prereqMap.get(parent)
            parentPrereqs.forEach((parentPrereq) => {
                prereqMap.get(child).add(parentPrereq)
            })
        })
    }
}

function initMapSet(numCourses){
    toRetMap = new Map()
    for(let i = 0; i < numCourses; i++){
        toRetMap.set(i,new Set())
    }
    return toRetMap
}

// function printMap(myMap){
//     myMap.forEach((val,key) => {
//         console.log("For key = " + key + "\t: val = ")
//         console.log(val)
//     })
// }

var checkIfPrerequisite = function(numCourses, prerequisites, queries) {
    let q = queries.length
    let inDegMap = new Map()
    for(let i = 0; i < numCourses; i++){
        inDegMap.set(i,0)
    }
    let adjList = initMapSet(numCourses)
    let prereqMap = initMapSet(numCourses)
    solveInDeg(inDegMap,numCourses,prerequisites)
    makeAdjList(adjList,numCourses,prerequisites)
    execTopSort(prereqMap,inDegMap,adjList)
    let queryResponse = Array(q).fill(false)
    let wIdx = 0
    queries.forEach((query) => {
        let uj = query[0]
        let vj = query[1]
        if(prereqMap.has(vj) && prereqMap.get(vj).has(uj)) {
            queryResponse[wIdx] = true
        }
        wIdx++
    })
    return queryResponse
};
