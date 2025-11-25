from .protocols import amm_swap_token0_for_token1, update_lending_state
from .metrics import compute_metrics
from .state import SimulationSnapshot

def run_scenario(market_path, amm_state, lending_state, params):
    snapshots = []

    for m in market_path:
        lending_state = update_lending_state(lending_state, m, params.ltv_bps, params.liq_bps)
        amm_state, _ = amm_swap_token0_for_token1(amm_state, params.trade_size, params.fee_bps)
        metrics = compute_metrics(amm_state, lending_state, m)

        snapshots.append(SimulationSnapshot(
            t=m.time, market=m, amm=amm_state, lending=lending_state, metrics=metrics
        ))

    return snapshots
