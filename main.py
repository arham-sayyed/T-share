import argparse
from connecs import login

def main():
    try:
        parser = argparse.ArgumentParser(description="Tshare File Manager")
        parser.add_argument("--login", action="store_true", help="Log in to Tshare")
        args = parser.parse_args()

        if args.login:
            token_manager = login()
            token_manager.run()
        else:
            parser.print_help()
        
    except Exception as e:
        #print(f"Error: {e} \nin main")
        return False
    
if __name__ == "__main__":
    main()