import pyrebase, json, os
from firebase_auth import *

CONFIG_FILE = "config.json"

def load_config_from_file():
    """Load the token from the config file, if it exists."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
            return config.get("config", None)
    return None

config = load_config_from_file()

if config:
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

def share_link(sender_email, receiver_email, link):
    try:
        # Retrieve sender's UID
        sender_uid = auth.get_account_info(auth.current_user['idToken'])['users'][0]['localId']
        
        # Save the link under the sender's UID (this step can be skipped if not required)
        db.child("users").child(sender_uid).child("sent_links").push(link)
        
        # Retrieve receiver's UID from their email (this requires a function which we will define next)
        receiver_uid = get_uid_from_email(receiver_email)
        
        if receiver_uid:
            # Save the link under receiver's UID indicating it was shared by sender
            db.child("users").child(receiver_uid).child("received_links").child(sender_uid).push(link)
            return True
        else:
            print("Receiver email not found in the system.")
            return False

    except Exception as e:
        print(f"Error: {e}")
        return False