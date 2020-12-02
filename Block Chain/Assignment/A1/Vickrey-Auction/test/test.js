const VickreyAuction = artifacts.require("VickreyAuction");


contract('Test for Vickrey Auction', async (accounts) => {
  it("the smart contract is well inited", async () => {
     let instance = await VickreyAuction.deployed();
     let auctionIsOpen = await instance.getIsOpen.call({from: accounts[0]});
     assert.equal(auctionIsOpen.valueOf(), true, "The auction is not open normally");
  });

  it("one could bid normally", async () => {
     let instance = await VickreyAuction.deployed();
     await instance.bid.sendTransaction(50, accounts[1], {from: accounts[0], gas: 3000000});
     await instance.bid.sendTransaction(20, accounts[2], {from: accounts[0], gas: 3000000});
     await instance.bid.sendTransaction(10, accounts[3], {from: accounts[0], gas: 3000000});
     //await instance.bid.sendTransaction(1, accounts[4], {from: accounts[0], gas: 3000000});
     let countBuyers = await instance.getTotalBuyers.call({from: accounts[0]});
     assert.equal(countBuyers.valueOf(), 3, "please check function bid() or its modifiers");
  });

  it("The auction is closed here", async() => {
    let instance = await VickreyAuction.deployed();
    await instance.closeAuction.sendTransaction({from: accounts[0], gas: 3000000});
    let auctionIsclosed = await instance.getIsOpen.call({from: accounts[0]});
    assert.equal(auctionIsclosed.valueOf(), false, "The auction is not closed normally");
  });

  it("The winner and the price to pay are well found", async() => {
    let instance = await VickreyAuction.deployed();
    let result = await instance.findWinner.call({from: accounts[0]});
    assert.equal(result[0].valueOf(), accounts[1], "The address of the winner is wrong");
    assert.equal(result[1].valueOf(), 20, "The amount to pay is wrong");
  });

  it("The trade is well executed", async() => {
    let instance = await VickreyAuction.deployed();
    let balanceBefore = /*await instance.*/web3.eth.getBalance/*.call*/(accounts[0]);
    await instance.trade.sendTransaction({from: accounts[1], value: 20000000000000000000, gas: 3000000});
    let balanceCheck = /*await instance.*/web3.eth.getBalance/*.call*/(accounts[0]);
    let balance = balanceBefore.valueOf()*1 + 20000000000000000000;
    assert.equal(balanceCheck.valueOf(), balance, "There is something wrong during the transaction of ether.");
  });
});
