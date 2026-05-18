//! Contrôle de flux — signaux sur série de prix

fn signal(price: f64, threshold: f64, long: bool) -> &'static str {
    match (long, price > threshold) {
        (true, true) => "BUY",
        (false, true) => "SELL",
        _ => "HOLD",
    }
}

fn main() {
    let prices = [100.0, 100.5, 99.8, 100.2, 101.0];
    let threshold = 100.3;
    let mut long = false;

    for p in prices {
        let s = signal(*p, threshold, !long);
        if s == "BUY" {
            long = true;
        }
        if s == "SELL" {
            long = false;
        }
        println!("prix={p:.2} -> {s}");
    }
}
