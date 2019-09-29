use std::fs::File;
use std::io::prelude::*;

const chain: usize = 13;

fn main() -> std::io::Result<()>{
    let mut file = File::open("input.txt")?;
    let mut contents = String::new();
    file.read_to_string(&mut contents)?;
    let N = contents.find('\n').expect("no newlines");
    let M = contents.matches('\n').count();
    let mut grid_raw = vec![0; N * M];

    // Vector of 'width' elements slices
    let mut grid_base: Vec<_> = grid_raw.as_mut_slice().chunks_mut(N).collect();

    // Final 2d array
    let grid: &mut [&mut [u64]] = grid_base.as_mut_slice();

    for (m, line) in contents.lines().enumerate() {
        for (n, character) in line.chars().enumerate() {
            grid[m][n] = character.to_digit(10).expect("wtf") as u64;
        }
    }
    let mut candidates : Vec<Option<u64>> = Vec::new();
    for m in (0..grid.len()) {
        for n in (0..grid[m].len()) {
            candidates.push(across(grid, m, n));
            candidates.push(down(grid, m, n));
            //candidates.push(diagonal(grid, m, n));
            //candidates.push(other_diagonal(grid, m, n));
        }
    }
    let largest = candidates.iter().flat_map(|x| x).fold(&u64::min_value(), |a, b| a.max(b));
    println!("{:?}", largest);
    Ok(())
}

fn across(grid: &mut [&mut [u64]], m: usize, n: usize) -> Option<u64> {
    let mut t : Vec<Option<&u64>> = Vec::new();
    for i in (0..chain) {
        match grid.get(m) {
            Some(x) => t.push(x.get(n + i)),
            None => t.push(None)
        }
    }
    if t.iter().all(|x| x.is_some()) {
        let product = t.iter().flat_map(|x| *x).fold(1 as u64, |a, b| a * b);
        return Some(product);
    }
    return None;
}

fn down(grid: &mut [&mut [u64]], m: usize, n: usize) -> Option<u64> {
    let mut t : Vec<Option<&u64>> = Vec::new();
    for i in (0..chain) {
        match grid.get(m + i) {
            Some(x) => t.push(x.get(n)),
            None => t.push(None)
        }
    }
    if t.iter().all(|x| x.is_some()) {
        let product = t.iter().flat_map(|x| *x).fold(1 as u64, |a, b| a * b);
        return Some(product);
    }
    return None;
}

fn diagonal(grid: &mut [&mut [u64]], m: usize, n: usize) -> Option<u64> {
    let mut t : Vec<Option<&u64>> = Vec::new();
    for i in (0..chain) {
        match grid.get(m + i) {
            Some(x) => t.push(x.get(n + i)),
            None => t.push(None)
        }
    }
    if t.iter().all(|x| x.is_some()) {
        let product = t.iter().flat_map(|x| *x).fold(1 as u64, |a, b| a * b);
        return Some(product);
    }
    return None;
}

fn other_diagonal(grid: &mut [&mut [u64]], m: usize, n: usize) -> Option<u64> {
    let mut t : Vec<Option<&u64>> = Vec::new();
    for i in (0..chain) {
        match grid.get(m.checked_sub(i)?) {
            Some(x) => t.push(x.get(n.checked_sub(i)?)),
            None => t.push(None)
        }
    }
    if t.iter().all(|x| x.is_some()) {
        let product = t.iter().flat_map(|x| *x).fold(1 as u64, |a, b| a * b);
        return Some(product);
    }
    return None;
}
