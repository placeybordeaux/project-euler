use std::fs::File;
use std::io::prelude::*;

fn main() -> std::io::Result<()>{
    let mut file = File::open("input.txt")?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    let mut numbers: Vec<u64> = Vec::new();

    for (m, line) in contents.lines().enumerate() {
        for (n, character) in line.chars().enumerate() {
            numbers.push(character.to_digit(10).expect("wtf") as u64);
        }
    }

    let candidate = numbers.windows(13)
        .map( |window|  
            window.iter().fold(1, |a,b| a * b)
        )
        .fold(u64::min_value(), |a, b| a.max(b));
    println!("{:?}", candidate);
    Ok(())
}
