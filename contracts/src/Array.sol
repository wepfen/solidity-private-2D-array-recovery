// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.28;

contract Nested {
	uint256[][] array;
	
	constructor(uint256[][] memory initialGrid) {
        array = initialGrid;
    }
}
