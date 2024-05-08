'''
URL := https://leetcode.com/problems/finding-pairs-with-a-certain-sum/
1865. Finding Pairs With a Certain Sum

Gaaah self keyword for classes here
It really wqasn't that much more performant sadly
'''
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.mapOne = dict()
        self.mapTwo = dict()
        self.nums = nums2
        # functions of objects seen as attrributes
        self.populate(self.mapOne,nums1)
        self.populate(self.mapTwo,nums2)
    
    def populate(self, myMap: dict(), nums:int) -> None:
        for val in nums:
            if val not in myMap:
                myMap[val] = 0
            myMap[val] += 1

    # oh shit we need the original index gaaah
    def add(self, index: int, val: int) -> None:
        origVal = self.nums[index]
        replVal = origVal + val
        self.nums[index] = replVal
        self.mapTwo[origVal] -= 1
        if(self.mapTwo[origVal] == 0):
            # del keyword remove a key from a dict
            del self.mapTwo[origVal]
        if replVal not in self.mapTwo:
            self.mapTwo[replVal] = 0
        self.mapTwo[replVal] += 1

    def count(self, tot: int) -> int:
        countFreq = 0
        for key, value in self.mapOne.items():
            delta = tot - key
            if delta in self.mapTwo:
                countFreq += (self.mapTwo[delta] * self.mapOne[key])
        return countFreq
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
