Intuition and Approach
Categories : Greedy, Sort, Custom Comparator, Modular Arithmetic, Type Coercion

Complexity
N:=length(input)

Time complexity:
T=O(NlgN)

Space complexity:
S=O(1)(E)O(1)(I)

Code
'''
179. Largest Number
URL := https://leetcode.com/problems/largest-number/description/
Complexity
'''
# do we need to import extraneous libraries?
# convert to strings
import math
import functools

# gaaah at usage of funct tools here
def compare(num1:str, num2:str) -> int:
    status = 0
    m = len(num1)
    n = len(num2)
    # bound = max(m,n)
    bound = math.lcm(m,n)
    ptr1 = 0
    ptr2 = 0
    # modulos have to match to their ends ( I guess ) versus the bound only
    for steps in range(bound):
        digOne = (int)(num1[ptr1])
        digTwo = (int)(num2[ptr2])
        if(digOne < digTwo):
            status = 1
            break
        elif(digOne > digTwo):
            status = -1
            break
        ptr1 = ((ptr1 + 1 ) % m)
        ptr2 = ((ptr2 + 1 ) % n)
    return status

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        largest = ""
        # goes smallest to largest here
        convNums = []
        for num in nums:
            convNums.append((str)(num))
        # target = sorted(convNums, key=functools.cmp_to_key(compare))
        convNums.sort(key=functools.cmp_to_key(compare))
        for num in convNums:
            largest += num
        # and all zeros case SMH
        isAllZero = True
        for x in largest:
            if(x != '0'):
                isAllZero = False
                break
        if(isAllZero):
            return "0"
        return largest
