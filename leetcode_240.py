'''
240. Search a 2D Matrix II
URL := https://leetcode.com/problems/search-a-2d-matrix-ii/description/

M = #-rows
N = #-cols
T = O(MlgN)
S = O(1) ( Exp ) O(1) ( Imp )

'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # subscript notation derefence to underneath `.` notation?
        m = len(matrix)
        n = len(matrix[0])
        # does practicing good naming here translate elsewhere
        foundTargetStatus = False
        for row in range(m):
            low = 0
            high = n - 1
            while(low <= high):
                mid = (int)(low + (int)((high-low)/2))
                candidate = matrix[row][mid]
                if(candidate == target):
                    foundTargetStatus = True
                    break
                elif(candidate < target):
                    low = mid + 1
                elif(candidate > target):
                    high = mid - 1
        return foundTargetStatus

        
