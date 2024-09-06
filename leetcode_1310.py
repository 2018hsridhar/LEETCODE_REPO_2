Intuition and Approach
Can we leverage range segmentation in our query computations?
E.g [5,8] => [5,6] and [7,8] => XOR each each subrange, if available for precomputation/
XOR is associative and commutative: aXb = bXa and aXbXc = aXcXc
aX0 = a
aXa = 0
^ Leverage identity element properties of XOR
Complexity
N:= length of the arr
Time complexity:
Time:=O(N)

Space complexity:
Space:=O(1) ( Explicit and Implicit )

Code
'''
URL := https://leetcode.com/problems/xor-queries-of-a-subarray/description/
1310. XOR Queries of a Subarray

'''
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xorAns = arr
        runXor = 0
        # enumerate simplifies list unpackaging
        for idx,el in enumerate(arr):
            runXor = runXor ^ el
            xorAns[idx] = runXor
        queryResp = [-1 for idx in range(len(queries))]
        for idx,query in enumerate(queries):
            upperTarget = query[1]
            lowerTarget = query[0]
            queryAns = xorAns[upperTarget]
            if(lowerTarget > 0):
                queryAns = xorAns[upperTarget] ^ xorAns[lowerTarget - 1]
            queryResp[idx] = queryAns
        return queryResp
