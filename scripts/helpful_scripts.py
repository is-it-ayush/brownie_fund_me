from brownie import network,accounts,config, MockV3Aggregator


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.load("test_account")

def get_price_feed():
    print(f"[Network] Active Network is {network.show_active()}")
    if network.show_active() != "development":
        return config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        print(f"[Contract] The Mock Contract is being deployed.")
        mock_v3_aggregator = MockV3Aggregator.deploy(18,2000000000000000000000, {"from": get_account()})
        return mock_v3_aggregator.address
