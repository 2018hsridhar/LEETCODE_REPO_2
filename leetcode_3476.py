'''
3476. Maximize Profit from Task Assignment
URL = https://leetcode.com/problems/maximize-profit-from-task-assignment/description/
'''
class Solution:
    def maxProfit(self, workers: List[int], tasks: List[List[int]]) -> int:
        totalProfit = 0
        workers.sort()
        tasks.sort(key = lambda x : (x[0],-1 * x[1]))
        tIdx = 0
        wIdx = 0
        visited = set()
        # get best assignment
        print(tasks)
        while(tIdx < len(tasks) and wIdx < len(workers)):
            if(tasks[tIdx][0] == workers[wIdx]):
                totalProfit += tasks[tIdx][1]
                visited.add(tIdx)
                wIdx += 1
                tIdx += 1
            elif(tasks[tIdx][0] < workers[wIdx]):
                tIdx += 1
            elif(tasks[tIdx][0] > workers[wIdx]):
                wIdx += 1
        # get best task remaining
        remTasks = []
        maxObs = 0
        for idx, task in enumerate(tasks):
            if(idx not in visited):
                maxObs = max(maxObs, tasks[idx][1])
        totalProfit += maxObs
        return totalProfit
            
        
