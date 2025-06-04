'''
3527. Find the Most Common Response
URL := https://leetcode.com/problems/find-the-most-common-response/description/

'''
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        dedupeResponses = [set(response) for response in responses]
        wordFreq = dict()
        for response in dedupeResponses:
            for word in response:
                if(word not in wordFreq):
                    wordFreq[word] = 0
                wordFreq[word] += 1
        # print(wordFreq)
        sortedPairs = [[word,wordFreq] for word,wordFreq in wordFreq.items()]
        sortedPairs.sort(key = lambda x : (-1*x[1],x[0]))
        targetResp = sortedPairs[0][0]
        return targetResp
        
