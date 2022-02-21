import time
from brownie import network,accounts,config, MockV3Aggregator 
# from web3 import Web3 | Importing Web3 to convert MockPrice to Wei

DECIMALS=8
STARTING_VALUE = 200000000000
LOCAL_BLOCKCHAIN_ENVIRONMENTS=["development","ganache-local"]
FORKED_LOCAL_ENVIRONEMENTS=["mainnet-fork", "mainnet-fork-dev"]

# This function will return the account depending upon the network.
def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONEMENTS:
        return accounts[0]
    else:
        return accounts.load("test_account")


# Returns priceFeed depending upon the network.
def get_price_feed(mockUSD=2000):
    # Current Network Info
    print(f"[Network] Active Network is {network.show_active()}")
    # If its not development load the priceFeed from the address in brownie-config.yaml
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        # Deploy a mock if its development network.
        print(f"[Contract] The Mock Contract is being deployed.")
        # Dont deploy mock more then once. We can check this by checking the length of the MockV3Aggregator array.
        if len(MockV3Aggregator) <= 0:
            mock_v3_aggregator = MockV3Aggregator.deploy(DECIMALS,STARTING_VALUE, {"from": get_account()})
            # To Fix the "Web3 is not connected Brownie Bug."
            time.sleep(1)
        # Return price feed from the latest deployed Mock
        return MockV3Aggregator[-1].address
