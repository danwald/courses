fn main() {
    let th = 1000i32;
    let thu8 = th as u8;

    println!("1000 as i32: {}", th);
    println!("1000 as  u8: {} '8 LSB(1000) = 232' {} -> {}",
        th as u8,
        format!("{th:b}"),
        format!("{thu8:b}"),

    );

    let x = 1u8;
    let y = 1i32;
    let z = 1f64;
    println!("{} size is {} bytes and type", x, std::mem::size_of_val(&x));
    println!("{} size is {} bytes and type", y, std::mem::size_of_val(&y));
    println!("{} size is {} bytes and type", z, std::mem::size_of_val(&z));

    let em = 5u8;
    let em2 = 5u8;
    let mut vec = Vec::new();
    vec.push(em);
    vec.push(em2);
    println!("{:?}", vec);

    type NanoSecond = u64;
    let nano: NanoSecond = 5 as u64;
    println!("nano: {}", nano);
}
