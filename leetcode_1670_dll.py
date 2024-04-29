'''
1670. Design Front Middle Back Queue
OMG a DLL class for this problem
Ok a DLL is a lot of work, but does work. Can we do this faster for now -> with array reslicing?
Does someone really need to code up a DLL from scratch? Yes go know to code up a DLL -> but from a template!
URL := https://leetcode.com/problems/design-front-middle-back-queue/description/
'''

class Node:
    def __init__(self, data, prev, next):
        self.data = data
        self.next = next
        self.prev = prev

class FrontMiddleBackQueue:

# can we dodge a sentinel node? do a length check here
# set up head-tail nodes ( init to None )
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None
        self.middle = None

    def pushFront(self, val: int) -> None:
         frontNode = Node(val, None)
         if(self.head == None):
            self.head = frontNode
            self.tail = frontNode
            self.middle = None
        else:
            prevHead = head
            frontNode.next = prevHead
            self.head = frontNode
        self.length += 1
        if(self.length % 2 == 0):
            self.shiftMiddlePointerBack()

    # assume no empty list case here
    def pushMiddle(self, val: int) -> None:

        self.length += 1

    def pushBack(self, val: int) -> None:
         rearNode = Node(val, None)
         if(self.head == None):
            self.head = frontNode
            self.tail = frontNode
            self.middle = None
        else:
            prevTail = tail
            tail.next = rearNode
            self.tail = rearNode
        self.length += 1
        # even case is an adjustment
        if(self.length % 2 == 0):
            self.shiftMiddlePointerFront()

    def popFront(self) -> int:

    def popMiddle(self) -> int:

    def popBack(self) -> int:
        
    def shiftMiddlePointerFront(self) -> None:

    def shiftMiddlePointerBack(self) -> None:

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
