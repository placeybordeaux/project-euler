
struct Primes {
  primes: Vec<i32>
}

impl Primes {
  fn generate_up_to(&self, limit: i32) {
    let last = match self.primes.get(self.primes.len()-1) {
      None => panic!(":("),
      Some(l) => l
    };
    for i in *last..limit {
      for prime in self.primes {
        if let Some(p) = prime {
          if i % p == 0 {
            self.primes.push(i);
            break;
          }
        }
      }
    }
  }
}

fn main() {
  let primes = Primes{primes: vec![2,3]};
  primes.generate_up_to(5)
}
