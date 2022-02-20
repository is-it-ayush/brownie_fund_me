from brownie import FundMe, accounts, network
from .helpful_scripts import get_account

def deploy_fund_me():
    # Getting the account.
    account = get_account()
    # Deploying Contract with publish_source=True
    fund_me = FundMe.deploy({"from":account}, publish_source=True)
    print(f"[Contract] Contract Deployed to {fund_me.address}")
    

def main():
    deploy_fund_me()

