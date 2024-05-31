'''
URL := https://leetcode.com/problems/basic-calculator-ii/description/
227. Basic Calculator II

Category : Stack, Array, Operands and Operations, Math

Complexity :
Let N := #-operands and #-operators combinewd
Time = O(N)
Space = O(N) ( E ) O(1) ( I ) 

Commit Log :
    1. So much (string,integer) casting taking place here
    2. Set literal notation is older Python, but good when working with a short list of default values
    3. Why is reasoning on the REGEXP harder? Probably regexps aren't as encountered : \D for non-digit
'''
class Solution:
    def calculate(self, s: str) -> int:
        # https://stackoverflow.com/questions/17373161/use-curly-braces-to-initialize-a-set-in-python
        mdSet = {"*", "/"}
        asSet = {"+", "-"}
        opsSet = {"*", "/", "+", "-"}
        # https://stackoverflow.com/questions/8113782/split-string-on-whitespace-in-python
        # split on space -> then on operators
        # tokens = s.split("+-/*\s++")
        # gaaah need for encapsulation here why
        # targetPattern = '[\\s+\+\-\*\/]'
        # targetPattern = '[\\s+(\D)]'
        spacePattern = "\\s+"
        spacesRemoved = "".join(re.split(spacePattern,s))
        tokens = re.split(r"(\D+)",spacesRemoved)
        # print(tokens)
        # return 0
        evalStack = []
        # first pass : evaluate multiplication and divsiion
        for token in tokens:
            if(len(evalStack) == 0 or token in opsSet):
                evalStack.append(token)
            else:
                # execute checks based on token type
                if token not in opsSet:
                    if(len(evalStack) >= 2):
                        operatorEl = evalStack.pop()
                        leftOperand = evalStack.pop()
                        if(operatorEl in mdSet):
                            computedVal = 1
                            if(operatorEl == "*"):
                                computedVal = int(leftOperand) * int(token)
                            elif(operatorEl == "/"):
                                computedVal = int(int(leftOperand) / int(token))
                            evalStack.append(str(computedVal))
                        else:
                            evalStack.append(leftOperand)
                            evalStack.append(operatorEl)
                            evalStack.append(token)
        # second pass : evaluate addition and subtraction
        finalVal = int(evalStack[0])
        for opIndex in range(1,len(evalStack),2):
            operator = evalStack[opIndex]
            rightOp = evalStack[opIndex+1]
            if(operator == "+"):
                finalVal += int(rightOp)
            elif(operator == "-"):
                finalVal -= int(rightOp)
        return finalVal        
