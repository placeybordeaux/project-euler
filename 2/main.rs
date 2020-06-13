fn main() {
  let mut old = 1;
  let mut curr = 1;
  let mut sum = 0;
  while curr < 4000000 {
    let tmp = old + curr;
    old = curr;
    curr = tmp;
    sum += if curr % 2 == 0 { curr } else { 0 }
  }
  print!("{}", sum)
}
