//! Types et variables — ticks, symboles, flags

fn main() {
    let symbol: &str = "AAPL";
    let mut price: f64 = 150.25;
    let quantity: i64 = 100;
    let is_active: bool = true;

    price += 0.10; // mutabilité explicite

    println!(
        "Ordre: {quantity} x {symbol} @ {price:.2} | actif={is_active}"
    );
}
