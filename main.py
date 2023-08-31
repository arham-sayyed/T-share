import sys, os
from connecs.envs import check_env_token, update_token
from connecs.reqs import upload_file
from firebase_files.firebase_auth import *
from firebase_files.firebase_sharing import *

SESSION_FILE = os.path.join(os.path.expanduser('~'), '.tshare_session.json')

args = sys.argv

def display_help():
    help_text = """
Usage:

    -r <email> <password>        : Register a new user.
    -l <email> <password>        : Login a user.
    -s <receiver_email> <link>   : Share a link with another user.
    -gl                          : Get shared links for the logged-in user.
    -gs                          : Get sent links for the logged-in user.
    -u <filepath>                : Upload a file to Web3.
    --change-token <token>       : Change the authentication token (for advanced users).
    -h                           : Display this help message.
    -logout                      : Log out the current user.

Note: Always ensure you use secure and unique passwords when registering.
    """
    print(help_text)

def store_session(data):
    with open(SESSION_FILE, 'w') as f:
        json.dump(data, f)

def load_session():
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, 'r') as f:
            return json.load(f)
    return None

def main(args_list):
    try:
        if len(args_list) < 2:
            print("Invalid arguments!")
            return

        command = args_list[1]

        # Register a new user
        if command == "-r" and len(args_list) == 4:
            email = args_list[2]
            password = args_list[3]
            user = register_user(email, password)
            if user:
                print("User registered successfully!")
            else:
                print("Failed to register user.")

        # Login user
        elif command == "-l" and len(args_list) == 4:
            email = args_list[2]
            password = args_list[3]
            user = login_user(email, password)
            if user:
                store_session(user)
                print("Logged in successfully!")
            else:
                print("Failed to log in.")

        # Share a link
        elif command == "-s" and len(args_list) == 4:
            session_data = load_session()
            if not session_data:
                print("Please log in first.")
                return
            receiver_email = args_list[2]
            link = args_list[3]
            if share_link(session_data['email'], receiver_email, link):
                print("Link shared successfully!")
            else:
                print("Failed to share the link.")

        # Get shared links
        elif command == "-gl":
            session_data = load_session()
            if not session_data:
                print("Please log in first.")
                return

            links = get_shared_links_for_current_user()
            if links:
                print("Received links:")
                for link, sender in links:
                    print(f"From {sender}: {link}")
            else:
                print("No links found.")
        # Get sent links
        elif command == "-gs":
            session_data = load_session()
            if not session_data:
                print("Please log in first.")
                return
            links = get_sent_links_for_current_user()
            if links:
                print("Sent links:")
                for link, receiver in links:
                    print(f"To {receiver}: {link}")
            else:
                print("No links found.")
        # Upload a file to Web3
        elif command == "-u" and len(args_list) == 3:
            file_path = args_list[2]
            if os.path.exists(file_path):
                if not check_env_token():
                    print("auth token is absent! \nuse `--change-token <token>` to set token")
                else:
                    file_link = upload_file(file_path)
                    if file_link:
                        print(f"Upload successful\n {file_link}")
                    else:
                        print("Upload failed.")
            else:
                print("File does not exist!")

        # Logout
        elif command == "-logout":
            if os.path.exists(SESSION_FILE):
                os.remove(SESSION_FILE)
                print("Logged out successfully.")
            else:
                print("No active session found.")

        # Display help
        elif command == "-h":
            display_help()

        else:
            print("Invalid arguments or command!")
            display_help()

    except Exception as e:
        print(f"Error: {e} \nin main")
        return False

if __name__ == "__main__":
    main(args_list=args)
