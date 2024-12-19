enum WebEvent {
    Pageload,
    PageUnload,
    KeyPress(char),
}

type WE = WebEvent;

fn inspect(we: WE) {
    match we {
        WE::Pageload => println!("Page loaded"),
        WE::PageUnload => println!("Page unloaded"),
        WebEvent::KeyPress(c) => println!("KeyPressed '{}'",c),
    }

}

fn main() {
    let kp = WE::KeyPress('x');
    let pl = WE::Pageload;
    let pu = WE::PageUnload;
    inspect(kp);
    inspect(pu);
    inspect(pl);
}
