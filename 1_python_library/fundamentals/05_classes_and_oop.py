#!/usr/bin/env python3
"""Classes et OOP — modéliser ordres, positions, stratégies."""

from dataclasses import dataclass
from enum import Enum


class Side(Enum):
    BUY = "BUY"
    SELL = "SELL"


@dataclass
class Order:
    """Pourquoi dataclass : ordre immuable/comparable, sérialisable vers JSON."""
    symbol: str
    side: Side
    quantity: int
    price: float

    def notional(self) -> float:
        return self.quantity * self.price


class Position:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.qty = 0
        self.avg_price = 0.0

    def apply_fill(self, side: Side, qty: int, price: float) -> None:
        signed = qty if side == Side.BUY else -qty
        new_qty = self.qty + signed
        if new_qty == 0:
            self.qty = 0
            self.avg_price = 0.0
            return
        self.avg_price = (self.avg_price * self.qty + price * signed) / new_qty
        self.qty = new_qty


if __name__ == "__main__":
    o = Order("AAPL", Side.BUY, 10, 150.0)
    print(o, "notional=", o.notional())
    pos = Position("AAPL")
    pos.apply_fill(Side.BUY, 10, 150.0)
    pos.apply_fill(Side.SELL, 5, 151.0)
    print(f"Position {pos.symbol}: qty={pos.qty}, avg={pos.avg_price:.2f}")
