import requests

API_ENDPOINT = "https://api.web3.storage"
API_TOKEN = ""
headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/x-directory"
}

def upload_file(file_path):
    with open(file_path, 'rb') as f:
        response = requests.post(f"{API_ENDPOINT}/upload", headers=headers, data=f)

    if response.status_code == 200:
        print(response.json())
        print("\n\n")
        return response.json()["cid"] 
    else:
        print("Upload Error:", response.text)
        return None

def get_file_url(cid):
    return f"https://dweb.link/ipfs/{cid}"

file_path = input("file path: ")

# cid = upload_file(file_path=file_path)
