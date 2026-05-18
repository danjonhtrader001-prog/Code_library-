#!/usr/bin/env python3
"""Introduction NumPy — vecteurs de prix, rendements (pont vers stack HFT)."""

import numpy as np

prices = np.array([100.0, 101.0, 100.5, 102.0, 101.5])
returns = np.diff(prices) / prices[:-1]

print("Prix    :", prices)
print("Rendements :", returns.round(6))
print("Moyenne :", returns.mean())
print("Vol (écart-type) :", returns.std())

# Masque booléen : filtrer mouvements > 0.5%
mask = returns > 0.005
print("Gros up-moves :", returns[mask])
