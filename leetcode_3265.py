'''
URL := https://leetcode.com/problems/count-almost-equal-pairs-i/description/
3265. Count Almost Equal Pairs I

Well boudned : 100000 = max value ( in array ) 
pow(N,2)*0.5 ish pairs : for 6, about 20 pairings
    Can set up a set : ask ourselves if nmber is in set ( and how frequently ) 
    just don't visit the same number again after a swap operation ( e..g swp(1,5) = swp(2,4) ) type of thing

Oh : at most one operation ( or exactly equal ) 
Case str len = 1 or strlen > 1, but inside -> execute ( e.g. 12,12,12)

[1, 1, 3, 5, 5, 5, 5, 5, 5, 5, 8, 10, 10]


'''
class Solution:
    def countPairs(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        numFreq = dict()
        for num in nums:
            if(num not in numFreq):
                numFreq[num] = 0
            numFreq[num] += 1
        numAlmostPairs = 0
        # Correct, but be pairwise : (i,j) and (j,i) matching -> 
        visitedPairs = set()
        for num in nums:
            strVersion = (str)(num)
            # Each pairwise swap doable here
            for i in range(len(strVersion)):
                visited = set()
                # if a value to swap
                if(len(strVersion) >= 2):
                    for j in range(i+1,len(strVersion), 1):
                        # print("(i,j) = (%s,%s)" %(i,j))
                        swpNumArr = list(strVersion)
                        temp = swpNumArr[i]
                        swpNumArr[i] = swpNumArr[j]
                        swpNumArr[j] = temp
                        swpNum = (int)("".join(swpNumArr))
                        if(swpNum not in visited):
                            visited.add(swpNum)
                            if(swpNum in numFreq):
                                lowerNum = min(num,swpNum)
                                upperNum = max(num,swpNum)
                                curPair = (str)(lowerNum) + ":" + (str)(upperNum)
                                if(curPair not in visitedPairs):
                                    visitedPairs.add(curPair)
                                    if(swpNum == num):
                                        curFreq = (int)(numFreq[swpNum] * (numFreq[swpNum] -1 ) * 0.5)
                                        numAlmostPairs += curFreq
                                    else:
                                        curFreq = numFreq[swpNum] * numFreq[num]
                                        numAlmostPairs += (curFreq)
                # case len = 1 or equal
                freqNum = numFreq[num]
                samePair = (str)(num) + ":" + (str)(num)
                if(samePair not in visitedPairs):
                    visitedPairs.add(samePair)
                    numAlmostPairs += (int)(freqNum * (freqNum - 1) * 0.5)
        return numAlmostPairs

