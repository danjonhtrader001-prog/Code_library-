# Rust — Fondamentaux

Bases indispensables pour services HFT sûrs et concurrents.

| Exemple | Sujet |
|---------|--------|
| `01_variables_types` | Variables, types, mutabilité |
| `02_control_flow` | if, loop, match |
| `03_functions` | Fonctions, closures |
| `04_ownership` | Ownership, move, borrow |
| `05_structs_enums` | struct, enum, impl |
| `06_error_handling` | Result, Option, ? |
| `07_collections` | Vec, HashMap |
| `08_traits_generics` | Traits, impl générique |

## Exécution

```bash
cd fundamentals
cargo run --example 01_variables_types
# tous :
for e in examples/*.rs; do cargo run --example "$(basename "$e" .rs)"; done
```

Rust 1.70+ recommandé.
