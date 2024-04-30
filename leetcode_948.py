'''
948. Bag of Tokens
URL := https://leetcode.com/problems/bag-of-tokens/description/

Category : Brain Teaser, Sliding Window, Two Pointers, Linear Scanning

Complexity :;
Let N := #-tokens
T = O(N)
S = O(1) ( E & I ) 


15 mins to solutioning :-) 
'''
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        lPtr = 0
        rPtr = len(tokens) - 1
        # Check our while statement later.
        # wait what if we get a case where we attempted to go up in score - but it didn't work too?
        # idea : keep track of a running max global score as well
        curScore = 0
        maxRunScore = 0
        while(lPtr <= rPtr):
            if(power >= tokens[lPtr] and lPtr <= rPtr):
                power -= tokens[lPtr]
                curScore += 1
                lPtr += 1
            elif( power < tokens[lPtr] and curScore >= 1):
                power += tokens[rPtr]
                rPtr -= 1
                curScore -= 1
            else:
                # hit terminal state : can not increase power nor execute left players <--- problem constraint
                break
            maxRunScore = max(maxRunScore, curScore)
        return maxRunScore
