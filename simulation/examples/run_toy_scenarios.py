from simulation.scenarios import price_crash_scenario
from simulation.state import AMMState, LendingState
from simulation.engines import run_scenario

class Params:
    trade_size = 100
    fee_bps = 30
    ltv_bps = 7500
    liq_bps = 8500

market = price_crash_scenario(50, 1.0, 10, 0.7)
amm = AMMState(100000, 100000)
lending = LendingState(10000, 5000, 0)

snaps = run_scenario(market, amm, lending, Params)

print("Simulation steps:", len(snaps))
