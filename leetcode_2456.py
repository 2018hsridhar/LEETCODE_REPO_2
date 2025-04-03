'''
2456. Most Popular Video Creator
URL := https://leetcode.com/problems/most-popular-video-creator/

Inputs : creators and ids
ID : most viewed video ( smallest by LEX ordering ) 
Creator : highest popularity ( get all of them ) 
'''
class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        answers = []
        n = len(creators)
        creatorFreq = dict()
        creatorViewCount = dict()
        popularity = 0
        # Different videos can have the same ID : get id with highest view count ( for a creator ) 
        # hierarchy : creators -> ids(videos viewed ) -> viewCount
        for idx in range(n):
            creator = creators[idx]
            curId = ids[idx]
            view = views[idx]
            if(creator not in creatorFreq):
                creatorFreq[creator] = 0
                creatorViewCount[creator] = dict()
            creatorFreq[creator] += view
            if(curId not in creatorViewCount[creator]):
                creatorViewCount[creator][curId] = 0
            creatorViewCount[creator][curId] += view
            popularity = max(popularity, creatorFreq[creator])
        bestCreators = []
        for creator, viewCount in creatorFreq.items():
            if(viewCount == popularity):
                bestCreators.append(creator)
        for creator in bestCreators:
            viewCounts = creatorViewCount[creator]
            viewCountsArr = [[k,v] for k,v in viewCounts.items()]
            # in DESC order
            viewCountsArr.sort(key = lambda x : (-1 * x[1],x[0]))
            targetId = viewCountsArr[0][0]
            record = [creator,targetId]
            answers.append(record)
        return answers
        
