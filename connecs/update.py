import logging
from colorama import init, Fore, Style
from pyfiglet import Figlet

class TshareUpdateToken:
    def __init__(self):
        init(autoreset=True)
        self.logger = self.setup_logger()

    def setup_logger(self):
        logger = logging.getLogger("Tshare Token Update Manager!")
        logger.setLevel(logging.INFO)
        
        console_handler = logging.StreamHandler()
        logger.addHandler(console_handler)
        
        return logger
    
    @staticmethod
    def update_token(new_token):
        with open("token.txt", "a") as f:
            f.write(new_token + "\n")
        
    def run(self):
        f = Figlet(font='big')
        colored_text = f"{Fore.BLUE}Tshare update token manager!" 
        rendered_text = f.renderText("Tshare update token manager!")
        self.logger.info(colored_text + "\n" + rendered_text)
        user_token = input(f"{Fore.MAGENTA}Please input your new Github Token to update\n")
        if user_token.strip():
            self.update_token(user_token)
            self.logger.info(f"{Fore.GREEN}{Style.BRIGHT}Token Updated Successfully!")
        else:
            self.logger.info(f"{Fore.RED}Invalid, Token update failed.")
