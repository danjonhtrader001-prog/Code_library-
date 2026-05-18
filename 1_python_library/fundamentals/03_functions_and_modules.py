#!/usr/bin/env python3
"""Fonctions et modularité — factoriser calculs de risque / PnL."""

from typing import Iterable


def mid_price(bid: float, ask: float) -> float:
    """Prix médian du carnet — référence pour ordres limite."""
    return (bid + ask) / 2.0


def pnl_long(entry: float, exit_price: float, qty: int) -> float:
    return (exit_price - entry) * qty


def average_fill(prices: Iterable[float], sizes: Iterable[int]) -> float:
    """Prix moyen pondéré (VWAP simplifié sur quelques fills)."""
    num = sum(p * s for p, s in zip(prices, sizes))
    den = sum(sizes)
    return num / den if den else 0.0


if __name__ == "__main__":
    print("Mid :", mid_price(99.9, 100.1))
    print("PnL :", pnl_long(100.0, 101.5, 50))
    print("VWAP:", average_fill([100, 100.5, 101], [10, 20, 5]))
