
fn main() {
    let coins: &Vec<i32> = &vec![    1, 2, 5, 10, 20, 50, 100,200];
    println!("{:?}", can_make_change(200, coins).unwrap().len());
}

fn can_make_change(mut remaining: i32, possible_coins: &Vec<i32>) -> Option<Vec<bool>> {
    let mut the_copy = possible_coins.clone();
    let coin = the_copy.pop()?;
    let mut results: Vec<bool> = Vec::new();
    while remaining >= 0{
        let r = can_make_change(remaining, &the_copy);
        if r.is_some() {
            results.extend(r.unwrap());
        }
        remaining -= coin;
        if remaining == 0 {
            results.push(true);
        }
        if remaining < 0 {
            break;
        }
	}
    return Some(results);
}
