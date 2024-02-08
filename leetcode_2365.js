/**
 * @param {number[]} tasks
 * @param {number} space
 * @return {number}
 */
 /*
 https://leetcode.com/problems/task-scheduler-ii/
2365. Task Scheduler II

Complexity
Let T := #-tasks
Time := O(T) (single pass)
Space := O(T) ( exp map ) O(1) ( call stack ) 

Addition to the minDays here
(A) Work on current task -> add one day
    ( single day to process a task; task consumes 1 day )
(B) Stay idle ( get next working day of a task )

Task completion is greedy-based usually
12 mins to solutioning :-)
 */
var taskSchedulerII = function(tasks, space) {
    let minDays = 0
    let taskMap = new Map()
    tasks.forEach((curTask) => {
        if(!taskMap.has(curTask)){ // new type case : always doable
            taskMap.set(curTask,minDays + space) // minDays val must be greater then this
            minDays++
        } else {
            let nextDayTaskExecutable = taskMap.get(curTask) + 1 // be on this exact day
            if(minDays < nextDayTaskExecutable){
                minDays = nextDayTaskExecutable // make the jump and sadly stay idle
            }
            taskMap.set(curTask,minDays + space)
            minDays++
        }
    })
    return minDays
};
