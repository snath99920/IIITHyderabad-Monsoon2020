const Addition = artifacts.require("./Addition.sol");

contract("Addition", accounts => {
  it("should display 5", async () => {
    const addition = await Addition.deployed();
    await addition.add(3, 2, { from: accounts[0] });
    const storedSum= await addition.sum.call();
assert.equal(storedSum, 5);
  });
});