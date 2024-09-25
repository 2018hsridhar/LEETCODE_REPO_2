Intuition and Approach
Leveraging Binary Representation of Power
Make sure to convert inputs to a larger range : we are given INTs, but work with DOUBLES to accomodate for larger power values
Complexity
Let N := power we raise our base to.

Time complexity:
O(logN)

Space complexity:
O(1) ( Explicit and Implicit )

Code
/*
 Note that n can get very large as well
 Note that n is NOT always a positive power ( it can be a negative power as well :: signage matters sadly )
 But positive case proves easier to deal with
 X is a double : not always an integral value ( at least reaonsably bounded by (-100.0, 100.0))
 x^n will never overflow : that power is large but if x in (-1,1), x^(power) only decreases. Same at 1, else, increase outside that power radius
 
URL = https://leetcode.com/problems/powx-n/
50. Pow(x, n)

For the enegative case, just evaluate positively and then divde ( seems trivial )?

*/
class Solution 
{
    public double myPow(double x, int n) 
    {
        // Convert n to its binary representation instead ( standard LSB -> MSB fitting-in algo ) 
        double powerVal = 1;
        int numShifts = 0;
        double divisor = 2;
        double dividend = Math.abs((double)(n));
        double remainder = 0;
        double quotient = 0;
        double factor = 0;
        while(dividend > 0)
        {
            quotient = dividend / divisor;
            remainder = dividend % 2;
            if(remainder == 1)
            {
                factor = x;
                for(int i = 0; i < numShifts; ++i)
                    factor *= factor;
                powerVal *= factor;
            }
            dividend = (int)quotient;
            ++numShifts;
        }
        if(n < 0) {
            powerVal = (1 / powerVal );
        }
        return powerVal;
    }
}
