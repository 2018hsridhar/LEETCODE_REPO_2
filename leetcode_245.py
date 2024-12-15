'''
URL := https://leetcode.com/problems/shortest-word-distance-iii/description/
245. Shortest Word Distance III

Shortest distance problem : get all the indices of word1 and word2
Categories : Hashmap, Binary Search, Sorting

Complexity
N := len(wordsDict)
T = O(NlgN)
S = O(N) explicit O(1) 

If word is the same : iterate over list of one of the words and get min Differences
w1 : [1,3,5,100]
w2 : [2,4,6,...]
Hmm - zipperMerge both lists ( if word differs ) but also track the id of each word and SCAN all indices again>
    SCAN is an O(N) bounded operation.
    No need to sort original Lists
    Do not need all words too
    Greedy property : [w1,(w1,w2),w1,w2,w2,(w2,w1)]
                          ---- only the deltas ( if [w1,w1,w1,w2] hone in final(w1,w2) pairing

'''
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        # there's a bound
        shortestDist = len(wordsDict) - 1
        indexCapture = dict()
        records = []
        for index, word in enumerate(wordsDict):
            if(word == word1 or word == word2):
                record = [word,index]
                records.append(record)
        for index in range(len(records) - 1):
            [wordOne,indexOne] = records[index]
            [wordTwo,indexTwo] = records[index+1]
            caseOne = (wordOne == word1 and wordTwo == word2)
            caseTwo = (wordTwo == word1 and wordOne == word2)
            if(caseOne or caseTwo):
                curDistance = abs(indexTwo - indexOne)
                shortestDist = min(shortestDist, curDistance)
        return shortestDist    
