import os
import sys

# --- Make sure project root is on sys.path ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

import streamlit as st
from simulation.scenarios import price_crash_scenario
from simulation.state import AMMState, LendingState
from simulation.engines import run_scenario


class Params:
    def __init__(self, trade_size, fee_bps, ltv_bps, liq_bps):
        self.trade_size = trade_size
        self.fee_bps = fee_bps
        self.ltv_bps = ltv_bps
        self.liq_bps = liq_bps


def main():
    st.title("DeFi Risk Scenario Lab")

    st.sidebar.header("Scenario")
    T = st.sidebar.slider("Horizon", 10, 200, 50)
    initial_price = st.sidebar.number_input("Initial Price", 0.1, 10.0, 1.0)
    crash_depth = st.sidebar.slider("Crash Depth", 0.1, 0.99, 0.7)
    crash_start = st.sidebar.slider("Crash Start", 0, T - 1, 10)

    st.sidebar.header("Protocols")
    fee_bps = st.sidebar.slider("AMM Fee (bps)", 0, 200, 30)
    ltv_bps = st.sidebar.slider("LTV (bps)", 1000, 9000, 7500)
    liq_bps = st.sidebar.slider("Liquidation Threshold (bps)", 5000, 9500, 8500)

    if st.button("Run Simulation"):
        market_path = price_crash_scenario(T, initial_price, crash_start, crash_depth)

        amm = AMMState(100000, 100000 / initial_price)
        lending = LendingState(10000, 5000, 0)

        params = Params(
            trade_size=100,
            fee_bps=fee_bps,
            ltv_bps=ltv_bps,
            liq_bps=liq_bps,
        )

        snapshots = run_scenario(market_path, amm, lending, params)

        prices = [s.market.price_base for s in snapshots]
        pool_values = [s.metrics["pool_value"] for s in snapshots]

        st.subheader("Price")
        st.line_chart(prices)

        st.subheader("Pool Value")
        st.line_chart(pool_values)


if __name__ == "__main__":
    main()
