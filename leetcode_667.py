'''
URL := https://leetcode.com/problems/beautiful-arrangement-ii/description/
667. Beautiful Arrangement II

Greedy, Sorting, Linear Scan
'''
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        answer = []
        maxValFromOne = 1 + k
        # gaaah naming system 
        step = True
        # always start at a one here
        curVal = 1
        delta = k
        answer.append(curVal)
        i = 0
        while(i < k):
            if(step):
                curVal = curVal + delta
                delta -= 1
                # woooh `not` operator as native language syntax
                step = not step
            else:
                curVal = curVal - delta
                delta -= 1
                step = not step
            answer.append(curVal)
            i += 1
        # Fill in rest of values up till n
        step = maxValFromOne + 1
        i += 1
        while(i < n):
            answer.append(step)
            step += 1
            i += 1
        return answer
