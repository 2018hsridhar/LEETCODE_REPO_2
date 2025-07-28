'''
URL := https://leetcode.com/problems/pour-water-between-buckets-to-make-water-levels-equal/description/
2137. Pour Water Between Buckets to Make Water Levels Equal

Epsilon needed
'''
class Solution:
    def equalizeWater(self, buckets: List[int], loss: int) -> float:
        sumWater = sum(buckets)
        buckets.sort()
        low = 0
        high = sumWater
        maxWater = 0
        epsilon = 0.000001
        while(low <= high):
            mid = (low + high) / 2
            underfill = 0
            overfill = 0
            for bucket in buckets:
                if(bucket < mid):
                    underfill += abs(mid - bucket)
                elif(bucket > mid):
                    overfill += abs(bucket - mid)
            notLoss = 100 - loss
            remain = (overfill * notLoss) / 100
            # SMH at this epsilon
            if(remain >= underfill):
                maxWater = mid
                low = mid + epsilon
            elif(remain < underfill):
                high = mid - epsilon
        return maxWater

        
