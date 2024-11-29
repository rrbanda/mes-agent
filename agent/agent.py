import requests
import time
import os
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

MESOP_APP_URL = os.getenv('MESOP_APP_URL', 'http://mesop-app-container:8080')
API_KEY = os.getenv('API_KEY', 'default_api_key')  # Secure this appropriately

def perform_task(input_data):
    url = f"{MESOP_APP_URL}/process"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {API_KEY}"
    }
    payload = {'input': input_data}
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        output = response.json().get('output')
        logging.info(f"Agent received output: {output}")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error communicating with Mesop App: {e}")

def main():
    # Example input data; in a real scenario, this could come from various sources
    example_inputs = ["Task 1", "Task 2", "Task 3"]

    while True:
        logging.info("Starting new task cycle.")
        for input_data in example_inputs:
            perform_task(input_data)
            time.sleep(5)  # Wait for 5 seconds before the next task
        logging.info("Completed task cycle. Waiting before next cycle.")
        time.sleep(10)  # Reduced sleep for testing

if __name__ == '__main__':
    main()
