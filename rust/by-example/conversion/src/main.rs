use std::convert::From;
use std::convert::Into;
use std::fmt;

struct Number {
    value: i32,
}

impl fmt::Display for Number {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{}", self.value)
    }
}
impl From<i32> for Number {
    fn from(item: i32) -> Self {
        Number {value: item}
    }
}


fn main() {
    let num = Number::from(42);
    let i = 5i32;
    let n2: Number = i.into();
    println!("num:{} n2:{}", num, n2);
}
