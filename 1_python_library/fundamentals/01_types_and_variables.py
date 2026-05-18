#!/usr/bin/env python3
"""Types et variables — base de toute logique de stratégie."""

# Pourquoi : en HFT on manipule prix (float), quantités (int), symboles (str), flags (bool).

symbol: str = "AAPL"
price: float = 150.25
quantity: int = 100
is_active: bool = True

# Collections immuables utiles pour clés de cache (ex. paramètres de stratégie)
params: tuple[float, float] = (0.01, 0.02)  # stop, take-profit en %

print(f"Ordre : {quantity} x {symbol} @ {price} | actif={is_active}")
print(f"Paramètres (tuple immuable) : {params}")

# Opérateurs — attention aux floats pour l'argent (arrondi / décimal plus tard)
spread = 150.26 - 150.25
print(f"Spread : {spread:.4f}")
