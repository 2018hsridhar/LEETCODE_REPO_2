'''
URl := https://leetcode.com/problems/fraction-addition-and-subtraction/description/
592. Fraction Addition and Subtraction

Leverage math packages :-)
https://note.nkmk.me/en/python-gcd-lcm/#python-35-or-later-mathgcd

https://stackoverflow.com/questions/2136556/in-python-how-do-i-split-a-string-and-keep-the-separators

30 minutes gaah at all the REGEXES here
'''
import re

class Solution:
    def fractionAddition(self, expression: str) -> str:
        # pattern = '+-'
        tokens = re.split('([+-])', expression)
        if(len(tokens[0]) == 0):
            tokens.pop(0)
        if(tokens[0] != '-'):
            tokens.insert(0,"+")
        startIndex = 1
        runningLCM = 1
        n = len(tokens)
        while(startIndex < n):
            operand = tokens[startIndex]
            fraction = re.split('/',operand)
            denom = int(fraction[1])
            runningLCM = math.lcm(runningLCM, denom)
            startIndex += 2
        finalDenom = runningLCM
        # calculator result
        finalNumerator = 0
        operandIndex = 1
        operatorIndex = 0
        while(operandIndex < n):
            operand = tokens[operandIndex]
            operator = tokens[operatorIndex]
            fraction = re.split('/',operand)
            numerator = int(fraction[0])
            denominator = int(fraction[1])
            scalar = runningLCM / denominator
            toAddVal = numerator * scalar
            if(operator == "+"):
                finalNumerator += toAddVal
            if(operator == "-"):
                finalNumerator -= toAddVal
            operandIndex += 2
            operatorIndex += 2
        finalDenominator = runningLCM
        finalGCD = math.gcd((int)(finalNumerator), int(finalDenominator))
        reducedNum = str(int(finalNumerator / finalGCD))
        reducedDen = str(int(finalDenominator / finalGCD))
        return "".join([reducedNum, "/", reducedDen])

        
