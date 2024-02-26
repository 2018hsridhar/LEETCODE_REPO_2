'''
30 mins solutioning ( gaaah feeling sleep apnea lethargy still )
Gaaah hard but got it :-)
636. Exclusive Time of Functions
URL := https://leetcode.com/problems/exclusive-time-of-functions/description/

Goal : to emulate current function execution in an evolving functino call stack
Log the func execution -> { id, started/ended, timestamp(started/ended)}

Recursive func call handling ( this is hard ) 
Exclusive time(func) = sum(each time it is called ) 

Seems hashmap based ( id each func )
Tricky question due to all the edge case handling introduced here gaaah!!!

'''
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        idETime = dict()
        funcStk = []
        # gaaah unterminated string literal here
        delim = ":"
        for i in range(len(logs)):
            log = logs[i]
            logTokens = log.split(delim)
            funcId = logTokens[0]
            if(funcId not in idETime):
                idETime[funcId] = 0
            funcStatus = logTokens[1]
            funcTime = int(logTokens[2])
            if(funcStatus == 'start'):
                if(len(funcStk) == 0):
                    # Do we always terminate a function with (-1) or another value? we should check this out too!
                    # unless we maintain an invariant at least :-)
                    funcStk.append([funcId,funcTime,-1])
                elif(len(funcStk) >= 1):
                    currExecFunc = funcStk[-1]
                    currExecFuncId = currExecFunc[0]
                    # Adjust for inclusive principle here at least
                    # But what about adding the value at least?
                    currExecFunc[2] = funcTime
                    currExecFuncTime = currExecFunc[2] - currExecFunc[1]
                    idETime[currExecFuncId] += currExecFuncTime
                    funcStk.append([funcId,funcTime,-1])
            elif(funcStatus == 'end'):
                # Remove current function stack from call and 
                # Add this time ( since it's a deletive operation )
                currExecFunc = funcStk[-1]
                funcStk.pop() # last element removal
                currExecFuncId = currExecFunc[0]
                currExecFuncTime = (funcTime - currExecFunc[1] + 1)
                idETime[currExecFuncId] += currExecFuncTime
                # Adjust existing functino underneath
                if(len(funcStk) >= 1):
                    nextExecFunc = funcStk[-1]
                    # this func has not ended; update stime though
                    if(nextExecFunc[2] == -1):
                        # next func will start 1 unit afterwards
                        nextExecFunc[1] = funcTime + 1
                    # This function ended a while ago ( so change it). Overwrite existing record as if it begins new again
                    elif(nextExecFunc[2] != -1):
                        nextExecFunc[1] = funcTime + 1
                        nextExecFunc[2] = -1
        # Flatten hashmap into array
        exclusiveTimeVals = []
        # gaaah no ability to discard keys or immediately flatten values. 
        for funcId, excTime in idETime.items():
            exclusiveTimeVals.append(excTime)
        return exclusiveTimeVals
    
# closing parantheses synta errors

        
