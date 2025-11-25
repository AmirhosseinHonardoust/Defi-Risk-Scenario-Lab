# **DeFi-Risk-Scenario-Lab**

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Solidity-0.8.20-black?style=for-the-badge&logo=solidity&logoColor=white">
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Contributions-Welcome-orange?style=for-the-badge">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/DeFi-Simulation-blueviolet?style=for-the-badge&logo=ethereum">
  <img src="https://img.shields.io/badge/Risk-Modeling-critical?style=for-the-badge">
  <img src="https://img.shields.io/badge/Smart--Contracts-Research-important?style=for-the-badge">
</p>

### *A Research-Grade Environment for Stress-Testing DeFi Protocols with Solidity Mini-Systems + Python Simulation Engine + Streamlit Visualization*

---

## **Executive Summary**

**DeFi-Risk-Scenario-Lab** is a full-stack analytical environment designed to **simulate, visualize, and explain the behavior of DeFi protocols under market stress**.

It integrates:

* **Miniature Solidity protocol implementations** (AMM, lending pool, yield system)
* **A Python simulation backend** modeling price crashes, liquidity dynamics, and liquidation cascades
* **A Streamlit dashboard** for real-time scenario exploration and visualization
* **Quantitative risk metrics**: pool value, protocol equity, position health, and cascading effects

This lab is intentionally designed for:

* **DeFi protocol architects** exploring parameter sensitivities
* **Smart-contract security researchers** analyzing failure modes
* **Financial engineers** performing scenario & stress testing
* **Data scientists** modeling systemic risks in on-chain economies

It serves as a *sandbox for understanding risk propagation*, not as a production DeFi system.

---

# **Why This Lab Exists**

DeFi protocols, despite being autonomous and deterministic, remain vulnerable to:

* market shocks
* liquidity fragmentation
* leverage spirals
* oracle-dependent liquidation loops
* fee misconfigurations
* AMM inventory risk
* cross-protocol contagion

Traditional DeFi audits focus on **code correctness**, not **economic correctness**.
This lab fills that gap by simulating:

### *“What happens to protocol state when the market breaks?”*

Examples this lab answers:

* How fast does an AMM’s value deteriorate during a crash?
* At what volatility levels does a lending pool enter liquidation spiral?
* What parameter combinations (LTV, fees) create instability?
* How do swap flows interact with falling collateral prices?

The two figures you generated are the *first outputs of this investigation*.

---

## **Project Architecture**

```
DeFi-Risk-Scenario-Lab/
│
├── contracts/            # Solidity mini-protocols
│   ├── amm/
│   ├── lending/
│   └── yield/
│
├── simulation/           # Python simulation engine
│   ├── scenarios.py
│   ├── protocols.py
│   ├── engines.py
│   ├── metrics.py
│   └── state.py
│
├── app/
│   └── streamlit_app.py  # UI Dashboard
│
├── tests/
└── README.md
```

---

# **System Architecture**

The architecture is designed to be modular, interpretable, and extensible.

## **1. Solidity Mini-Protocols (Specification Layer)**

Lightweight smart contracts representing essential mechanics:

* **SimpleAMM.sol**

  * Uniswap v2-style x*y=k invariant
  * Configurable swap fee
  * No LP token complexity (for clarity)

* **SimpleLendingPool.sol**

  * Collateral-value-based health factor
  * LTV (loan-to-value) limits
  * Liquidation threshold
  * Deterministic liquidation logic

* **RewardFarm.sol**

  * Linear emission
  * Useful for modeling yield contraction during crashes

These contracts provide the **ground-truth rule sets** that the Python engine mirrors mathematically.

---

## **2. Python Simulation Engine (Dynamic Layer)**

The simulation engine consists of:

### **a. Market Generator**

Creates price/shock paths:

* Linear crashes
* Multi-phase dumps
* Liquidity drains (future feature)
* Volatility spikes (planned)

### **b. Protocol Mirrors**

Re-implement Solidity logic in Python for speed:

* AMM swaps adjust reserve state each timestep
* Lending pool health evaluated continuously
* Liquidations executed deterministically

### **c. Metrics Module**

Computes:

* pool value = reserve₀ + reserve₁ × price
* protocol equity
* liquidation count
* drawdown (planned)
* impermanent loss (planned)

### **d. Snapshot Collector**

Every timestep records structured simulation state:

```
MarketState
AMMState
LendingState
Metrics
```

---

## **3. Streamlit Dashboard (Visualization Layer)**

The UI lets you:

* configure crash depth, start, horizon
* tweak LTV, liquidation threshold
* adjust AMM fee behavior
* execute simulation
* visualize how AMM value and price evolve

This turns analytical modeling into **interactive experimentation**.

---

# **Core Figures**
## **1. Price Trajectory Under Crash Scenario**

<img width="727" height="393" alt="Screenshot 2025-11-25 at 15-52-16 Streamlit" src="https://github.com/user-attachments/assets/40d05813-7247-4769-8996-abbf2e8ba01c" />

This chart shows:

* A stable price plateau during the “calm” phase
* A linear downward crash starting at timestep 10
* A final stabilization at a lower price

### **Interpretation**

This is a *controlled price crash model*, ideal for studying deterministic protocol response.
It isolates the following variables:

* **Price levels**
* **Rate of decline**
* **Crash starting point**
* **Shock duration**

This makes the scenario analytically clean and easy to interpret.

---

## **2. AMM Pool Value Response During Crash**

<img width="736" height="403" alt="Screenshot 2025-11-25 at 15-52-35 Streamlit" src="https://github.com/user-attachments/assets/b9a49b9b-85dd-4dbe-9b45-6566efe7985f" />

This chart shows:

* A stable pool value until the crash begins
* A gradual decline in AMM value as reserves rebalance
* The characteristic *impermanent loss curve* induced by volatile price movement

### **Interpretation**

This figure demonstrates several canonical AMM behaviors:

### **1. Inventory Risk**

As price melts, the pool becomes overexposed to the losing asset.

### **2. Impermanent Loss**

Even if price later stabilizes, the AMM’s reserve ratio has shifted such that:

```
Pool Value < HODL Value
```

### **3. Swap-Induced Reserve Drift**

Your simulation applies a constant trade size each timestep, modeling:

* arbitrage
* passive flow
* user swap pressure

This increases divergence between AMM and baseline value.

### **4. Deterministic Value Decay**

Because the AMM is a *function of price*, a predictable decline appears:

```
V_pool(t) = reserve₀(t) + reserve₁(t) × price(t)
```

Your simulation correctly exhibits:

* concave decay
* linear-like reserve depletion
* no sudden discontinuities (as expected from AMM math)

---

# **Mathematical Foundations**

The simulation is driven by two classical DeFi equations:

---

## **1. AMM (Uniswap v2) Constant Product Formula**

```
x * y = k
```

When a swap comes in:

```
amount_in_with_fee = amount_in × (1 – fee)
new_reserve_in  = reserve_in + amount_in_with_fee
new_reserve_out = k / new_reserve_in
amount_out      = reserve_out - new_reserve_out
```

This determines:

* price impact
* reserve composition
* pool value trajectory

---

## **2. Lending Pool Health Factor**

```
health = collateral_value / debt
```

Liquidation condition:

```
health < liquidation_threshold
  → trigger liquidation
```

In this simulation:

* liquidations reduce collateral
* reduce debt
* increment liquidation counter

Even though your current chart doesn’t show liquidations yet, the system is ready for them.

---

# **How to Run the Lab**

### **Install dependencies**

```bash
pip install streamlit
```

### **Run the dashboard**

```bash
streamlit run app/streamlit_app.py
```

Dashboard appears at:

```
http://localhost:8501
```

---

# **Next Extensions Built Into the Design**

This repo is structured for future expansion:

### Market Layer

* GBM stochastic volatility
* Flash crashes
* Multi-asset contagion

### Protocol Layer

* Leverage loops
* Cross-protocol interactions
* Oracle lag models

### Visualization Layer

* Liquidation timeline
* Health factor trajectory
* Impermanent loss curve
* AMM arbitrage efficiency

---

# **Intended Audience**

This lab is meant for:

### **DeFi Engineers**

Testing parameter sensitivity before launching mainnet protocols.

### **Security Researchers**

Understanding economic attack surfaces.

### **Quants**

Modeling deterministic stress behaviors.

### **Data Scientists**

Running reproducible simulations of on-chain risk.
