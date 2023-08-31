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

def email_to_username(email):
    return email.replace("@", "").replace(".", "")

def register_user(email, password) -> dict | None:
    try:
        user = auth.create_user_with_email_and_password(email, password)
        
        # Save email to username mapping (can be used for reverse lookup if needed)
        username = email_to_username(email)
        db.child("email_to_username").child(email).set(username)
        
        return user
    except Exception as e:
        print(f"Error: {e} in register user")
        return None

def login_user(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        # print(user)
        return user
    except Exception as e:
        print(f"Error: {e} in login user")
        return None

def verify_user(token):
    try:
        user = auth.get_account_info(token)
        return user
    except Exception as e:
        print(f"Error: {e} in verify user")
        return None
