# Redis

**Stack HFT — Rust**

## Rôle

État partagé : positions, PnL intraday, circuit breakers.

## Bibliothèques / dépendances

- `redis`
- `deadpool-redis`

## Usage prévu dans ce dépôt

Code réutilisable, wrappers et benchmarks pour le chemin critique **market data → signal → ordre → risk**.

Voir aussi : [`../README.md`](../README.md) et [quant-finance-probability](https://github.com/danjonhtrader001-prog/quant-finance-probability).
