'''
251. Flatten 2D Vector
URL := https://leetcode.com/problems/flatten-2d-vector/description/

Intuition & Approach :
Why are in-built data structure iterators so ubiquitous?
Value is either (a) a List[int] - of multiple integers OR (b) a List[int] ( single integer )
'''
class Vector2D:
    # def __init__(self, vec: List[List[int]]):
    #     self.vec = vec
    #     self.ptrInVec = 0
    #     self.ptrOutVec = 0
    #     self.size = len(self.vec)

    # def next(self) -> int:
    #     targetRecord = self.vec[self.ptrOutVec]
    #     if(self.ptrInVec < len(targetRecord) - 1):
    #         targetEl = targetRecord[self.ptrInVec]
    #         self.ptrInVec += 1
    #     elif(self.ptrInVec == len(targetRecord) - 1):
    #         targetEl = targetRecord[self.ptrInVec]
    #         self.ptrInVec = 0
    #         self.ptrOutVec += 1
    #     return targetEl

    # # if list is a null -> return false ( ahh dang ) 
    # # made more sense when we did the preallocation TBH
    # def hasNext(self) -> bool:
    #     return (self.ptrOutVec < self.size)
        
    def __init__(self, vec: List[List[int]]):
        self.vec = []
        for elem in vec:
            if(type(elem) is list):
                if(len(elem) > 1):
                    for interior in elem:
                        self.vec.append(interior)
                elif(len(elem) == 1):
                    self.vec.append(elem[0])
        self.ptr = 0
        self.size = len(self.vec)

    def next(self) -> int:
        targetEl = self.vec[self.ptr]
        self.ptr += 1
        return targetEl

    def hasNext(self) -> bool:
        return (self.ptr < self.size)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()
