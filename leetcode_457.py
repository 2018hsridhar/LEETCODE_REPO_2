'''
URL := https://leetcode.com/problems/circular-array-loop/description/
457. Circular Array Loop

# Approach and Intuition 
Category : Linear Scan, Cycle Detection, Tracking with counters, Hashmaps

Target complexity
Let N := length(nums)
$$O(N)$$
$$O(N)$$ ( Explicit )
$$O(1)$$ ( Implicit )
'''
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        hasCycle = False
        # Py3 DSA easy to instantiate
        visitedNodes = set()
        n = len(nums)
        for idx,num in enumerate(nums):
            status = self.getCycle(idx, nums)
            hasCycle = hasCycle | status
        return hasCycle
        
    # can not be size one : take note of this
    def getCycle(self, node:int, nums: List[int]) -> bool:
        cycleStatus = True
        n = len(nums)
        num = nums[node]
        nextVal = (node + num) % n
        cycleStatus &= (node != nextVal)
        visited = set()
        initNode = node # the first progeneitor check
        startDir = (num>0)
        while(True):
            visited.add(node)
            num = nums[node]
            nextDir = (num > 0)
            cycleStatus &= (nextDir == startDir)
            childNode = (node + num) % n
            if(childNode not in visited):
                node = childNode
            elif(childNode in visited):
                cycleStatus &= (childNode == initNode)
                break
        return cycleStatus
