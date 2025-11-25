from dataclasses import dataclass

@dataclass
class MarketState:
    time: int
    price_base: float
    volatility: float
    volume: float

@dataclass
class AMMState:
    reserve0: float
    reserve1: float

@dataclass
class LendingState:
    total_collateral: float
    total_debt: float
    liquidations: int

@dataclass
class SimulationSnapshot:
    t: int
    market: MarketState
    amm: AMMState
    lending: LendingState
    metrics: dict
