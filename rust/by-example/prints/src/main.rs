use std::fmt;

#[derive(Debug)]
struct Point2D {
    x: f64,
    y: f64,
}
impl fmt::Display for Point2D {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "({},{})", self.x, self.y)
    }
}

fn main() {
    println!("Hello, world!");
    eprintln!("Hello, world!");
    let dan = "dan";
    println!("Hello {dan}, hello world!");
    println!("Hello {}, hello world!", "peeps");
    println!("Hello {1} {:?}, hello world!", "peeps", 2);
    let p = Point2D {y:1.4, x:2.4};
    println!("Debug Point: {:?}", p);
    println!("Point: {}", p);
}
