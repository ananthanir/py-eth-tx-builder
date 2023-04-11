from web3 import Web3
import json
from eth_account import Account

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))

with open('hardhat-vyper/details.json', 'r') as f:
    details = json.load(f)

with open('hardhat-vyper/artifacts/contracts/Cert.vy/Cert.json', 'r') as f:
    artifact = json.load(f)

contract_instance = w3.eth.contract(
    address=details['contract'], abi=artifact['abi'])
# print(contract_instance.all_functions())
# print(artifact['abi'])
print("Contract:", details['contract'])
print("Deployer:", details['deployer'])

private_key = "0x6a99f5386ad5d5f4b5c58087363ad16de601cba52e1bd3d83b40b6bd9427fb50"

account = Account.from_key(private_key)
w3.eth.default_account = account.address

_id = 101
_name = "Ananthan"
_course = "CKA"
_grade = "A"
_date = "May 20th 2023"
_document = b'123456789012345678901234567890123456789012345678'

tx = contract_instance.functions.issue(_id, _name, _course, _grade, _date, _document).build_transaction({'maxFeePerGas': 2000000000, 'maxPriorityFeePerGas': 1000000000, 'value': 0, 'nonce': w3.eth.get_transaction_count(account.address)})

# print(tx)

signed_tx = account.signTransaction(tx)

tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

print('Transaction sent:', tx_hash.hex())

# certificate = contract_instance.functions.Certificates(_id).call()

# print("Certificate: ", certificate)
