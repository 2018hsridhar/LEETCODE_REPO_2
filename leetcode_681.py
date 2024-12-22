'''
URL := https://leetcode.com/problems/next-closest-time/description/
681. Next Closest Time

Complexity
N := len(time)


No limit to times of use ( digit time )
BUT -- no invalid times ( and careful on 0 case too ) -> check digit formed isInBounds
hour : [0,23] and minute : [0,59] 

Brute force recursion, try out each digit, check validitiy, and get timing
20 minutes to solutioning :-)
'''
class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = []
        oldTime = []
        for let in time:
            if(let.isdigit()):
                digits.append(let)
                oldTime.append(let)
        digits.sort()
        timeIndex = 0
        newTime = []
        minTime = ["",float('inf')]
        self.getMinTime(oldTime, newTime,timeIndex, digits, minTime)
        # answer = minTime[0]
        digits = minTime[0]
        # no solution case
        if(len(digits) == 0):
            return time
        answer = digits[0] + digits[1] + ":" + digits[2] + digits[3]
        return answer

    def getMinTime(self, time:str, newTime:List[str], timeIndex:int, digits:List[str], minTime):
        if(timeIndex == 4):
            hour = newTime[0] + newTime[1]
            minute = newTime[2] + newTime[3]
            if(self.isValidHour(hour) and self.isValidMinute(minute)):
                timeValNew = self.getTimeValue(newTime)
                timeValOld = self.getTimeValue(time)
                timeValTwentyFour = self.getTimeValue(['2','3','5','9'])
                timeDelta = timeValNew - timeValOld
                if(timeValOld == timeValNew):
                    return
                if(timeValNew < timeValOld):
                    # 24 hour adjustment ( backwards and forwards ) 
                    # maybe offset of one here?
                    timeDelta = timeValNew + (timeValTwentyFour - timeValOld) + 1
                # track the smaller time delta
                if(timeDelta < minTime[1]):
                    minTime[0] = newTime
                    minTime[1] = timeDelta
        elif(timeIndex < 4):
            for digit in digits:
                childTime = newTime.copy()
                childTime.append(digit)
                self.getMinTime(time,childTime,timeIndex+1,digits,minTime)

    def getTimeValue(self, time:List[str]) -> int:
        timeVal = 0
        hour = (int)(time[0] + time[1])
        minute = (int)(time[2] + time[3])
        timeVal = (60 * hour) + minute
        return timeVal

    def isValidMinute(self, minute:str) -> bool:
        minuteVal = (int)(minute)
        return (0 <= minuteVal and minuteVal <= 59)

    def isValidHour(self, hour:str) -> bool:
        hourVal = (int)(hour)
        return (0 <= hourVal and hourVal < 24)
