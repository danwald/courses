#![allow(dead_code)]
#![allow(unused_variables)]

use::std::fmt::{Display, Formatter, Result};

#[derive(Debug)]
struct Person {
    name: String,
    age: u8,
}

struct Unit;

struct Pair(i32, f32);

#[derive(Debug)]
struct Point {
    x: f32,
    y: f32,
}

struct Rectangle {
    top_left: Point,
    bottom_right: Point,
}

impl Rectangle {

    fn area(&self) -> f32 {
        let Point{x: x1, y: y1} = self.top_left;
        let Point{x: x2, y: y2} = self.bottom_right;
        ((x1 - x2) * (y1 - y2)).abs()
    }
}

impl Display for Rectangle {
    fn fmt(&self, f: &mut Formatter) -> Result {
        write!(f, "top_left: ({}, {}), bottom_right: ({}, {})", self.top_left.x, self.top_left.y, self.bottom_right.x, self.bottom_right.y)
    }
}



fn main() {
    let name = String::from("danny");
    let age = 45;
    let person = Person {name, age};
    println!("{:?}", person);

    let pair = Pair(1,3.14);
    println!("Pair:{:?},{:?}", pair.0, pair.1);

    let tl = Point{x: 0.0, y: 5.0};
    let br = Point{x: -5.0, y: -5.0};
    println!("tl {:?}, br {:?}", tl, br);

    let Pair(p1, p2) = pair;
    println!("p1: {}, p2: {}", p1, p2);

    let rect = Rectangle{top_left: tl, bottom_right: br};
    println!("{} {}^2", rect, rect.area());
}
