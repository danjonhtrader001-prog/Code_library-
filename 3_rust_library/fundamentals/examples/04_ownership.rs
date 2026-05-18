//! Ownership — éviter copies inutiles sur gros flux de messages

struct Order {
    symbol: String,
    qty: i64,
    price: f64,
}

fn notional(o: &Order) -> f64 {
    o.qty as f64 * o.price // emprunt immuable, pas de copie du String
}

fn take_owner(o: Order) -> f64 {
    o.qty as f64 * o.price // consomme o (move)
}

fn main() {
    let o = Order {
        symbol: "AAPL".into(),
        qty: 10,
        price: 150.0,
    };
    println!("Notional (ref): {}", notional(&o));
    println!("Symbole encore valide: {}", o.symbol);
    let n = take_owner(o);
    println!("Notional (owned): {n}");
    // o n'est plus accessible ici — sécurité compile-time
}
