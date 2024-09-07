Intuition & Approach
Let's keep a hashmap and a pointer to our constantly growing list
seems simplier : test if the el frequency is one ( greedily ). If elFreq = 1, it's first uniq
else, increment the pointer ( until it goes out of range ).
test the pointer ( since array size is growing as well )
So many design questions are architecting operations questions in the hiding.

Complexity
Let N:= number-values to append to our queue.
Time complexity:

Time = O(N)
Space complexity:

Space = O(N) ( Explicit ) O(1) ( Implicit )
Pure iterative method no recursion
Code
'''
URL := https://leetcode.com/problems/first-unique-number/description/
1429. First Unique Number
'''
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.ptr = 0
        self.vals = nums
        self.freqMap = dict()
        for num in nums:
            if(num not in self.freqMap):
                self.freqMap[num] = 0
            self.freqMap[num] = self.freqMap[num] + 1

    def showFirstUnique(self) -> int:
        firstUniq = -1
        n = len(self.vals)
        while(self.ptr < n):
            curEl = self.vals[self.ptr]
            # brackets operator facilitates fast k-v lookups in Python3
            curFreq = self.freqMap[curEl]
            if(curFreq == 1):
                firstUniq = curEl
                break
            self.ptr = self.ptr + 1
        return firstUniq

    # modify both our frequency hashmap and out underlying list of values
    def add(self, value: int) -> None:
        if(value not in self.freqMap):
            self.freqMap[value] = 0
        nextFreq = self.freqMap[value] + 1
        self.freqMap[value] = nextFreq
        self.vals.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
