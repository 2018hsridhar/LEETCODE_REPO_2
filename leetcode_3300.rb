Intuition
Approach
Complexity
Time complexity:
Space complexity:
Code
# @param {Integer[]} nums
# @return {Integer}

# dynamically styped scripting language ( no static typing here ) 
def getDigitSum(num)
    digSum = 0
    while(num >= 10) do
        rem = num % 10
        digSum += rem
        num = (num / 10).to_i 
    end
    digSum += num
    return digSum
end

# call methods after their definition
def min_element(nums)
    minVal = Float::INFINITY
    for num in nums do
        digitSum = getDigitSum(num)
        minVal = (digitSum < minVal) ? digitSum : minVal
    end
    return minVal
end
