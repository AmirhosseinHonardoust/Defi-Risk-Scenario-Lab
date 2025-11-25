from .state import MarketState

def price_crash_scenario(T, initial_price, crash_start, crash_depth):
    states = []
    for t in range(T):
        if t < crash_start:
            price = initial_price
        else:
            frac = min(1.0, (t - crash_start) / (T - crash_start))
            price = initial_price * (1 - crash_depth * frac)
        states.append(MarketState(t, price, 0.0, 0.0))
    return states
