import os
from web3 import Web3
from config import PRIVATE_KEY, INFURA_API_KEY, CONTRACT_ADDRESS

# Connect to Ethereum network using the Infura API key
web3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{INFURA_API_KEY}'))

# Ensure the connection is successful
if not web3.isConnected():
    raise ConnectionError("Failed to connect to Ethereum network via Infura.")

# Set default account
web3.eth.defaultAccount = web3.eth.accounts[0]

# Contract ABI (can be stored as a JSON object or loaded from a separate file)
contract_abi = [...]  # Replace this with your actual contract ABI

# Create contract instance
contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)

def log_drone_status(status, drone_id):
    """
    Function to log the drone status by calling the smart contract.
    Arguments:
        status (str): The current status of the drone (e.g., "Ready for takeoff").
        drone_id (int): The unique identifier of the drone.
    Returns:
        str: Transaction hash of the recorded status.
    """
    tx = contract.functions.recordStatus(drone_id, status).buildTransaction({
        'from': web3.eth.defaultAccount,
        'gas': 2000000,
        'gasPrice': web3.toWei('10', 'gwei'),
        'nonce': web3.eth.getTransactionCount(web3.eth.defaultAccount),
    })

    # Sign and send the transaction
    signed_tx = web3.eth.account.signTransaction(tx, private_key=PRIVATE_KEY)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    
    return tx_hash.hex()

# Example usage
if __name__ == '__main__':
    drone_status = "Ready for takeoff"
    drone_id = 1
    tx_hash = log_drone_status(drone_status, drone_id)
    print(f"Transaction sent with hash: {tx_hash}")
