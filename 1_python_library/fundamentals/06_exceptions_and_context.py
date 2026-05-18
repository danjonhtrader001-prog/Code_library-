#!/usr/bin/env python3
"""Exceptions et context managers — robustesse sur flux marché."""

from contextlib import contextmanager


class MarketDataError(Exception):
    """Flux interrompu ou tick invalide."""


def parse_price(raw: str) -> float:
    try:
        price = float(raw)
    except ValueError as e:
        raise MarketDataError(f"Prix invalide : {raw!r}") from e
    if price <= 0:
        raise MarketDataError(f"Prix non positif : {price}")
    return price


@contextmanager
def simulated_connection(name: str):
    """Modèle de connexion : garantir fermeture (fichier, socket, DB)."""
    print(f"[{name}] connect")
    try:
        yield
    finally:
        print(f"[{name}] disconnect")


if __name__ == "__main__":
    for raw in ["150.5", "bad", "-1"]:
        try:
            print("Prix =", parse_price(raw))
        except MarketDataError as err:
            print("Erreur marché :", err)

    with simulated_connection("feed-primary"):
        print("Réception de ticks…")
