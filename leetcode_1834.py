Intuition and Approach
Think about using sorting ( greedy ) and heaps to solution the problem.

Complexity
Let N := length(input)

Time complexity:
O(NlgN)

Space complexity:
O(N) ( Explicit )
O(1) ( Implicit )

Code
'''
URL := https://leetcode.com/problems/single-threaded-cpu/description/
1834. Single-Threaded CPU

Intuition and Approach :
Task-ordering problems tend to be heap based.

Target complexity
Let N := len(tasks)
Time = O(NlgN)
Space = O(N) ( Explicit ) O(1) ( Implicit ) 

Have to finish executing all tasks.
30 minutes but solutioned ( should have been easier though ) 
'''
from heapq import heappop, heappush

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        finalTaskOrder = []
        # preprocessing grab index information
        # lex order : ( enqueueTime, procTime 
        actualTasks = []
        for idx,task in enumerate(tasks):
            struct = [task[0],task[1],idx]
            actualTasks.append(struct)
        # presort by enque time ( to know availability ) 
        actualTasks.sort(key = lambda x : (x[0],x[1],x[2]))
        n = len(tasks)
        firstTaskTime = actualTasks[0][0]
        curTime = firstTaskTime
        taskPriority = []
        firstRecord = (actualTasks[0][1],actualTasks[0][2])
        heapq.heappush(taskPriority, firstRecord)
        taskPtr = 1
        numTasksExec = 0
        while(numTasksExec < n):
            # NOT IDLE CPU CASE
            if(len(taskPriority) > 0):
                numTasksExec += 1
                taskProcTime, taskIndex = heapq.heappop(taskPriority)
                finalTaskOrder.append(taskIndex)
                curTime += taskProcTime
                while(taskPtr < n):
                    nextTask = actualTasks[taskPtr]
                    enqueueTime = nextTask[0]
                    procTime = nextTask[1]
                    indexTime = nextTask[2]
                    curRecord = (procTime, indexTime)
                    if(enqueueTime <= curTime):
                        heapq.heappush(taskPriority, curRecord)
                        taskPtr += 1
                    else:
                        break
            # IDLE CPU CASE
            # go reset out heap now
            elif(len(taskPriority) == 0):
                if(taskPtr < n):
                    nextTask = actualTasks[taskPtr]
                    enqueueTime = nextTask[0]
                    procTime = nextTask[1]
                    indexTime = nextTask[2]
                    curRecord = (procTime, indexTime)
                    heapq.heappush(taskPriority, curRecord)
                    curTime = enqueueTime
                    taskPtr += 1
                else:
                    break
        return finalTaskOrder
        
