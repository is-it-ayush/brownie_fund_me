// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

// Removing the code from the below imports and putting them in your own contract is called Flattening.
import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

contract FundMe {

    // Mapping is basically Dictionary with Key, Value Pairs
    mapping(address => uint256) public addressToAmountFunded;
    // Using funders to keep record of the adddress of people Funding to the Contract
    address[] public funders;
    // Storing the information of Owner
    address public owner;
    // Declaring Variable for Price Feed
    AggregatorV3Interface public priceFeed;

    // The value of priceFeed will be passed to contract on deployment.
    constructor(address _priceFeed) public {
        priceFeed = AggregatorV3Interface(_priceFeed);
        owner = msg.sender;
    }

    // The Funding Method: To add ether to contract.
    function fund() public payable {
        uint256 mimimumUSD = 50 * 10**18;
        require(getConversionRate(msg.value) >= mimimumUSD,"You need to spend more ETH!");
        addressToAmountFunded[msg.sender] += msg.value;
        funders.push(msg.sender);
    }

    //getVersion(): Return the PriceFeed version.
    function getVersion() public view returns (uint256) {
        return priceFeed.version();
    }

    //getPrice(): Return the current Price.
    function getPrice() public view returns (uint256) {
        (, int256 answer, , , ) = priceFeed.latestRoundData();
        return uint256(answer * 10000000000);
    }

    //getConversionRate(): Converting eth to usd.
    function getConversionRate(uint256 ethAmount) public view returns (uint256)
    {
        uint256 ethPrice = getPrice();
        uint256 ethAmountInUsd = (ethPrice * ethAmount) / 1000000000000000000;
        return ethAmountInUsd;
    }

    function getEntranceFee() public view returns(uint256) {
        uint256 minimumUSD = 50 * 10 ** 18;
        uint256 price = getPrice();
        uint256 precision = 1 * 10 ** 18;
        return (minimumUSD * precision) / price;
    }


    // Modifier: They add prerequisite code to the function. In a way, this is modifying a function.
    // Important to use _; (underscore) represents the rest of the function code.  
    modifier onlyOwner() {
        require(msg.sender == owner);
        _;
    }

    // Executing this will send all the money to the owner of the contract.
    // The fuction can only be executed by Owner because of "onlyOwner()" Modifier.
    function withdraw() public payable onlyOwner {
        msg.sender.transfer(address(this).balance);
        
        //Clearing the address stored in funders.
        for (uint256 funderIndex = 0;funderIndex < funders.length;funderIndex++) {
            address funder = funders[funderIndex];
            addressToAmountFunded[funder] = 0;
        }
        funders = new address[](0);
    }
}