# Vickrey-Auction
A demo of a [vickrey auction](https://en.wikipedia.org/wiki/Vickrey_auction) fulfilled with smart contract in Solidity.
## Run the demo
### Required
- node.js & npm
- Truffle
> npm install truffle -g
- web3
> npm install web3@^0.20.0 (version could be updated)
- TestRPC
> npm install -g ethereumjs-testrpc
### Install
Download the file.
### Run
1. Setup test net (In Powershell/Terminal)
> testrpc
2. Compile & Test (In a new window of Powershell/Terminal)
(In the folder "Vickrey-Auction")
> truffle compile

(There will be some warnings.)
> truffle test

(5 tests defined in test/test.js should all pass.)
## Reference
[Truffle Doc](https://truffleframework.com/docs/truffle/overview)

[Solidity Doc](https://solidity.readthedocs.io/en/v0.4.24/index.html)
