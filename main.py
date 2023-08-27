#!/usr/bin/env python3

import argparse
from connecs import login
from colorama import Fore
from pyfiglet  import Figlet

def check_token_file():
    try:
        with open("token.txt", "r") as f:
            return bool(f.read().strip())
    except FileNotFoundError:
        return False

def main():
    if check_token_file():
        parser = argparse.ArgumentParser(description="Tshare File Manager")
        parser.add_argument("--login", action="store_true", help="Log in to Tshare")
        args = parser.parse_args()

        if args.login:
            token_manager = login()
            token_manager.run()
        else:
            parser.print_help()
    else:
        logger  = login().logger
        f = Figlet(font='big')
        colored_text = f"{Fore.BLUE}Tshare File Manager!" 
        rendered_text = f.renderText("Tshare File Manager!")
        logger.info(colored_text + "\n" + rendered_text)
        logger.info(f"{Fore.RED}You are not logged in. Please log in using:\n\n")
        logger.info(f"{Fore.BLUE} Tshare --login")

if __name__ == "__main__":
    main()
