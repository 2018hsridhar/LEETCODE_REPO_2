'''
URL := https://leetcode.com/problems/partition-string/description/
3597. Partition String 

Complexity
S = len(S)
T = O(S)
S = O(S) ( E ) O(1) ( I ) ( Worst case ) 
'''
class Solution:
    def partitionString(self, s: str) -> List[str]:
        seenSegments = set()
        EMPTY = ""
        curSegment = EMPTY
        segments = []
        for letter in s:
            curSegment += letter
            if(curSegment not in seenSegments):
                seenSegments.add(curSegment)
                segments.append(curSegment)
                curSegment = EMPTY
        return segments        
