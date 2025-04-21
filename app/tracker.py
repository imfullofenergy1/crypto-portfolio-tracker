import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_wallet_data():
    wallet_address = os.getenv("WALLET_ADDRESS")
    etherscan_api_key = os.getenv("ETHERSCAN_API_KEY")

    # ETH Balance (in Wei)
    eth_balance_url = f"https://api.etherscan.io/api?module=account&action=balance&address={wallet_address}&tag=latest&apikey={etherscan_api_key}"
    eth_balance_response = requests.get(eth_balance_url).json()
    balance_eth = int(eth_balance_response['result']) / 1e18

    # HEX Token Balance (ERC20)
    hex_contract = "0x2b591e99afe9f32eaa6214f7b7629768c40eeb39"
    hex_token_url = f"https://api.etherscan.io/api?module=account&action=tokenbalance&contractaddress={hex_contract}&address={wallet_address}&tag=latest&apikey={etherscan_api_key}"
    hex_response = requests.get(hex_token_url).json()
    balance_hex = int(hex_response['result']) / 1e8  # HEX has 8 decimals

    # Prices from CoinGecko
    prices = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=ethereum,hex&vs_currencies=usd").json()
    eth_price = prices['ethereum']['usd']
    hex_price = prices['hex']['usd']

    return [
    {
        'wallet': wallet_address,
        'token': 'ETH',
        'balance': round(balance_eth, 4),
        'usd_value': round(balance_eth * eth_price, 2)
    },
    {
        'wallet': wallet_address,
        'token': 'HEX',
        'balance': round(balance_hex, 2),
        'usd_value': round(balance_hex * hex_price, 2)
    }
]