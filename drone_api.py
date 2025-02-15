from flask import Flask, request, jsonify
from contract_interaction import log_drone_status

app = Flask(__name__)

@app.route('/update_status', methods=['POST'])
def update_status():
    data = request.get_json()
    
    # Validate input data
    if not data or 'status' not in data or 'drone_id' not in data:
        return jsonify({"error": "Invalid data, 'status' and 'drone_id' are required."}), 400

    status = data['status']
    drone_id = data['drone_id']
    
    # Log the drone status via the smart contract
    tx_hash = log_drone_status(status, drone_id)
    
    if tx_hash:
        return jsonify({"message": "Drone status updated successfully!", "tx_hash": tx_hash}), 200
    else:
        return jsonify({"error": "Failed to update drone status."}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
