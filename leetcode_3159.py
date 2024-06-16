'''
URL := https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/description/
3159. Find Occurrences of an Element in an Array

Single integer only -> can we linear scan ( and avoid extra space )?
or create a map as we go and append anyways ( keys known in the future too ! ) 

It's the occurence of x -> get positional information ( OOHH ) 
    query(3) -> third occurence -> nope
    query(4) -> fourth occurence -> nope
    query(2) -> second occurence -> 2
    query(1) -> first occurence -> 0

'''
class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        q = len(queries)
        occurences = [-1 for i in range(q)]
        elementIndex = dict()
        hitPos = []
        for index, num in enumerate(nums):
            if(num == x):
                hitPos.append(index)
        for index, query in enumerate(queries):
            queryDelta = query - 1
            if(queryDelta < len(hitPos)):
                occurences[index] = hitPos[queryDelta]
        return occurences
        
