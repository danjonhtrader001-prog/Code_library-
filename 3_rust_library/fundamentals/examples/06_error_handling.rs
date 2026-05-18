//! Gestion d'erreurs — Result / Option sur données marché

use std::num::ParseFloatError;

#[derive(Debug)]
enum MarketError {
    InvalidPrice(ParseFloatError),
    NonPositive(f64),
}

fn parse_price(raw: &str) -> Result<f64, MarketError> {
    let p: f64 = raw.parse().map_err(MarketError::InvalidPrice)?;
    if p <= 0.0 {
        return Err(MarketError::NonPositive(p));
    }
    Ok(p)
}

fn last_tick(prices: &[f64]) -> Option<f64> {
    prices.last().copied()
}

fn main() {
    for raw in ["150.5", "oops", "-1"] {
        match parse_price(raw) {
            Ok(p) => println!("OK: {p}"),
            Err(e) => println!("Erreur: {e:?}"),
        }
    }
    let ticks = vec![100.0, 100.2];
    println!("Dernier tick: {:?}", last_tick(&ticks));
}
