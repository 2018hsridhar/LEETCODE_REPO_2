'''
URL := https://leetcode.com/problems/best-team-with-no-conflicts/
1626. Best Team With No Conflicts

Category : DP, Linear Pass, Caching

Complexity
Let N := #-scores
Time := O(N^2)
Space := O(N) ( E ) O(1) ( I ) 

25 minutes

'''
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        bts = 0
        # Leverage list comprehension : compose lsits from pre-existing lists.
        createdTuple = [[scores[i],ages[i]] for i in range(len(scores))]
        # the sort has to be () EXPR encapsulated too
        createdTuple.sort(key=lambda pair : (pair[1], pair[0]))
        # print(createdTuple)
        # dict() memos over array[] memos always easier to mem-init
        # '-1' useful for debug ( versus 0 => more error prone in future debug )
        memo = [-1 for i in range(len(scores))]
        for index in range(len(scores) - 1,-1,-1):            
            curSubProblemScore = createdTuple[index][0]
            localProblemScore = curSubProblemScore
            curSubProblemAge = createdTuple[index][1]
            for j in range(index+1,len(scores),1):
                otherSubProblemScore = createdTuple[j][0]
                otherSubProblemAge = createdTuple[j][1]
                if (curSubProblemAge < otherSubProblemAge and curSubProblemScore <= otherSubProblemScore) or (curSubProblemAge == otherSubProblemAge):
                    localProblemScore = max(localProblemScore, curSubProblemScore + memo[j])
            memo[index] = localProblemScore
            bts = max(bts, memo[index])
        return bts
