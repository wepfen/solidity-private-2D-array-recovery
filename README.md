A attempt to implement on a 2D array:

- https://www.rareskills.io/post/solidity-dynamic (nested array part)
- https://docs.soliditylang.org/en/latest/internals/layout_in_storage.html#mappings-and-dynamic-arrays

# Usage

Install the pypi packages with the `requirements.txt` file.

```bash
usage: recover2DArray.py [-h] --rpc RPC --target TARGET --slot SLOT --lines LINES
                             --columns COLUMNS

options:
  -h, --help         show this help message and exit
  --rpc RPC          RPC URL
  --target TARGET    Target contract address
  --slot SLOT        Array storage slot
  --lines LINES      Number of lines in the array
  --columns COLUMNS  Number of columns in the array
```

Recovering a 4 lines and 15 columns 2D array.

```bash
python recover2DArray.py --rpc http://127.0.0.1:8545 --target 0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512 --slot 0 --lines 4 --columns 15

[191, 6, 34, 78, 239, 45, 132, 15, 228, 192, 23, 56, 98, 150, 77]
[44, 219, 170, 84, 3, 205, 147, 0, 122, 64, 143, 17, 88, 77, 25]
[18, 199, 254, 115, 90, 13, 40, 11, 249, 157, 66, 78, 230, 188, 5]
[99, 184, 176, 33, 70, 188, 219, 14, 29, 230, 217, 48, 202, 92, 51]
```

# Testing local

To test you will need the [foundry-rs](https://book.getfoundry.sh/) toolkit.

1. Run a local blockchain with anvil :

```bash
anvil
```

2. Deploy a smart contract

```bash
forge create src/Array.sol:Nested --root contracts/ --private-key 0xac0974bec39a17e36ba4a6b4d238ff944bacb478cbed5efcae784d7bf4f2ff80 --broadcast --constructor-args "[[191, 6, 34, 78, 239, 45, 132, 15, 228, 192, 23, 56, 98, 150, 77], [44, 219, 170, 84, 3, 205, 147, 0, 122, 64, 143, 17, 88, 77, 25], [18, 199, 254, 115, 90, 13, 40, 11, 249, 157, 66, 78, 230, 188, 5], [99, 184, 176, 33, 70, 188, 219, 14, 29, 230, 217, 48, 202, 92, 51]]"
```

There is a sample code in `contracts/src/Array.sol`

3. Run the script

```bash
python recover2DArray.py --rpc http://127.0.0.1:8545 --target 0xe7f1725E7734CE288F8367e1Bb143E90bb3F0512 --slot 0 --lines 4 --columns 15
```


# TODO

- [x] Check that the script is working

- [x] Take arguments

- [x] Write a solidity script file to test in local

- [ ] Implement the script on an array with more dimensions
