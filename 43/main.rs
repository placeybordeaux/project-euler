fn main() {
    let v = 0..10;
    println!("{:?}", v);
    for perm in &v.Permutations {
        println!("{:?}", perm);
    }

}
