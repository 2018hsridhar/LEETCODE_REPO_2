'''
URL := https://leetcode.com/problems/largest-time-for-given-digits/
949. Largest Time for Given Digits

Greedy - focus on the hour
Four digits -> go sort them
hour in between 00, 23 ... hmmm
{012} and {0-9,0-9,0-3} for hour
Or we can just brute force it anwyays?
4 indices roll 4-sided dice, but check visitation status too

T = O(1)
S = O(1)
'''
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        bestTime = ""
        startIndex = 0
        # enumeration : pairwise
        n = len(arr)
        latestTime = 0
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    for l in range(n):
                        uniqVals = {i,j,k,l}
                        if(len(uniqVals) == 4):
                            hourVal = "".join([(str)(arr[i]),(str)(arr[j])])
                            minuteVal = "".join([(str)(arr[k]),(str)(arr[l])])
                            if(self.isValidHour(hourVal) and self.isValidMinute(minuteVal)):
                                curTimeVal = self.getTimeVal(hourVal,minuteVal)
                                if(curTimeVal >= latestTime):
                                    latestTime = curTimeVal
                                    bestTime = hourVal + ":" + minuteVal
        return bestTime


    def getTimeVal(self, hour:str, minute:str) -> int:
        timeVal = (60 * (int)(hour)) + (int)(minute)
        return timeVal                                

    def isValidHour(self, input:str) -> bool:
        hourVal = (int)(input)
        return (0 <= hourVal and hourVal <= 23)

    def isValidMinute(self, input:str) -> bool:
        minVal = (int)(input)
        return (0 <= minVal and minVal <= 59)



        
