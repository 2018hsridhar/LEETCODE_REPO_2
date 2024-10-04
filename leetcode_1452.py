Intuition
Approach
Complexity
Let C := #-favorite company lists
Let F := length(longest list)

Time complexity:
O(pow(C,2)∗F)

Space complexity:
O(F) ( Explicit )
O(1) ( Implicit )

Code
'''
1452. People Whose List of Favorite Companies Is Not a Subset of Another List
URL := https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/submissions/1411706040/
'''
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        setPos = self.getSetPositions(favoriteCompanies)
        targetIndices = self.getTargetIndices(favoriteCompanies, setPos)
        return targetIndices

    def getSetPositions(self, favoriteCompanies: List[List[str]]) -> dict():
        setPos = dict()
        for index, favoriteCompany in enumerate(favoriteCompanies):
            for company in favoriteCompany:
                if(company not in setPos):
                    setPos[company] = set()
                setPos[company].add(index)
        return setPos
    
    def getTargetIndices(self, favoriteCompanies, setPos):
        # [2] Go through records again and determine intersectionality
        targetIndices = []
        for index, favoriteCompany in enumerate(favoriteCompanies):
            candidates = set()
            for company in favoriteCompany:
                companySet = setPos[company]
                if(len(candidates) == 0):
                    candidates = companySet
                else:
                    candidates = candidates.intersection(companySet)
            candidates.remove(index)
            if(len(candidates) == 0):
                targetIndices.append(index)
        return targetIndices
        
