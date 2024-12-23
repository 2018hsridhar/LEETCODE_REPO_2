'''
URL := https://leetcode.com/problems/high-access-employees/description/
2933. High-Access Employees

Records of employees and access times
For security reasons, ensure we LOG high-access employeees : those with 3+ accessers within a one-hour rolling period
TC should always clarify what our target time format is : military or non-military time

'''
class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        highAccessEmps = set()
        access_times.sort(key = lambda x : (x[0], self.getTime(x[1])))
        # 3+ times one hour period : it's sorted, so we check greedily and check element at index+2 position
        numAccess = 0
        for at_one, at_two in zip(access_times, access_times[2:]):
            if(at_one[0] == at_two[0]):
                timeOne = self.getTime(at_one[1])
                timeTwo = self.getTime(at_two[1])
                if(timeOne <= timeTwo):
                    delta = timeTwo - timeOne
                    if(delta < 60):
                        highAccessEmps.add(at_one[0])
        ans = list(highAccessEmps)
        return ans

    def getTime(self, date:str) -> int:
        hour = (int)(date[0:2:1])
        minute = (int)(date[2:4:1])
        twentyFourTimeVal = (60 * hour) + minute
        return twentyFourTimeVal
        
