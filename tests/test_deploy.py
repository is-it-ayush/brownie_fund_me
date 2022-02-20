from brownie import FundMe, accounts, network

def test_deploy():
    # Act
    account = get_account()
    # Arrange
    fund_me = FundMe.deploy({"from":account}, publish_source=True)
    print(f"[Contract] Contract Deployed to {fund_me.address}")


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.load("test_account")

