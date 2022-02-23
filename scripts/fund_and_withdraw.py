from brownie import FundMe, accounts
from .helpful_scripts import get_account

def fund():
    # To get the latest deployed contract. (for latest entrace fee)
    fund_me = FundMe[-1]
    # Geting the account (depending on network)
    account = get_account()
    # Getting the entrance fee from within the contract.
    entrance_fee = fund_me.getEntranceFee()
    # Writing Info on Console
    print(f'[Info] The Current Entry Fee is {entrance_fee}')
    print("[Info] Funding!")
    # Funding from account (which called) with entrance fee.
    fund_me.fund({"from":account, "value": entrance_fee})

def withdraw():
    # Getting the latest deployed contract (for latest entrace fee)
    fund_me = FundMe[-1]
    # Getting the account. (depending on network)
    account = get_account()
    # Calling the withdraw function in the contract.
    fund_me.withdraw({"from":account})

def main():
    # Calling both fund and withdraw.
    fund()
    withdraw()