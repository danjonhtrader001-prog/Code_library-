#!/usr/bin/env python3
"""Structures de données — carnets, caches, agrégations."""

from collections import deque, defaultdict

# dict : lookup symbole → dernier prix O(1)
last_price: dict[str, float] = {"AAPL": 150.0, "MSFT": 300.0}
last_price["AAPL"] = 150.5

# deque : fenêtre glissante de ticks (taille fixe, append O(1))
tick_window: deque[float] = deque(maxlen=5)
for tick in [150.0, 150.1, 150.2, 150.15, 150.3, 150.25]:
    tick_window.append(tick)

# defaultdict : compter événements par type
event_counts: defaultdict[str, int] = defaultdict(int)
for event in ["trade", "quote", "trade", "trade", "quote"]:
    event_counts[event] += 1

# set : symboles actifs sans doublon
universe = {"AAPL", "MSFT", "GOOG"}
universe.add("AAPL")

print("Prix :", last_price)
print("Fenêtre ticks :", list(tick_window))
print("Événements :", dict(event_counts))
print("Univers :", universe)
