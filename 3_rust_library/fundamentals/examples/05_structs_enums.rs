//! Structs et enums — modéliser ordres et côtés

#[derive(Debug, Clone, Copy)]
enum Side {
    Buy,
    Sell,
}

#[derive(Debug)]
struct Order {
    symbol: String,
    side: Side,
    qty: i64,
    price: f64,
}

impl Order {
    fn notional(&self) -> f64 {
        self.qty as f64 * self.price
    }
}

fn main() {
    let o = Order {
        symbol: "MSFT".into(),
        side: Side::Buy,
        qty: 5,
        price: 300.0,
    };
    println!("{:?} notional={:.2}", o, o.notional());
}
