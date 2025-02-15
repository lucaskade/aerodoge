import threading
from drone_api import app
from contract_interaction import listen_to_contract_events

def run_api():
    app.run(debug=False, host='0.0.0.0', port=5000)

def run_event_listener():
    listen_to_contract_events()

if __name__ == "__main__":
    # Create the database if it doesn't exist
    from database import create_db
    create_db()

    # Start the Flask API in a separate thread
    api_thread = threading.Thread(target=run_api)
    api_thread.start()

    # Start listening to contract events
    run_event_listener()
