import pyrebase, json, os


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
    auth = firebase.auth()
    db = firebase.database()

def register_user(email, password) -> dict | None:
    try:
        user = auth.create_user_with_email_and_password(email, password)
        
        # Save email to UID mapping
        db.child("email_to_uid").child(email).set(user['localId'])
        
        return user
    except Exception as e:
        print(f"Error: {e}")
        return None

def login_user(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return user
    except Exception as e:
        print(f"Error: {e}")
        return None

def verify_user(token):
    try:
        user = auth.get_account_info(token)
        return user
    except Exception as e:
        print(f"Error: {e}")
        return None

