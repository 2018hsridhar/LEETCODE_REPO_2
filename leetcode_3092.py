'''
URL := https://leetcode.com/problems/most-frequent-ids/description/
3092. Most Frequent IDs
'''

import heapq

class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        freqMap = dict()
        ans = []
        maxFreqRecs = []
        for idx in range(len(nums)):
            time = idx
            num = nums[idx]
            fDelta = freq[idx]
            if(num not in freqMap):
                freqMap[num] = [0,idx,num]
            curFreq = -1 * freqMap[num][0]
            nextFreq = curFreq + fDelta
            record = [-1 * nextFreq,-1 * time,num]
            nextAns = 0
            freqMap[num] = record
            # insert new record into our running heap
            # sort by decreasing freq, then decreasing time
            heapq.heappush(maxFreqRecs, record)
            while(len(maxFreqRecs) > 0):
                curRecord = heapq.heappop(maxFreqRecs)
                [curFreq,curTime,curNum] = curRecord
                # It's been zeroed out
                if(curNum not in freqMap):
                    continue
                else:
                    [baseFreq,baseTime,baseNum] = freqMap[curNum]
                    # record of interest -> push back
                    if(baseTime == curTime):
                        nextAns = -1 * baseFreq
                        heapq.heappush(maxFreqRecs,curRecord)
                        break
                    else:
                        # mismatch in records
                        continue
            ans.append(nextAns)
        return ans
