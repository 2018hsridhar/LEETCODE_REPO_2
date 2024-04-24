'''
URL := https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/description/
3106. Lexicographically Smallest String After Operations With Constraint

Category : Greedy, Sorting, Counting, Indexing

Complexity : 
Let N := #-letters in the string
Time := O(N)
Space := O(1) ( E & I ) 

Close but at least more correct now :-)

'''
class Solution:
    # Be greedy and attempt to go a k distance, but in actuality, don't overshoot yourself too ( if you can not ) 
    def getSmallestString(self, s: str, k: int) -> str:
        smallestStr = ""
        index = 0
        # guaranteed monotonically decreasing k in each algorithmic iteration
        while index < len(s):
            if(k <= 0):
                break
            charAtI = s[index]
            ithValue = ord(charAtI) - ord("a")
            ithValToRight = ithValue + k
            ithValToLeft = ithValue - k
            posRight = 0 if (ithValToRight > 25) else ithValToRight
            posLeft = 0 if (ithValToLeft <= 0) else ithValToLeft
            # Positions be easy to calculate : what about the number of steps to iterate?
            deltaRight = (posRight - ithValue + 26) % 26
            deltaLeft = (ithValue - posLeft + 26) % 26
            charRight = chr(ord("a") + posRight)
            charLeft = chr(ord("a") + posLeft)
            # ord is for order() oh
            minStep = min(deltaLeft,deltaRight)
            minChar = charLeft if (charLeft < charRight ) else charRight
            smallestStr += minChar
            k -= minStep
            index += 1
        while index < len(s):
            smallestStr += s[index]
            index += 1
        return smallestStr
        
