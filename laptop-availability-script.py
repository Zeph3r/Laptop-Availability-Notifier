import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants from .env or directly from the environment
API_ENDPOINT = os.environ.get('API_ENDPOINT')
TOKEN = os.environ.get('BOSSDESK_API_TOKEN')

# Setup headers for API request
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

def fetch_and_count_available_devices():
    params = {
        "type": "laptop",
        "status": "available"
    }

    try:
        response = requests.get(API_ENDPOINT, headers=headers, params=params)
        response.raise_for_status()
        devices = response.json()
        count = len(devices)
        return count
    except requests.RequestException as e:
        print(f"Error fetching data from BOSSDesk API: {e}")
        return 0

def main():
    count = fetch_and_count_available_devices()
    print(f"Number of available laptops: {count}")

if __name__ == "__main__":
    main()
