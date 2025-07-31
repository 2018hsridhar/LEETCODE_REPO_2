'''
2015. Average Height of Buildings in Each Segment
URL := https://leetcode.com/problems/average-height-of-buildings-in-each-segment/description/

Sorted, Greedy, Iterate over Buildings L->R
pow(10,8) buildings - we can prefix sum, because only 
pow(10,5) buildings max

Complexity
N = len(buildings)
Time = O(NlgN)
S = O(1) ( E ) O(1) ( I )
'''
class Solution:
    def averageHeightOfBuildings(self, buildings: List[List[int]]) -> List[List[int]]:    
        # Sort : left->right->height
        # Half-closed segments : { left_j, right_j }
        buildings.sort(key = lambda  x: (x[0],x[1],x[2]))
        records = []
        for buildIndex,[left,right,height] in enumerate(buildings):
            leftRec = [buildIndex,left,height]
            rightRec = [buildIndex,right,-1 * height]
            records.append(leftRec)
            records.append(rightRec)
        records.sort(key = lambda x : (x[1],x[2]))
        buildingCount = 0
        runningHeight = 0
        segments = []
        for pointOne,pointTwo in zip(records,records[1:]):
            [leftIdx,leftPos,leftHeight] = pointOne
            [rightIdx,rightPos,rightHeight] = pointTwo
            runningHeight += leftHeight
            # leftHeight to rightHeight
            if(leftHeight > 0):
                buildingCount += 1
            else:
                buildingCount -= 1
            # works but no merge intervals here :-(
            if(leftPos < rightPos and buildingCount > 0):
                runningAverage = (int)(runningHeight / buildingCount)
                segment = [leftPos,rightPos,runningAverage]
                if(len(segments) >= 1):
                    finSeg = segments[-1]
                    [finLeft,finRight,finHeight] = finSeg
                    if(finHeight == runningAverage and leftPos <= finRight):
                        segments[-1][1] = rightPos
                    else:
                        segments.append(segment)
                else:
                    segments.append(segment)
        return segments







        
