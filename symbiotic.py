from web3 import Web3

endpoint_uri = "https://rpc.ankr.com/eth"
contract_address = '0xca11bde05977b3631167028862be2a173976ca11'
address = '0xe39B5f5638a209c1A6b6cDFfE5d37F7Ac99fCC84'  # https://app.symbiotic.fi/restake/ena

web3 = Web3(Web3.HTTPProvider(endpoint_uri))

if not web3.is_connected():
    print("Connection failed")

with open(f"abi/{contract_address}.json") as f:
    contract_abi = f.read()

args = [
    ('0xe39B5f5638a209c1A6b6cDFfE5d37F7Ac99fCC84', True, b'\x18\x16\r\xdd'),
    ('0xe39B5f5638a209c1A6b6cDFfE5d37F7Ac99fCC84', True, b'\xa4\xd6m\xaf'),
    # ('0xB26ff591F44b04E78de18f43B46f8b70C6676984', True, b'\x18\x16\r\xdd'),
    # ('0xB26ff591F44b04E78de18f43B46f8b70C6676984', True, b'\xa4\xd6m\xaf'),
    # ('0xBdea8e677F9f7C294A4556005c640Ee505bE6925', True, b'\x18\x16\r\xdd'),
    # ('0xBdea8e677F9f7C294A4556005c640Ee505bE6925', True, b'\xa4\xd6m\xaf'),
    # ('0x475D3Eb031d250070B63Fa145F0fCFC5D97c304a', True, b'\x18\x16\r\xdd'),
    # ('0x475D3Eb031d250070B63Fa145F0fCFC5D97c304a', True, b'\xa4\xd6m\xaf'),
    # ('0x03Bf48b8A1B37FBeAd1EcAbcF15B98B924ffA5AC', True, b'\x18\x16\r\xdd'),
    # ('0x03Bf48b8A1B37FBeAd1EcAbcF15B98B924ffA5AC', True, b'\xa4\xd6m\xaf'),
    # ('0x5198CB44D7B2E993ebDDa9cAd3b9a0eAa32769D2', True, b'\x18\x16\r\xdd'),
    # ('0x5198CB44D7B2E993ebDDa9cAd3b9a0eAa32769D2', True, b'\xa4\xd6m\xaf'),
    # ('0x19d0D8e6294B7a04a2733FE433444704B791939A', True, b'\x18\x16\r\xdd'),
    # ('0x19d0D8e6294B7a04a2733FE433444704B791939A', True, b'\xa4\xd6m\xaf'),
    # ('0x38B86004842D3FA4596f0b7A0b53DE90745Ab654', True, b'\x18\x16\r\xdd'),
    # ('0x38B86004842D3FA4596f0b7A0b53DE90745Ab654', True, b'\xa4\xd6m\xaf'),
    # ('0x422F5acCC812C396600010f224b320a743695f85', True, b'\x18\x16\r\xdd'),
    # ('0x422F5acCC812C396600010f224b320a743695f85', True, b'\xa4\xd6m\xaf'),
    # ('0xC329400492c6ff2438472D4651Ad17389fCb843a', True, b'\x18\x16\r\xdd'),
    # ('0xC329400492c6ff2438472D4651Ad17389fCb843a', True, b'\xa4\xd6m\xaf')
]

contract = web3.eth.contract(address=Web3.to_checksum_address(contract_address), abi=contract_abi)
try:
    response = contract.functions.aggregate3(args).call()
except Exception as e:
    print(f"An error occurred while fetching totalSupply: {e}")

data = {}
for i, r in enumerate(args):
    req = int.from_bytes(r[2], byteorder='big')
    if r[0] not in data:
        data[r[0]] = {}
    if req == 404098525:
        req = 'supply'
    else:
        req = 'limit'
    data[r[0]][req] = int.from_bytes(response[i][1], byteorder='big') / 1e18
    # print(i, r[0], r[1], req, int.from_bytes(response[i]['returnData'], byteorder='big')/1e18)

print(f"Total Supply: {data[address]['supply']}")
print(f"Limit: {data[address]['limit']}")

# from tabulate import tabulate
# headers = ['Address', 'Supply', 'Limit', 'Remaining', 'Percent']
# table_data = [[k, "{:.18f}".format(v['supply']), "{:.18f}".format(v['limit']),
#                "{:.18f}".format(v['limit'] - v['supply']),
#                f"{((v['limit'] - v['supply']) / v['limit'] * 100):.2f}%"
#                ] for k, v in data.items()]
# print(tabulate(table_data, headers=headers, tablefmt='pretty', stralign="right"))
