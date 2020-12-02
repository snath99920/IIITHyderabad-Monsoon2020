var VickreyAuction = artifacts.require("./VickreyAuction.sol");

module.exports = function(deployer) {
  deployer.deploy(VickreyAuction, 1);
};
