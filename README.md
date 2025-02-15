# AeroDoge Blockchain Integration

## Project Overview
AeroDoge is a blockchain-based system for autonomous drone navigation. The project interacts with Ethereum smart contracts to log drone statuses (e.g., "Ready for takeoff", "In flight").

## Setup Instructions

1. Clone the repository.
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Create a `.env` file in the root directory with the following values:
    ```env
    PRIVATE_KEY=your-private-key-here
    INFURA_API_KEY=your-infura-api-key-here
    CONTRACT_ADDRESS=your-contract-address-here
    ```
4. Run the `main.py` script:
    ```bash
    python main.py
    ```

## License
This project is open-source and available under the [MIT License](LICENSE).
