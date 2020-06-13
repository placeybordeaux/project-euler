fn main() {
    let mut n = 0;
    let mut step = 2;
    let mut times_in_step = 0;
    let mut sum = 0;
    let end = 1001_i32.pow(2);
    println!("{}", end);
    for i in 1..(end + 1) {
        if n == 0 {
            n = step;
            times_in_step += 1;
            if (times_in_step) == 4 {
                times_in_step = 0;
                step += 2;
            }
            sum += i;
        }
        n -= 1;
    }
    println!("{}", sum);
}
