'''
URL := https://leetcode.com/problems/make-number-of-distinct-characters-equal/description/
2531. Make Number of Distinct Characters Equal

Categories : Hash Table, Single Passes, Strings, Frequency Counting

Complexity
Let M := len(word1), N := len(word2)
T = O(M+N)
S = O(1) ( E ) O(1) ( I ) 

Commit Log Message :
    # Save on num chars with `str`
    # save on no need to type return statements
    # .items() for iterable hashmap as enumeration trick
    # Sigma Bounding on maps
    # Gaaha map not defined errors

20 mins to solutioning here
'''
class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        iip = False
        map1 = dict()
        map2 = dict()
        self.populateMap(map1,word1)
        self.populateMap(map2,word2)
        iip |= self.checkStatus(map1,map2)
        print(iip)
        iip |= self.checkStatus(map2,map1)
        print(iip)
        return iip

    def checkStatus(self, map1:dict, map2:dict) -> bool:
        iipStatus = False
        # make sure distances are reset to original values
        distCharOne = len(map1)
        distCharTwo = len(map2)
        for charOne, charOneFreq in map1.items():
            for charTwo, charTwoFreq in map2.items():
                # remove from first, add to second thinking
                # print(charOne)
                # print(charTwo)
                if(charOne != charTwo):
                    if charOne not in map2:
                        distCharTwo += 1
                    if charOneFreq == 1:
                        distCharOne -= 1
                    # remove from second, add to first
                    if charTwo not in map1:
                        distCharOne += 1
                    if charTwoFreq == 1:
                        distCharTwo -= 1
                    # print(distCharOne)
                    # print(distCharTwo)
                    if(distCharOne == distCharTwo):
                        iipStatus = True
                        return iipStatus
                    # reset original distances again
                    distCharOne = len(map1)
                    distCharTwo = len(map2)
                elif(charOne == charTwo):
                    if(distCharOne == distCharTwo):
                        iipStatus = True
                        return iipStatus
        return iipStatus

    def populateMap(self, targetMap:dict, word:str) -> None:
        for char in word:
            if char not in targetMap:
                targetMap[char] = 0
            targetMap[char] += 1
