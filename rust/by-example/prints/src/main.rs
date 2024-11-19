use std::fmt::{Display, Formatter, Result};

#[derive(Debug)]
struct Point2D {
    x: f64,
    y: f64,
}
impl Display for Point2D {
    fn fmt(&self, f: &mut Formatter) -> Result {
        write!(f, "({},{})", self.x, self.y)
    }
}

struct City {
    name: &'static str,
    lat: f32,
    lon: f32,
}
impl Display for City {
    fn fmt(&self, f: &mut Formatter) -> Result {
        let lac = if self.lat < 0.0 {'S'} else {'N'};
        let loc = if self.lon < 0.0 {'W'} else {'E'};
        write!(f, "{} {:.3}{} {:.3}{}", self.name, self.lat.abs(), lac, self.lon.abs(), loc)
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
    let c = City {name: "Dubai", lat: 25.276987, lon: 55.296249};
    let d = City {name: "Dublin", lat: 53.349805, lon: -6.260310};
    println!("{}", c);
    println!("{}", d);
}
