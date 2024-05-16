'''
2615. Sum of Distances
URL - https://leetcode.com/problems/sum-of-distances/

Complexity :
Let N := len(nums)
Time := O(N)
Space := O(N) ( E ) O(1) ( I ) 

'''
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        myDistances = [0 for i in range(len(nums))]
        hitMap = {}
        # [1] Construct the hashmap for precomputation
        for index, num in enumerate(nums):
            if num not in hitMap:
                hitMap[num] = []
            hitMap[num].append(index)
        # [2] Execute computation using prefix sums and hash table approach
        for value,valIndices in hitMap.items():
            # print("Operating on val = " + str(value))
            # print("operating on indices = " + str(valIndices))
            n = len(valIndices)
            lhsSum = 0
            rhsSum = sum(valIndices) - (n * valIndices[0])
            counter = 1
            for index in range(len(valIndices)):
                targetIdx = valIndices[index]
                # print(targetIdx)
                sumVal = lhsSum + rhsSum
                myDistances[targetIdx] = sumVal
                if(index + 1 < len(valIndices)):
                    delta = valIndices[index+1] - valIndices[index]
                    lhsSum += (counter * delta)
                    rhsSum -= ((len(valIndices) - counter) * delta)
                    counter += 1
        return myDistances
        
