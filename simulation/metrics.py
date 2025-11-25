from .state import AMMState, LendingState, MarketState

def compute_metrics(amm: AMMState, lending: LendingState, market: MarketState):
    pool_value = amm.reserve0 + amm.reserve1 * market.price_base
    protocol_equity = lending.total_collateral * market.price_base - lending.total_debt

    return {
        "pool_value": pool_value,
        "protocol_equity": protocol_equity,
        "liquidations": lending.liquidations,
    }
