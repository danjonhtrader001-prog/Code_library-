//! Fonctions et closures — mid, PnL, agrégations

fn mid_price(bid: f64, ask: f64) -> f64 {
    (bid + ask) / 2.0
}

fn pnl_long(entry: f64, exit: f64, qty: i64) -> f64 {
    (exit - entry) * qty as f64
}

fn main() {
    let prices = vec![100.0, 100.5, 101.0];
    let sum: f64 = prices.iter().copied().sum();
    let avg = sum / prices.len() as f64;

    let apply_fee = |x: f64| x - 0.01;
    println!("Mid: {}", mid_price(99.9, 100.1));
    println!("PnL: {}", pnl_long(100.0, 101.5, 50));
    println!("Moyenne: {:.2} | après frais: {:.2}", avg, apply_fee(avg));
}
