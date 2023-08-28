import os, sys, requests


def verify_token(token: str) -> bool: # run only when the token is being changed
    # headers["Authorization"] = f"Bearer {token}"
    headers = {
    "Authorization": f"Bearer {token}",  # replace 'YOUR_TOKEN' with the token you want to verify
    "Content-Type": "application/x-directory"
    }
    
    # Making a benign request to list the first page of stored files
    response = requests.get(f"https://api.web3.storage/user/uploads", headers=headers)
    
    # If the response is unauthorized, return False
    if response.status_code == 401:
        return False
    # If the response is okay (status code 200), return True
    elif response.status_code == 200:
        return True
    # For other responses, raise an exception (or handle differently as per your requirements)
    else:
        response.raise_for_status()


def check_env_token() -> bool:  # run everytime when the tool is called
    if "TSHARE_AUTH_TOKEN" in os.environ:
        return True
    else:
        return False




def update_token(token: str): # called to change the token or add on installation
    if verify_token(token = token):
        os.environ['TSHARE_AUTH_TOKEN'] = str(token)
        print("token updated successfully!")
    else:
        print("invalid token!")
        exit()

























