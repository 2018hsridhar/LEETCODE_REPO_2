Intuition
One pass, linear scan approach .

Solve the frequency of each character, using two pointers, and store frequencies in a map of cardinality = 26, which each k,v entry = (letter, frequencyOfLetter)
Recreate the better compressed output by iterating over said mapping in order
Approach
See intuition above

Complexity
Time complexity:
Let N := len(input string)
O(N)

Space complexity:
O(1) Explicit ( hashmap has 26 entries at worst : bounded by the size of our input language)
O(1) Implicit ( pure iterative method : no recursive call stacks involved )

Code
'''
URL := https://leetcode.com/problems/better-compression-of-string/description/
3167. Better Compression of String


'''
class Solution:
    def betterCompression(self, compressed: str) -> str:
        letterMap = self.createLetterMap(compressed)
        print(letterMap)
        # part 2 : construct better string
        betterCompression = self.getBetterCompressed(letterMap)
        return betterCompression
        
    def createLetterMap(self,compressed) -> dict():
        letterMap = [0 for i in range(26)]
        curLetter = ''
        curFreq = ""
        for rightPtr in range(len(compressed)):
            el = compressed[rightPtr]
            if(el.isalpha()):
                if(curLetter != ''):
                    targertIdx = ord(curLetter) - ord('a')
                    letterMap[targertIdx] += int(curFreq)
                curLetter = el
                curFreq = ""
            elif(el.isnumeric()):
                curFreq = curFreq + el
        # last alpha, curFreq value
        targertIdx = ord(curLetter) - ord('a')
        letterMap[targertIdx] += int(curFreq)
        return letterMap

    def getBetterCompressed(self, letterMap:List[int]) -> str:
        betterCompress = ""
        for idx,letFreq in enumerate(letterMap):
            if(letFreq > 0):
                betterLet = chr(ord('a') + idx)
                betterCompress += betterLet
                betterCompress += str(letFreq)
        return betterCompress
