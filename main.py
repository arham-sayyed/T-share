import sys, os
from connecs.envs import check_env_token, update_token
from connecs.reqs import upload_file
from firebase_files.firebase_auth import *
from firebase_files.firebase_sharing import * 

args = sys.argv

def display_help():
    help_text = """
Usage:

    -r <email> <password>        : Register a new user.
    -l <email> <password>        : Login a user.
    -s <receiver_email> <link>   : Share a link with another user.
    -gl                          : Get shared links for the logged-in user.
    -u <filepath>                : Upload a file to Web3.
    --change-token <token>       : Change the authentication token (for advanced users).
    -h                           : Display this help message.

Note: Always ensure you use secure and unique passwords when registering.
    """
    print(help_text)

# display_help()

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
                print("Logged in successfully!")
            else:
                print("Failed to log in.")

        # Share a link
        elif command == "-s" and len(args_list) == 4:
            receiver_email = args_list[2]
            link = args_list[3]
            if share_link(auth.current_user['email'], receiver_email, link):
                print("Link shared successfully!")
            else:
                print("Failed to share the link.")

        # Get shared links
        elif command == "-gl":
            links = get_shared_links()
            if links:
                print("Received links:")
                for sender, link_list in links.items():
                    for link in link_list.values():
                        print(f"From {sender}: {link}")
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

        # Other commands...
        # Add additional elif clauses for other commands as necessary.
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

