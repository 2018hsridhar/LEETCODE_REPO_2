// use serde_json::from_str;
impl Solution {
    // Rust likes bindings : and () => empty return type
    pub fn sum_of_the_digits_of_harshad_number(x: i32) -> i32 {
        // .str = immutable view
        // bindings and mutability
        let mut digitSum = 0;
        let RADIX = 10;
        for c in x.to_string().chars() {
            // print(type(c));
            // let my_digit = from_str::<32>(c);
            // digitSum += my_digit;
            // unwrap() versus unwrap_or(...)?
            let my_digit = c.to_digit(RADIX).unwrap_or(0);
            // WTF is c.to_diigt(...) Optiona<u32>
            digitSum = digitSum + (my_digit as i32);
        }
        // print!("Digit sum %{digitSum}");
        let mut status = -1;
        if(x % digitSum == 0){
            status = (digitSum as i32);
        }
        return status;
    }
}
