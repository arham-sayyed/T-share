
import logging
from colorama import init, Fore, Style
from pyfiglet import Figlet

class TshareLogin:
    def __init__(self):
        init(autoreset=True)
        self.logger = self.setup_logger()

    def setup_logger(self):
        logger = logging.getLogger("Tshare Login Manager!")
        logger.setLevel(logging.INFO)
        
        console_handler = logging.StreamHandler()
        logger.addHandler(console_handler)
        
        return logger
    
    @staticmethod
    def save_token(token):
        with open("token.txt", "w") as f:
            f.write(token)
        
    def run(self):
        f = Figlet(font='big')
        colored_text = f"{Fore.BLUE}Tshare Login Manager!" 
        rendered_text = f.renderText("Tshare Login Manager!")
        self.logger.info(colored_text + "\n" + rendered_text)
        user_token = input(f"{Fore.MAGENTA}Please input your Github Token to Login\n")
        if user_token.strip():
            self.save_token(user_token)
            self.logger.info(f"{Fore.GREEN}{Style.BRIGHT}Login Successful!")
        else:
            self.logger.info(f"{Fore.RED}Invalid token. Login failed.")
        


