import requests
from connecs.envs import get_token


API_ENDPOINT = "https://api.web3.storage"



def upload_file(file_path):

    token = get_token()

    with open(file_path, 'rb') as f:
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/x-directory"
        }

        response = requests.post(f"{API_ENDPOINT}/upload", headers=headers, data=f)

    if response.status_code == 200:
        print(response.json())
        print("\n\n")
        cid = response.json()["cid"]
        return f"https://{cid}.ipfs.w3s.link"

    else:
        print("Upload Error:", response.text)
        return None

