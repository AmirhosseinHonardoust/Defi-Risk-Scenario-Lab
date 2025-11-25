from .state import AMMState, LendingState, MarketState

def amm_swap_token0_for_token1(amm: AMMState, amount_in: float, fee_bps: float):
    fee_multiplier = (10000 - fee_bps) / 10000
    amount_in_with_fee = amount_in * fee_multiplier

    new_reserve0 = amm.reserve0 + amount_in_with_fee
    k = amm.reserve0 * amm.reserve1
    new_reserve1 = k / new_reserve0
    amount_out = amm.reserve1 - new_reserve1

    return AMMState(new_reserve0, new_reserve1), amount_out


def update_lending_state(lending: LendingState, market: MarketState,
                         ltv_bps: float, liq_bps: float):

    collateral_value = lending.total_collateral * market.price_base

    if lending.total_debt == 0:
        health = 10000
    else:
        health = int(10000 * collateral_value / lending.total_debt)

    if health < liq_bps:
        liquidated = 0.3 * lending.total_debt
        lending.total_debt -= liquidated
        lending.total_collateral -= liquidated / market.price_base
        lending.liquidations += 1

    return lending
