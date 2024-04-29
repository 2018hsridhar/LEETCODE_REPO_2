'''
1670. Design Front Middle Back Queue
URL := https://leetcode.com/problems/design-front-middle-back-queue/description/

# OMG a DLL class for this problem
# Ok a DLL is a lot of work, but does work. Can we do this faster for now -> with array reslicing?
# can we dodge a sentinel node? do a length check here
# set up head-tail nodes ( init to None )
# Preserve notions of indices too
# it's a lot of reslicing operations to be done here, sadly.
# Why not reslice directly ( versus weird middle index manipulation )
# A reslice way can be future converted to an index-based way too :-)
Ok so it is working code -> index error ( that's good ) 
'''
class FrontMiddleBackQueue:

    def __init__(self):
        self.list = []
        self.length = 0
        self.head = 0
        self.tail = 0
        self.middle = 0

    def pushFront(self, val: int) -> None:
        self.list.insert(0,val)
        self.length += 1
        if(self.isEven()):
            self.shiftMiddlePointerBack()
        elif(self.isOdd()):
            self.NOP()

    # assume no empty list case here
    def pushMiddle(self, val: int) -> None:
        self.list.insert(self.middle,val)
        self.length += 1
        if(self.isEven()):
            self.shiftMiddlePointerFront()
        elif(self.isOdd()):
            self.shiftMiddlePointerBack()

    def pushBack(self, val: int) -> None:
        self.list.insert(self.tail,val)
        self.tail += 1
        self.length += 1
        if(self.isEven()):
            self.shiftMiddlePointerFront()
        elif(self.isOdd()):
            self.NOP()

    def popFront(self) -> int:
        if(self.length == 0):
            return -1
        self.length -= 1
        el = self.list.pop(0)
        if(self.isEven()):
            self.shiftMiddlePointerFront()
        elif(self.isOdd()):
            self.NOP()
        return el

    def popMiddle(self) -> int:
        if(self.length == 0):
            return -1
        self.length -= 1
        el = self.list.pop(self.middle)
        if(self.isEven()):
            self.shiftMiddlePointerFront()
        elif(self.isOdd()):
            self.shiftMiddlePointerFront()
        return el

    def popBack(self) -> int:
        if(self.length == 0):
            return -1
        self.length -= 1
        el = self.list.pop(self.tail)
        self.tail -= 1
        if(self.isEven()):
            self.NOP()
        elif(self.isOdd()):
            self.shiftMiddlePointerBack()
        return el
    
    def NOP(self) -> None:
        return

    # Parity-driven, pointer-shifting data structure.
    def shiftMiddlePointerFront(self) -> None:
        if(self.length >= 2):
            self.middle += 1

    def shiftMiddlePointerBack(self) -> None:
        if(self.length >= 2):
            self.middle -= 1

    # Don't manipulate middle pointer if list length is only one element -> needs more elements
    def isEven(self) -> bool :
        return (self.length % 2 == 0)

# self positionArgs type error
    def isOdd(self) -> bool :
        return (self.length % 2 == 1)

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
