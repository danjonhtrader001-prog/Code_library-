# Lockfree Queues

**Stack HFT — C++**

## Rôle

Files SPSC/MPSC entre threads market-data et exécution.

## Bibliothèques / dépendances

- `boost::lockfree`
- `moodycamel::ConcurrentQueue`

## Usage prévu dans ce dépôt

Code réutilisable, wrappers et benchmarks pour le chemin critique **market data → signal → ordre → risk**.

Voir aussi : [`../README.md`](../README.md) et [quant-finance-probability](https://github.com/danjonhtrader001-prog/quant-finance-probability).
