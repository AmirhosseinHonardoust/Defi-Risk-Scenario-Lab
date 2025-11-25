// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract SimpleLendingPool {
    struct Position {
        uint256 collateral;
        uint256 debt;
    }

    mapping(address => Position) public positions;

    uint256 public totalCollateral;
    uint256 public totalDebt;

    uint256 public ltvBps;
    uint256 public liquidationBps;

    constructor(uint256 _ltvBps, uint256 _liquidationBps) {
        ltvBps = _ltvBps;
        liquidationBps = _liquidationBps;
    }
}
