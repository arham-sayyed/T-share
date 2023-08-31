import pyrebase, json, os
from firebase_files.firebase_auth import *

CONFIG_FILE = "config.json"
SESSION_FILE = os.path.join(os.path.expanduser('~'), '.tshare_session.json')

def load_config_from_file():
    """Load the token from the config file, if it exists."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
            return config.get("config", None)
    return None

config = load_config_from_file()

def load_session():
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, 'r') as f:
            return json.load(f)
    return None

if config:
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

def email_to_username(email):
    return email.replace("@", "").replace(".", "")

def share_link(sender_email, receiver_email, link):
    try:
        session_data = load_session()
        if not session_data:
            print("Please log in first.")
            return False
        
        sender_username = email_to_username(sender_email)
        receiver_username = email_to_username(receiver_email)
        
        # Save the link under the sender's username
        sent_data = {
            "link": link,
            "receiver": receiver_username
        }
        db.child("users").child(sender_username).child("sent_links").push(sent_data)
        
        # Save the link under receiver's username indicating it was shared by sender
        received_data = {
            "link": link,
            "sender": sender_username
        }
        db.child("users").child(receiver_username).child("received_links").push(received_data)
        return True

    except Exception as e:
        print(f"Error: {e} in share link")
        return False


def get_shared_links_for_current_user():
    try:
        # Fetch UID of the currently logged-in user
        session_data = load_session()  # Assuming session data has email info
        if not session_data:
            print("Please log in first.")
            return None

        current_user_email = session_data['email']
        username = email_to_username(current_user_email)
        
        # Fetch links shared with the user
        received_links_data = db.child("users").child(username).child("received_links").get().val()
        # print(received_links_data)
        
        received_links = []
        if received_links_data:
            for _, link_data in received_links_data.items():
                received_links.append((link_data["link"], link_data["sender"]))
        
        # Similarly for sent links, if needed
        # ...

        return received_links
    except Exception as e:
        print(f"Error: {e} in get_shared_links_for_current_user")
        return None

def get_sent_links_for_current_user():
    try:
        # Fetch UID of the currently logged-in user
        session_data = load_session()  # Assuming session data has email info
        if not session_data:
            print("Please log in first.")
            return None

        current_user_email = session_data['email']
        username = email_to_username(current_user_email)
        
        # Fetch links sent by the user
        sent_links_data = db.child("users").child(username).child("sent_links").get().val()
        
        sent_links = []
        if sent_links_data:
            for _, link_data in sent_links_data.items():
                sent_links.append((link_data["link"], link_data["receiver"]))
        
        return sent_links
    except Exception as e:
        print(f"Error: {e} in get_sent_links_for_current_user")
        return None

# get_shared_links_for_current_user()