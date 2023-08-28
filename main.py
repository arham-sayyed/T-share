import sys, os

args = sys.argv

def main(args_list):
    try:
        if not len(args_list) == 3:
            print("invalid arguments!")
            exit()

        if (args_list[1] == "-u") and os.path.exists(args_list[2]):
            upload(file_path = args_list[2])

        elif args_list[1] == "-g":
            download(url = args_list[2])

        return True
    except Exception as e:
        print(f"Error: {e} \nin main")
        return False
    


