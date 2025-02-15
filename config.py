import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve sensitive values from environment variables
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
INFURA_API_KEY = os.getenv('INFURA_API_KEY')
CONTRACT_ADDRESS = os.getenv('CONTRACT_ADDRESS')

# Ensure all sensitive data is loaded
if not PRIVATE_KEY:
    raise ValueError("Private key is not set in environment variables!")
if not INFURA_API_KEY:
    raise ValueError("Infura API key is not set in environment variables!")
if not CONTRACT_ADDRESS:
    raise ValueError("Contract address is not set in environment variables!")

