from contract_interaction import log_drone_status

def main():
    drone_status = "In flight"
    drone_id = 2  # Example drone ID

    print("Logging drone status...")
    tx_hash = log_drone_status(drone_status, drone_id)
    print(f"Transaction sent with hash: {tx_hash}")

if __name__ == "__main__":
    main()
