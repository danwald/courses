fn main() {
    let th = 1000i32;
    let thu8 = th as u8;

    println!("1000 as i32: {}", th);
    println!("1000 as  u8: {} '8 LSB(1000) = 232' {} -> {}",
        th as u8,
        format!("{th:b}"),
        format!("{thu8:b}"),

    );
}
