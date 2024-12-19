'''
2559. Count Vowel Strings in Ranges

'''
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        vowelStrCount = [0 for idx in range(len(words))]
        runVowelStrCount = 0
        for idx,word in enumerate(words):
            if(self.meetsCond(word)):
                runVowelStrCount += 1
            vowelStrCount[idx] = runVowelStrCount
        ans = [0 for idx in range(len(queries))]
        for idx,query in enumerate(queries):
            [left,right] = query
            numVowelStr = vowelStrCount[right]
            if(left - 1 >= 0):
                 numVowelStr -= vowelStrCount[left-1]
            ans[idx] = numVowelStr
        return ans

    # Python enables rapid dev and prototyping of code
    def meetsCond(self, word:str) -> bool:
        firstLetter = word[0]
        lastLetter = word[-1]
        vowelSet = {'a','e','i','o','u'}
        isVowelFirst = firstLetter in vowelSet
        isVowelLast = lastLetter in vowelSet
        return (isVowelFirst and isVowelLast)

                

        
