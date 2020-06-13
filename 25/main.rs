#![feature(generators, generator_trait)]

extern crate num_bigint;
extern crate num_traits;

use std::ops::{Generator, GeneratorState};
use std::pin::Pin;
use num_bigint::BigUint;
use num_traits::{Zero, One};

fn main() {
    let mut generator = || {
        yield One::one();
        let mut fib: (BigUint, BigUint) = (One::one(), One::one());
        while true {
            fib = (fib.1, fib.0 + fib.1);
            yield fib.0;
        }
    };
    for i in 1..1000 {
        let p = Pin::new(&mut generator).resume();
        match p {
            GeneratorState::Yielded(f) => {
                if f > 10_u128.pow(1000) {
                    println!("{:?}", p);
                    println!("{:?}", i);
                    break;
                }
            }
            _ => {
                continue
            }
        }
    }
}
