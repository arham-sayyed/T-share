import os
import sys
import requests
import json

# Define the path to the configuration file
CONFIG_FILE = "config.json"

def verify_token(token: str) -> bool:
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/x-directory"
    }
    
    response = requests.get(f"https://api.web3.storage/user/uploads", headers=headers)
    
    if response.status_code == 401:
        return False
    elif response.status_code == 200:
        return True
    else:
        response.raise_for_status()

def check_env_token() -> bool:
    """Check if token exists in the config file."""
    if load_token_from_config():
        return True
    else:
        return False

def update_token(token: str):
    """Update or set the token in the config file after verification."""
    if verify_token(token=token):
        try:
            save_token_to_config(token)
            if load_token_from_config():
                print("Token updated successfully!")
            else:
                print("Something went wrong.")
        except Exception as e:
            print(e)
    else:
        print("Invalid token!")
        exit()

def save_token_to_config(token):
    """Save the token to a config file."""
    with open(CONFIG_FILE, 'w') as f:
        json.dump({"TSHARE_AUTH_TOKEN": token}, f)

def load_token_from_config():
    """Load the token from the config file, if it exists."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
            return config.get("TSHARE_AUTH_TOKEN", None)
    return None

def get_token() -> str | bool:
    """Retrieve the token from the config file."""
    return load_token_from_config() or False
