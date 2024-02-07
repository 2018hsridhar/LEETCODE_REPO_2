/**
 * @param {character[]} tasks
 * @param {number} n
 * @return {number}
 */
 /*
 URL := https://leetcode.com/problems/task-scheduler/description/
 Classic CPU-Task scheduling question
    Tasks : do in any order or do in a speciic order
    What is unit of time for a given task
621. Task Scheduler

 Minimum number of units of time for CPU to finish all tasks
 Do we have a cooldown period between two tasks?

 Return the number of units -> not actual task allocation strategy
 mostFreqval + (mostFreqVal - 1) * n = chain length needed ( for longest taking task )
 "squeeze property" as well

20 minutes to solutioning woooh still recall from earlier!

Approach : Greedy, Counting, HashMaps
 */
var leastInterval = function(tasks, n) {
    let taskFreqMap = new Map()
    let mostFreqTask = ''
    let mostFreqVal = 0
    let freqValFreq = 0
    tasks.forEach((task) => {
        if(!taskFreqMap.has(task)){
            taskFreqMap.set(task,0)
        }
        let nextVal = taskFreqMap.get(task) + 1
        taskFreqMap.set(task, nextVal)
        if(nextVal > mostFreqVal){
            mostFreqVal = nextVal
            mostFreqTask = task
            freqValFreq = 1
        } else if ( nextVal === mostFreqVal) {
            freqValFreq++
        }
    })
    let numberGaps = (mostFreqVal - 1) * n
    let offsetTasks = (freqValFreq - 1)
    let numOtherTasks = tasks.length - mostFreqVal - offsetTasks
    let numInBetweenTasks = Math.max(numberGaps, numOtherTasks)
    let totalTime = numInBetweenTasks + (mostFreqVal) + offsetTasks
    return totalTime
};
