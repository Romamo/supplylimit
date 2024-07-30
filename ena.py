from web3 import Web3

endpoint_uri = "https://rpc.ankr.com/eth"
contract_address = "0xe39B5f5638a209c1A6b6cDFfE5d37F7Ac99fCC84"

web3 = Web3(Web3.HTTPProvider(endpoint_uri))

if not web3.is_connected():
    print("Connection failed")

# https://app.symbiotic.fi/restake/ena
with open(f"abi/{contract_address}.json") as f:
    contract_abi = f.read()

contract = web3.eth.contract(address=Web3.to_checksum_address(contract_address), abi=contract_abi)
try:
    total_supply = contract.functions.totalSupply().call()
    print(f"Total Supply: {total_supply/1e18}")
except Exception as e:
    print(f"An error occurred while fetching totalSupply: {e}")

try:
    limit = contract.functions.limit().call()
    print(f"Limit: {limit/1e18}")
except Exception as e:
    print(f"An error occurred while fetching limit: {e}")
