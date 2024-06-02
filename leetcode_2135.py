'''
URL := https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/description/
2135. Count Words Obtained After Adding a Letter

Category : Binary Strings, Sets, String Manipulations

Complexity
Let M := len(startWords) and N := len(targetWords)
Time = O(MN)
Space = O(M) ( E ) O(1) ( I )

Commit log : 
(A) Such verbosity to Python3's type system
(B) Interesting set() initialization syntax in Py3
(C) enumerate(...) simplifies loops needing counters
(D)
(E)

18 mins to solutioning

'''
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        startWordBinStrings = set()
        for startWord in startWords:
            startWordBinStr = self.createBinaryString(startWord)
            startWordBinStrings.add(startWordBinStr)
        targetWordCount = 0
        for targetWord in targetWords:
            targetWordBin = self.createBinaryString(targetWord)
            for index,letter in enumerate(targetWordBin):
                if(letter == '1'):
                    leftPiece = targetWordBin[:index]
                    rightPiece = targetWordBin[index+1:]
                    evictPiece = leftPiece + '0' + rightPiece
                    if(evictPiece in startWordBinStrings):
                        targetWordCount += 1
                        break 
        return targetWordCount


    def createBinaryString(self, word:str) -> str:
        binStringArr = ["0" for i in range(26)]
        baseAlphaLetter = 'a'
        for letter in word:
            indexPos = ord(letter) - ord(baseAlphaLetter)
            binStringArr[indexPos] = "1"
        binString = "".join(binStringArr)
        return binString


        
