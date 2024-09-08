Python3 Solution Leveraging Hashmap and a Queue Determine Optional Number Alloc O(1) T O(N) S

Intuition
Think of cycles, queues and hashmaps ( two DS&A combined )
Hashmap to track status of slot : available or unavailable
Queue to track available and which to alloc
Len(queue) = 0 => ret -1 no slot avaialble

Complexity
Complexity
Let M:= max numbers
Let O:= number of operations

Time complexity:
O(O)=O(1)

Space complexity:
O(M) ( Explicit )
O(1) ( Implicit )

Code
'''
URL := https://leetcode.com/problems/design-phone-directory/description/
379. Design Phone Directory

'''
class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.slotStatus = dict()
        self.slotsAvail = []
        for slot in range(0,maxNumbers,1):
            # true ( can alloc ) false ( can not alloc ) 
            self.slotStatus[slot] = True
            self.slotsAvail.append(slot)

    # Centralized logging for how often specific code call paths are under exercise
    def get(self) -> int:
        slotAvail = -1
        if(len(self.slotsAvail) > 0):
            slotAvail = self.slotsAvail.pop(0)
            self.slotStatus[slotAvail] = False
        return slotAvail

    def check(self, number: int) -> bool:
        if(number in self.slotStatus):
            return self.slotStatus[number]

    def release(self, number: int) -> None:
        if(number in self.slotStatus and self.slotStatus[number] == False):
            self.slotStatus[number] = True
            self.slotsAvail.append(number)

        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
