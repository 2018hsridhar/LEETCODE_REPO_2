/**
 * @param {number[][]} intervals
 * @return {number[]}
 */
 /*
 URL := https://leetcode.com/problems/find-right-interval/description/
 436. Find Right Interval

 15 mins to solutioning
 */
var findRightInterval = function(intervals) {
    let intervalInfo = intervals
        .map((interval,index) => { return [...interval, index] })
        .sort((a,b) => { return a[0] - b[0] }) // sort by nonDecr start time here
    return intervals.map((interval,idx) => {
            let bestIntervalInfoIndex = getBestInterval(interval, intervalInfo)
            return (bestIntervalInfoIndex === -1) ? -1 : intervalInfo[bestIntervalInfoIndex][2]
        })
};

// start_j minimized : not end_j minimized here!
function getBestInterval(interval,intervalInfo){
    let bestIntervalIdx = -1
    let low = 0
    let high = intervalInfo.length - 1
    let endI = interval[1]
    while(low <= high){
        let mid = Math.floor(0.5 * (low + high)) // gotch aiwht JS : gotta use a floor in binary search
        // let mid = (0.5 * (low + high)) // gotch aiwht JS : gotta use a floor in binary search
        let startJ = intervalInfo[mid][0]
        if(startJ === endI){
            bestIntervalIdx = mid
            break
        } else if ( startJ > endI ) { // can start later, but check if we can find a better start point -> go down!
            bestIntervalIdx = (bestIntervalIdx === -1) ? mid : Math.min(bestIntervalIdx, mid)
            high = mid - 1
        } else {
            low = mid + 1
        }
    }
    return bestIntervalIdx
}
