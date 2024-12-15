'''
URL := https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/description/
1996. The Number of Weak Characters in the Game

Categories : Sorting, Greedy, Running Max, Linear Scan, Queue

Complexity
N := #-characters
T = O(NlgN)
S = O(1) ( Implicit ) O(N)( Explicit ) 
'''
class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        numWeakCharacters = 0
        properties.sort(key = lambda x : (x[0],x[1]))
        maxDefense = 0
        # note : inequality strict : carefuly : 
        # case : [5,5] vs [5,10] versus [6,7] - we want the max, but not the max for the next value
        # we can do running sum with sorts : [5,5],[5,10],[5,13] and [6,8],[6,12] thing
        # but need to ... restrict the running max defense here
        # maybe a delay queue : analyze first element and check value
        # insert in reverse order : [11,....] [10,100..1] type of thing
        delayQueue = []
        for [attack_i,defense_i] in reversed(properties):
            # [1] empty queue any record > attack_i
            while(len(delayQueue) > 0):
                firstRecord = delayQueue[0]
                [attack_j,defense_j] = firstRecord
                if(attack_j > attack_i):
                    maxDefense = max(maxDefense, defense_j)
                    del delayQueue[-1]
                else:
                    break
            # [2] Exec check
            if(maxDefense > defense_i):
                numWeakCharacters += 1
            # [3] append new record
            curRecord = [attack_i,defense_i]
            delayQueue.append(curRecord)
        return numWeakCharacters
