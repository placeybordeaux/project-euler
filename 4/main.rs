fn palindromic(n: i32) -> bool {
  let s = n.to_string().into_bytes();
  for i in 0..s.len()/2 {
    if s.get(i) != s.get(s.len() - i - 1) {
      return false;
    }
  }
  return true;
}

fn main() {
  let mut m = 0;
  for x in 100..999 {
    for y in x..999 {
      if palindromic(x*y) {
        if x*y > m {
          m = x*y;
          println!("{}", m);
        }
      }
    }
  }
  println!("done!");
}

