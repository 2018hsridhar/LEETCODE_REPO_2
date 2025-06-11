'''
1106. Parsing A Boolean Expression
URL := https://leetcode.com/problems/parsing-a-boolean-expression/description/

Complexity
$$N = len(input)$$
$$ T = O(N) $$
$$ S = O(N) $$ ( Exp ) 
$$ S = O(1) $$ ( Imp ) 

Bool expression -> rulesEngine with limited rule set
Leverage short-circuit eval
Never append on stack actual T/F values

20 minutes spent ( 20 mins another day ) -> closing in -> Passed -> woooh Rules Engine ( another HARD down !!! ) 
'''
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        evalResult = True
        TRUE = 't'
        FALSE = 'f'
        NOT = '!'
        AND = '&'
        OR = '|'
        INIT = ''
        stack = []
        ptr = 0
        n = len(expression)
        exprStack = []
        exprStack.append([NOT,INIT])
        NOT_MAP = {
            TRUE:False,
            FALSE:True
        }
        while(ptr < n):
            curEl = expression[ptr]
            if(curEl == NOT or curEl == AND or curEl == OR):
                exprStack.append([curEl,INIT])
                ptr += 2
            elif(curEl == TRUE or curEl == FALSE):
                topRec = exprStack[-1]
                # ahhh is this a bug ( could be ) 
                if(topRec[1] == INIT):
                    topRec[1] = curEl
                    if(topRec[0] == NOT and curEl == TRUE):
                        topRec[1] = FALSE
                    elif(topRec[0] == NOT and curEl == FALSE):
                        topRec[1] = TRUE
                else:
                    # short-circuit evals
                    if(topRec[0] == AND and curEl == FALSE):
                        topRec[1] = FALSE
                    elif(topRec[0] == OR and curEl == TRUE):
                        topRec[1] = TRUE
                    elif(topRec[0] == NOT and curEl == TRUE):
                        topRec[1] = FALSE
                    elif(topRec[0] == NOT and curEl == FALSE):
                        topRec[1] = TRUE
                ptr += 1
            elif(curEl == ')'):
                # top Record handling case -> eval in expression
                # can we modularize here?
                curRecord = exprStack.pop()
                curEl = curRecord[1]
                nextTopRec = exprStack[-1]
                if(nextTopRec[1] == INIT):
                    nextTopRec[1] = curEl
                    if(nextTopRec[0] == NOT and curEl == TRUE):
                        nextTopRec[1] = FALSE
                    elif(nextTopRec[0] == NOT and curEl == FALSE):
                        nextTopRec[1] = TRUE
                else:
                    if(nextTopRec[0] == AND and curEl == FALSE):
                        nextTopRec[1] = FALSE
                    elif(nextTopRec[0] == OR and curEl == TRUE):
                        nextTopRec[1] = TRUE
                    elif(nextTopRec[0] == NOT and curEl == TRUE):
                        nextTopRec[1] = FALSE
                    elif(nextTopRec[0] == NOT and curEl == FALSE):
                        nextTopRec[1] = TRUE 
                ptr += 1
            elif(curEl == ','):
                ptr += 1
        finalRes = exprStack.pop()
        lastState = finalRes[1]
        evalResult = NOT_MAP[lastState]
        return evalResult
