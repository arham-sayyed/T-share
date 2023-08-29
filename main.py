import sys, os
from connecs.envs import check_env_token, update_token
from connecs.reqs import upload_file

args = sys.argv

def main(args_list):
    try:
        if not len(args_list) == 3:
            print("invalid arguments!")
            exit()

        if (args_list[1] == "-u") and os.path.exists(args_list[2]):
            if not check_env_token():
                print("auth token is absent! \nuse `--change-token <token>` to set token")
            file_link = upload_file(file_path = args_list[2])
            if file_link:
                print(f"upload successfull\n {file_link}")

        elif args_list[1] == "-g":
            # download(url = args_list[2])
            print("download feature is still under development!")

        elif args_list[1] == "--change-token":
            update_token(args_list[2])

            
    except Exception as e:
        print(f"Error: {e} \nin main")
        return False
    
if __name__ == "__main__":
    main(args_list=args)

