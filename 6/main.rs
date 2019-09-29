fn main() {
    let number = 100;
    let sum_of_squares = (0..(number + 1)).map(|n| n * n).fold(0, |a, b| a + b);
    let sum: i128 = (0..(number + 1)).fold(0, |a, b| a + b);
    let square_of_sum = sum.pow(2);

    println!("{}", sum_of_squares);
    println!("{}", square_of_sum);
    println!("{}", square_of_sum - sum_of_squares);
}
