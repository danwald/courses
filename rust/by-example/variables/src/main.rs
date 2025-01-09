fn main() {

    let outer_shadow: &str = "foo";
    println!("outer_shadow:'{}'", outer_shadow);
    {
        let outer_shadow: &str = "bar";
        println!("scroped outer_shadow:'{}'", outer_shadow);
    }
    println!("outer_shadow:'{}'", outer_shadow);
}
