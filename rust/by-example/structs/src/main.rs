#![allow(dead_code)]
#![allow(unused_variables)]
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

fn main() {
    let name = String::from("danny");
    let age = 45;
    let person = Person {name, age};
    println!("{:?}", person);

    let pair = Pair(1,3.14);
    println!("Pair:{:?},{:?}", pair.0, pair.1);

    let tl = Point{x: 0.0, y: 5.0};
    let br = Point{x: -5.0, y: 5.0};
    println!("tl {:?}, br {:?}", tl, br);

    let rect = Rectangle{top_left: tl, bottom_right: br};
    let Pair(p1, p2) = pair;
    println!("p1: {}, p2: {}", p1, p2);
}
