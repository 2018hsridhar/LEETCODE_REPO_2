# Duplicate points allowed : how to track point frequency ( store with the y coordinate too )?
# Count number of formed squares
# URL := https://leetcode.com/problems/detect-squares/description/
# Count of well formed squares : 
class DetectSquares:

    def __init__(self):
        self.pointFreq = dict()
        self.xMap = dict()
        self.yMap = dict()
        self.numPointsOnGrid = 0

    def add(self, point: List[int]) -> None:
        x = point[0]
        y = point[1]
        uniqKey = self.makePoint(x,y)
        if(uniqKey not in self.pointFreq):
            self.pointFreq[uniqKey] = 0
        # self.<identifier> at a different scope ( the class not the method ) 
        self.pointFreq[uniqKey] += 1
        # index-based accessor for our maps :-)
        self.numPointsOnGrid += 1

    def count(self, point: List[int]) -> int:
        # ways for 3 points ( ignore the 4th point if any duplicates )
        # must be positive area calculations only
        squareCount = 0
        x1 = point[0]
        y1 = point[1]
        curPointKey = self.makePoint(x1,y1)
        for cornerKey,freqCorner in self.pointFreq.items():
            if(cornerKey != curPointKey):
                tokens = cornerKey.split("&")
                x2 = int(tokens[0])
                y2 = int(tokens[1])
                if(abs(x2-x1) == abs(y1-y2) and abs(x2-x1) != 0 and abs(y1-y2) != 0):
                    pointKeyOne = self.makePoint(x1,y2)
                    pointKeyTwo = self.makePoint(x2,y1)
                    if(pointKeyOne in self.pointFreq and pointKeyTwo in self.pointFreq):
                        freqOne = self.pointFreq[pointKeyOne]
                        freqTwo = self.pointFreq[pointKeyTwo]
                        delta = (freqOne * freqTwo * freqCorner)
                        squareCount += delta
        return squareCount


    def makePoint(self, x:int, y:int) -> str:
        res = '%s&%s' % (x,y)
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
