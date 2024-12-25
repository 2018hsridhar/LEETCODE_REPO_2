'''
URL := https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/description/
1904. The Number of Full Rounds You Have Played

Rounds of chess, taking place each 15 minutes
First round 00:00 ( what time affixed at )?

15 minute intervals -> can a. get value closest?
Do by the hour metric ( hour as a boundary ) plus or minute ?
Past 24 hours = invalidity too 

10 mins solutioned :-)
'''
class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        numChessRounds = 0
        loginTimeVal = self.getTimeVal(loginTime)
        logoutTimeVal = self.getTimeVal(logoutTime)
        hourIn = (int)(loginTime[0:2])
        hourOut = (int)(logoutTime[0:2])
        hourInVal = (60 * hourIn)
        hourInOneVal = 60 * (hourIn + 1)
        hourOutVal = 60 * (hourOut)
        hourOutOneVal = 60 * (hourOut + 1)
        # do not double count by accident
        twentyFourVal = (24*60) - 1
        if(loginTimeVal <= logoutTimeVal):
            for candidVal in range(hourInVal, hourOutOneVal,15):
                if(loginTimeVal <= candidVal and candidVal+15 <= logoutTimeVal):
                    numChessRounds += 1
        else:
            for candidVal in range(hourInVal,twentyFourVal, 15):
                if(loginTimeVal <= candidVal):
                    numChessRounds += 1
            for candidVal in range(0,hourOutOneVal, 15):
                if(candidVal+15 <= logoutTimeVal):
                    numChessRounds += 1
        return numChessRounds
        
    def getTimeVal(self, time:str) -> int:
        hour = (int)(time[0:2])
        minute = (int)(time[3:5])
        timeVal = (60 * hour) + minute
        return timeVal
