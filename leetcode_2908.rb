# @param {Integer[]} nums
# @return {Integer}
def minimum_sum(nums)
    # Is Ruby OOP?
    # how many PLs represent infinity as a float ( Ruby does )?
    # This PL reminds me well of BASIC
    globalMin = Float::INFINITY
    foundTriplet = false
    n = nums.length()
    m = n - 1
    # for i in (0...nums.length()) do
    (0...nums.length()).each do |i|
        ((i+1)...n).each do |j|
            ((j+1)...n).each do |k|
                elOne = nums[i]
                elTwo = nums[j]
                elThree = nums[k]
                # auto add new line end of message
                # print : no desire for new line behavior
                # vals = [elOne,elTwo,elThree]
                # puts "elOne = ${nums[i]}"
                # puts "elTwo = ${nums[j]}"
                # puts "elThree = ${nums[k]}"
                # puts vals
                if elOne < elTwo && elThree < elTwo 
                    tripletSum = elOne + elTwo + elThree
                    foundTriplet = true
                    globalMin = (globalMin < tripletSum) ? globalMin : tripletSum
                    # enum = [globalMin,tripletSum]
                    # globalMin = enum.min(1) { |a, b| a<=>b }
                end
            end
        end
    end
    retVal = (foundTriplet) ? globalMin : -1
    return retVal
end
