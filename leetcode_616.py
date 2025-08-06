'''
URL := https://leetcode.com/problems/add-bold-tag-in-string/description/
616. Add Bold Tag in String

It's an intervals merge problem in the hiding ( if intersecting <b></b> intervals, merge them until we get final state )

Small enough constraints - brute force it :-)
S = 1000
W = 100
M = 1000

Time
Space

15 mins and solutioned ( 2 problems ) 
'''
class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        intervals = []
        sLen = len(s)
        for word in words:
            wLen = len(word)
            bound = (sLen - wLen) + 1
            for left in range(0,bound,1):
                right = left + wLen
                candidate = s[left:right]
                if(candidate == word):
                    interval = [left,right]
                    intervals.append(interval)
        intervals.sort(key = lambda x : (x[0],x[1]))
        mergedIntervals = self.mergeIntervals(intervals)
        boldedString = self.makeBoldedString(s,mergedIntervals)
        return boldedString

    def makeBoldedString(self, s:str, intervals:List[int]) -> str:
        boldedString = ""
        LEFT_BOLD = "<b>"
        RIGHT_BOLD = "</b>"
        # makeNewString
        leftPos = set()
        rightPos = set()
        for [left,right] in intervals:
            leftPos.add(left)
            rightPos.add(right)
        for index,letter in enumerate(s):
            if(index in leftPos):
                boldedString += LEFT_BOLD
            if(index in rightPos):
                boldedString += RIGHT_BOLD
            boldedString += letter
        # ahh last interval case SMH
        maxIndex = len(s)
        if(maxIndex in rightPos):
            boldedString += RIGHT_BOLD
        return boldedString
        
    def mergeIntervals(self, intervals:List[int]) -> List[int]:
        if(len(intervals) == 0):
            return intervals
        merged = []
        curInt = intervals.pop(0)
        while(len(intervals) > 0):
            childInt = intervals.pop(0)
            if(self.hasIntersection(curInt,childInt)):
                [leftOne,rightOne] = curInt
                [leftTwo,rightTwo] = childInt
                leftMost = min(leftOne,leftTwo)
                rightMost = max(rightOne,rightTwo)
                curInt = [leftMost,rightMost]
            else:
                merged.append(curInt)
                curInt = childInt
        # End of the Line
        merged.append(curInt)
        return merged

    def hasIntersection(self, intOne,intTwo) -> bool:
        [leftOne,rightOne] = intOne
        [leftTwo,rightTwo] = intTwo
        caseOne = (leftOne <= leftTwo and leftTwo <= rightOne)
        caseTwo = (leftTwo <= leftOne and leftOne <= rightTwo)
        return (caseOne or caseTwo)
