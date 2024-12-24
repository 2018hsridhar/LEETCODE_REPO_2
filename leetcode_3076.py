'''
3076. Shortest Uncommon Substring in an Array
URL := https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/description/
'''
class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        # make it initValue
        # map() in PY is a func : 2 args
        answers = []
        subStrIndices = {}
        # for each substring, store a set of indices of words it belongs too ( e.g. ab found in word 1,2,3,...)
        for wordIndex, word in enumerate(arr):
            for lPtr in range(len(word)):
                for rPtr in range(lPtr+1,len(word)+1,1):
                    subStr = word[lPtr:rPtr]
                    if(subStr not in subStrIndices):
                        subStrIndices[subStr] = set()
                    subStrIndices[subStr].add(wordIndex)
        # Oh for each word, get it's substring appearing once only
        for curWordIndex, word in enumerate(arr):
            shortestString = ''
            for lPtr in range(len(word)):
                for rPtr in range(lPtr+1,len(word)+1,1):
                    subStr = word[lPtr:rPtr]
                    # we should check, but that's ok too
                    indexList = subStrIndices[subStr]
                    if(len(indexList) == 1):
                        targetIndices = list(indexList)
                        targetIndex = targetIndices[0]
                        if(targetIndex == curWordIndex):
                            if(shortestString == ''):
                                shortestString = subStr
                            else:
                                if(len(subStr) < len(shortestString)):
                                    shortestString = subStr
                                elif(len(subStr) == len(shortestString)):
                                    if(subStr < shortestString):
                                        shortestString = subStr
            answers.append(shortestString)
        return answers
