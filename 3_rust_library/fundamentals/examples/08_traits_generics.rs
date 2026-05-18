//! Traits et génériques — abstractions réutilisables

trait Priced {
    fn price(&self) -> f64;
}

struct Quote {
    bid: f64,
    ask: f64,
}

impl Priced for Quote {
    fn price(&self) -> f64 {
        (self.bid + self.ask) / 2.0
    }
}

fn spread<T: Priced>(q: &T, other: f64) -> f64 {
    (q.price() - other).abs()
}

fn main() {
    let q = Quote {
        bid: 99.9,
        ask: 100.1,
    };
    println!("Mid: {:.4}", q.price());
    println!("Écart: {:.4}", spread(&q, 100.0));
}
