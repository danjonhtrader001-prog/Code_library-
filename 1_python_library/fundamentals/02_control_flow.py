#!/usr/bin/env python3
"""Structures de contrôle — parcourir ticks, signaux, positions."""

prices = [100.0, 100.5, 99.8, 100.2, 101.0]
position = 0
threshold = 100.3

# Boucle : générer un signal simple de cassure
signals: list[str] = []
for p in prices:
    if p > threshold and position == 0:
        signals.append("BUY")
        position = 1
    elif p < threshold and position == 1:
        signals.append("SELL")
        position = 0
    else:
        signals.append("HOLD")

print("Prix   :", prices)
print("Signaux:", signals)

# Compréhension : filtrer les ticks « haussiers »
up_ticks = [p for p in prices if p >= 100.0]
print("Ticks >= 100 :", up_ticks)
