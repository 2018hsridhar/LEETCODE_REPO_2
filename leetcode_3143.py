'''
3143. Maximum Points Inside the Square
URL := https://leetcode.com/problems/maximum-points-inside-the-square/description/

Fun combination of methods : sorting, binary search, prefixSums, and optimization
N - len(points)
T = O(nlgn)
S = O(N) ( Exp ) O(1) ( Imp ) 

'''
class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        maxPoints = 0
        records = []
        worstDistance = 0
        distanceCount = dict()
        for index,point in enumerate(points):
            curDistance = self.getDistance(point)
            record = [points[index][0], points[index][1],s[index],self.getDistance(point)]
            worstDistance = max(worstDistance, self.getDistance(point))
            if(curDistance not in distanceCount):
                distanceCount[curDistance] = 0
            distanceCount[curDistance] += 1
            records.append(record)
        records.sort(key=lambda x : (x[3],x[2],x[0],x[1]))
        # no two points, same tag
        # we don't need distance -> just orderedness :-P
        prefixTags = []
        runMap = dict()
        for record in records:
            label = record[2]
            if(label not in runMap):
                runMap[label] = 0
            runMap[label] += 1
            copyMap = dict()
            for k, v in runMap.items():
                copyMap[k] = v
            prefixTags.append(copyMap)
        # close, but need distance notion
        # or ok ... it's sorted and growing - do we need bsearch?
        # can we join values at same distance?
        # distance count check ( till one ) 
        for index,prefixTag in enumerate(prefixTags):
            candidDist = records[index][3]
            distFreq = distanceCount[candidDist]
            if(distFreq > 1):
                distanceCount[candidDist] -= 1
            elif(distFreq == 1):
                del distanceCount[candidDist] 
                tagMap = prefixTags[index]
                isValidSquare = True
                for k, v in tagMap.items():
                    if(v >= 2):
                        isValidSquare = False
                if(isValidSquare == True):
                    maxPoints = max(maxPoints,  index + 1)
        return maxPoints

    # woooh abs(...) stdalone function
    def getDistance(self, point: List[int]) -> int:
        furtherDist = max(abs(point[0]),abs(point[1]))
        return furtherDist
        
