impl Solution {
    pub fn difference_of_sums(n: i32, m: i32) -> i32 {
        let mut num1 = 0;
        let mut num2 = 0;
        // range syntax just like Python ( .. notation ) 
        for integer in 1..=n {
            if(integer % m == 0){
                num2 += integer;
            } else {
                num1 += integer;
            }
        }
        let result = num1 - num2;
        return result
    }
}
