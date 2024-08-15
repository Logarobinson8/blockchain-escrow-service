mas2
blockchain-escrow-service
A secure smart contract escrow service that releases funds only when multiple conditions are met, reducing risk in crypto trades.
#!/usr/bin/env python3
from web3 import Web3
import json

# Connect to local Ethereum node
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
escrow_owner = w3.eth.accounts[0]
buyer = w3.eth.accounts[1]
seller = w3.eth.accounts[2]

with open("Escrow.json") as f:
    contract_interface = json.load(f)

Escrow = w3.eth.contract(abi=contract_interface['abi'], bytecode=contract_interface['bytecode'])

# Deploy contract
tx_hash = Escrow.constructor(buyer, seller, 100).transact({"from": escrow_owner})
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Escrow contract deployed at:", tx_receipt.contractAddress)

# Verify contract state
escrow_instance = w3.eth.contract(address=tx_receipt.contractAddress, abi=contract_interface['abi'])
print("Escrow balance:", w3.from_wei(w3.eth.get_balance(tx_receipt.contractAddress), 'ether'))
