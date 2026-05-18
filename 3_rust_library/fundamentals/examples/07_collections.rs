//! Collections — HashMap pour prix, Vec pour fenêtres

use std::collections::{HashMap, VecDeque};

fn main() {
    let mut last: HashMap<&str, f64> = HashMap::new();
    last.insert("AAPL", 150.0);
    last.insert("MSFT", 300.0);

    let mut window: VecDeque<f64> = VecDeque::with_capacity(5);
    for tick in [150.0, 150.1, 150.2, 150.15, 150.3, 150.25] {
        if window.len() == 5 {
            window.pop_front();
        }
        window.push_back(tick);
    }

    println!("Prix AAPL: {}", last["AAPL"]);
    println!("Fenêtre: {:?}", window);
}
