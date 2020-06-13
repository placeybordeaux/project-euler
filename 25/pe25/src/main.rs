#![feature(generators, generator_trait)]

extern crate num_bigint;
extern crate num_traits;

use std::ops::{Generator, GeneratorState};
use std::pin::Pin;
use num_bigint::{BigUint, ToBigUint};
use num_traits::{One, Pow};

fn main() {
    let mut generator = || {
        yield One::one();
        let mut fib: (BigUint, BigUint) = (One::one(), One::one());
        while true {
            let t = fib.0.clone() + fib.1.clone();
            fib = (fib.1, t);
            yield fib.0;
        }
    };
    let large = Pow::pow(&ToBigUint::to_biguint(&10).unwrap(), 1000_u16);
    for i in 1..1000 {
        let p = Pin::new(&mut generator).resume();
        match p {
            GeneratorState::Yielded(f) => {
                if f > large {
                    println!("{:?}", f);
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
