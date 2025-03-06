'''
URL := https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/description/
1524. Number of Sub-arrays With Odd Sum

Idea is right somewhere - needs a bit more refinement again :-)

Idea:
Time = O(N)
S = O(1) ( E ) O(1) ( I ) 

Intuition and Approach :

[1,3,5]
The 0 case is missing here ! OHHHHH all the way to the left!
psums = [1,4,9]
number = [1,1,2]
Oh we need the number of sums -> not the number of prefix arrays matching
wait a second

[1,2,3,4,5,6,7]
Prefix Sums : 1,3,4,10,15,21,28 per each index
number of odd sums at each index
{1,1,2,2,3,4,3}
sum = 16
'''
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        numMeetsCriteria = 0
        MODULO = pow(10,9) + 7
        prefixSum = 0
        # Offset for the0 case handling
        numEvenSums = 1
        numOddSums = 0
        for val in arr:
            prefixSum += val
            # [1] Evaluate number subarrays
            # [2] Update running counts
            if(prefixSum % 2 == 0):
                numMeetsCriteria += numOddSums
                numEvenSums += 1
            else:
                numMeetsCriteria += numEvenSums
                numOddSums += 1
        numMeetsCriteria = numMeetsCriteria % MODULO
        return numMeetsCriteria
        
