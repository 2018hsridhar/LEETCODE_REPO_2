A somewhat more involved problem which combines traversals of ancestors and descendants :-)

'''
1993. Operations on Tree
URL := https://leetcode.com/problems/operations-on-tree/description/
#-calls to tree operations :- reasonable bound of 2,000

Target Complexity Analysis :
N := #-nodes in the tree
H := height of the tree : log(N) balanced (N) worst
D := Diameter of the tree ( N at worst ) 
O := #-operations
Time = 
Space = O() ( Explicit ) O() ( Implicit ) 

Bit of an involved problem and NOT the most compute/memory-efficient solution
Almost passing
Go Debug this later
You're almost there !!!
'''
class LockingTree:

    # we know it's n nodes labeled 0 to n-1
    def __init__(self, parent: List[int]):
        self.adjList = self.makeAdjList(parent)
        self.parentList = self.makeParentList(parent)
        self.nodeLockStatus = dict()
        for idx in range(len(parent)):
            # -1 : unlocked
            # not -1 : locked ( by user id ) 
            self.nodeLockStatus[idx] = -1

    def makeAdjList(self, parent: List[int]) -> dict:
        n = len(parent)
        adjList = dict()
        for idx in range(len(parent)):
            adjList[idx] = set()
        for child,par in enumerate(parent):
            if(par != -1):
                adjList[par].add(child)
        return adjList

    def makeParentList(self, parent: List[int]) -> dict:
        n = len(parent)
        parentList = dict()
        for child,par in enumerate(parent):
            if(child not in parentList):
                parentList[child] = set()
            parentList[child] = par
        return parentList

    # Must track the user which locked the node too.
    def lock(self, num: int, user: int) -> bool:
        status = False
        lockVal = self.nodeLockStatus[num]
        if(lockVal == -1):
            self.nodeLockStatus[num] = user
            status = True
        return status

    def unlock(self, num: int, user: int) -> bool:
        status = False
        lockVal = self.nodeLockStatus[num]
        if(lockVal == user):
            self.nodeLockStatus[num] = -1
            status = True
        return status

    def upgrade(self, num: int, user: int) -> bool:
        status = False
        condOne = (self.nodeLockStatus[num] == -1)
        # cond two : work on only the parent
        parent = self.parentList[num]
        condTwo = (self.dfsNoLockUp(parent) == True)
        # cond three : DFS from child node only
        # leaf case : will never work ( must have at least one locked descendant )
        condThree = False
        children = self.adjList[num]
        for child in children:
            condThree = condThree or self.dfsLockDown(child)
        if(condOne and condTwo and condThree):
            # unlock all descendants
            self.dfsUpgradeUnlock(num)
            # lock the current node
            self.nodeLockStatus[num] = user
            status = True
        return status

    def dfsLockDown(self, num:int) -> bool:
        status = (self.nodeLockStatus[num] != -1)
        children = self.adjList[num]
        for child in children:
            status = (status or self.dfsLockDown(child))
        return status

    def dfsUpgradeUnlock(self, num:int):
        children = self.adjList[num]
        for child in children:
            self.nodeLockStatus[child] = -1
            self.dfsUpgradeUnlock(child)

    def dfsNoLockUp(self, num:int) -> bool:
        # immediate ancestor ( base case ) 
        if(num == -1):
            return True
        status = (self.nodeLockStatus[num] == -1)
        parent = self.parentList[num]
        if(status == True):
            status = (status and self.dfsNoLockUp(parent))
        return status

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
