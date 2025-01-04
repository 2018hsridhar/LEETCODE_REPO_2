'''
522. Longest Uncommon Subsequence II
URL := https://leetcode.com/problems/longest-uncommon-subsequence-ii/description/

'''
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        lus = -1
        indexHit = dict()
        for tokenIndex,token in enumerate(strs):
            startStr = ""
            strIndex = 0
            self.genSubSeqStrings(indexHit,token,startStr,strIndex,tokenIndex)
        # print(indexHit)
        for k,v in indexHit.items():
            if(len(v) == 1):
                lus = max(lus,len(k))
        return lus        

    # implicit return ( compiler-generated ) ?
    def genSubSeqStrings(self, indexHit:dict, token:str, curStr:str, strIndex:int, tokenIndex:int) -> None:
        n = len(token)
        if(strIndex == n+1):
            return
        if(curStr not in indexHit):
            indexHit[curStr] = set()
        indexHit[curStr].add(tokenIndex)
        if(strIndex < n):
            childStr = ""
            childStr2 = ""
            for let in curStr:
                childStr += let
                childStr2 += let
            # use current str Index
            childStr2 = childStr2 + token[strIndex]
            self.genSubSeqStrings(indexHit,token,childStr,strIndex+1,tokenIndex)
            self.genSubSeqStrings(indexHit,token,childStr2,strIndex+1,tokenIndex)


        
        
