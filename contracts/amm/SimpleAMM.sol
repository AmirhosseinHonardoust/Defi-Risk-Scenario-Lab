// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract SimpleAMM {
    address public token0;
    address public token1;
    uint256 public reserve0;
    uint256 public reserve1;
    uint256 public feeBps;

    constructor(
        address _token0,
        address _token1,
        uint256 _initial0,
        uint256 _initial1,
        uint256 _feeBps
    ) {
        token0 = _token0;
        token1 = _token1;
        reserve0 = _initial0;
        reserve1 = _initial1;
        feeBps = _feeBps;
    }

    function getAmountOut(
        uint256 amountIn,
        uint256 reserveIn,
        uint256 reserveOut
    ) public view returns (uint256) {
        uint256 amountInWithFee = amountIn * (10000 - feeBps) / 10000;
        uint256 numerator = amountInWithFee * reserveOut;
        uint256 denominator = reserveIn + amountInWithFee;
        return numerator / denominator;
    }
}
