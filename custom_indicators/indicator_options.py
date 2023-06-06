from dataclasses import dataclass


@dataclass
class OptionsVisualizer():
    lookback: int = 365
    alpha_period: int = 30,
    adr_length: int = 14


@dataclass
class OptionsRollingRisk():
    lookback: int = 30
