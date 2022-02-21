import time
from brownie import FundMe, accounts, network, config
from .helpful_scripts import get_account, get_price_feed

def deploy_fund_me():
    # Getting the account.
    account = get_account()
    
    # Deploying Contract with publish_source fetched from brownie-config.yaml
    # We also need to pass the priceFeed address to FundMe.sol
    fund_me = FundMe.deploy(get_price_feed(),{"from":account}, publish_source=config["networks"][network.show_active()].get("verify"))
    
    # To fix "Web3 Not Connected Bug"
    time.sleep(1)
    
    print(f"[Contract] Contract Deployed to {fund_me.address}")
    return fund_me

def main():
    deploy_fund_me()



