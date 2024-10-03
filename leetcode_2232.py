Intuition and Approach
Categories : Brute Force, Arrays, Slices, Two Pointers, RegExp

Complexity
M,N:= len of both expressions on each side of +

Time complexity:
O(MN)

Space complexity:
O(MN)(E)O(1)(I)

Code
'''
2232. Minimize Result by Adding Parentheses to Expression
URL := https://leetcode.com/problems/minimize-result-by-adding-parentheses-to-expression/description/
'''
class Solution:
    def minimizeResult(self, expression: str) -> str:
        minimalResult = float('inf')
        pattern = '\+'
        terms = re.split(pattern,expression)
        termOne = terms[0]
        termTwo = terms[1]
        m = len(termOne)
        n = len(termTwo)
        minimalExpr = float('inf')
        targetExpr = ""
        for i in range(m-1,-1,-1):
            addLeftTerm = (int)(termOne[i:])
            lhsTerm = termOne[0:i]
            lhsMx = 1
            if(len(lhsTerm) > 0):
                lhsMx = (int)(lhsTerm)
            for j in range(1,n+1,1):
                addRightTerm = (int)(termTwo[:j])
                addTerm = addLeftTerm + addRightTerm
                rhsTerm = termTwo[j:]
                rhsMx = 1
                if(len(rhsTerm) > 0):
                    rhsMx = (int)(rhsTerm)
                curExprResult = lhsMx * addTerm * rhsMx
                if(curExprResult < minimalExpr):
                    minimalExpr = curExprResult
                    targetExpr = lhsTerm + "(" + (str)(addLeftTerm) + "+" + (str)(addRightTerm) + ")" + rhsTerm
        return targetExpr
