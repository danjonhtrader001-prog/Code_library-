#!/usr/bin/env python3
"""Fichiers et JSON — configs de stratégie, logs structurés."""

import json
from pathlib import Path


def save_strategy_config(path: Path, config: dict) -> None:
    path.write_text(json.dumps(config, indent=2), encoding="utf-8")


def load_strategy_config(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    cfg = {
        "name": "mean_reversion_v1",
        "symbol": "AAPL",
        "max_position": 1000,
        "risk_limit_pct": 0.02,
    }
    tmp = Path("/tmp/strategy_config_demo.json")
    save_strategy_config(tmp, cfg)
    loaded = load_strategy_config(tmp)
    print("Config chargée :", loaded)
    tmp.unlink(missing_ok=True)
