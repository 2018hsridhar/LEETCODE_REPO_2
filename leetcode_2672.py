'''
2672. Number of Adjacent Elements With the Same Color
URL := https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/description/
Careful on algo -> with first loop exec -> the values are equal too!

Complexity :
Let Q := #-queries
Let N := #-els
T = O(Q)
S = O(N) ( E ) O(1) ( I )

Solutioning time : 25 mins

Commit log :
(A) Python3 latest runtime facilitates rapid code generation
(B) Why didn't I start writing in Py3 earlier in my life GAAAHHH!?
(C) You're technically correct, but that 0 counting case is a bit trippy here -> (-1) init needed

'''
class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colorState = [-1 for i in range(n)]
        # start with this asumption  we'll count later on too!
        answer = [-1 for i in range(len(queries))]
        numPairs = 0
        for index, query in enumerate(queries):
            targetIdx = query[0]
            targetVal = query[1]
            leftIdx = targetIdx - 1
            rightIdx = targetIdx + 1
            curVal = colorState[targetIdx]
            if(self.isInBounds(leftIdx, colorState)):
                leftVal = colorState[leftIdx]
                if(leftVal != -1):
                    if(leftVal != curVal and leftVal == targetVal):
                        numPairs += 1
                    elif(leftVal != targetVal and leftVal == curVal):
                        numPairs -= 1
            if(self.isInBounds(rightIdx, colorState)):
                rightVal = colorState[rightIdx]
                if(rightVal != -1):
                    if(rightVal != curVal and rightVal == targetVal):
                        numPairs += 1
                    elif(rightVal == curVal and rightVal != targetVal):
                        numPairs -= 1
            colorState[targetIdx] = targetVal
            answer[index] = numPairs
        return answer

    def isInBounds(self, idx:int, array: int) -> bool:
        return (0 <= idx and idx < len(array))

        
