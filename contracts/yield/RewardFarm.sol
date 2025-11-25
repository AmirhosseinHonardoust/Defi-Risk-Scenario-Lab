// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract RewardFarm {
    mapping(address => uint256) public stakes;
    uint256 public rewardRate;

    constructor(uint256 _rewardRate) {
        rewardRate = _rewardRate;
    }

    function stake(uint256 amount) external {
        stakes[msg.sender] += amount;
    }
}
