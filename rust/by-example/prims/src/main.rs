use std::fmt::{Display, Formatter, Result};
use std::mem;

#[derive(Debug)]
struct Matrix(f32, f32, f32,f32);

impl Display for Matrix {
    fn fmt(&self, f: &mut Formatter) -> Result {
        write!(f, "({},{})\n({},{})", self.0, self.1, self.2, self.3)
    }

}
fn reverse(matrix: Matrix) -> Matrix {
    Matrix(matrix.0, matrix.2, matrix.1, matrix.3)
}

fn transpose(matrix: Matrix) -> Matrix {
   reverse(matrix)
}

fn main() {
    let _int: i64 = 10000;
    let _float = 3.14f64;
    let _bool = false;
    let _tup = (1, 2, 4);
    let m = Matrix(1.1, 1.2, 2.1, 2.2);
    let mut m2: i32 = 2;
    println!("{:?}", m);
    println!("Matrix:\n{}", m);
    println!("Transpose Matrix:\n{}", transpose(m));

    let ar: [i32; 5] = [1, 2, 3, 4, 5];
    println!("{:?} size({}) len({})", ar, mem::size_of_val(&ar), ar.len());

    for i in 0..ar.len() + 1 {
        match ar.get(i) {
            Some(val) => println!("ar[{}] = {}", i, val),
            None => println!("ar[{}] = None", i),
        }
    }
    println!("m2={}", m2);
    m2 += 2;
    println!("m2={}", m2);
}
