# Web 3.0 Tutorial
Source code for the Web 3.0 Tutorial for the course on "Distributing Trust and Blockchain"

# Usage
1. Clone the repository `git clone --recurse-submodules https://github.com/ajainuary/web3.0-tutorial-truffle.git`
2. `npm i`
3. `truffle build`
4. `truffle develop` Now you're up and running with the Truffle console
5. Now let's fire up the react client `cd client && npm i`
6. `npm start`

# Directory Structure

```
.
├── build - Used to contain ABIs for our contracts earlier but now moved to client/src/contracts
├── client - The react client which is housed in its separate repository
├── contracts - All your solidity contracts go here
├── migrations - Contains all migrations for deploying your contracts
└── test - Ignore for now
```
