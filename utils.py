import os
from colorama import Fore
import pyfiglet
import random
from pyrogram import Client

session_name = 'user'

def delete_residual_files(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith("_thumb.jpg"):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                except OSError:
                    pass

def authenticate():
    # Get credentialas from user
    def get_credentials():
        api_id = input("Digite seu API ID: ")
        api_hash = input("Digite seu API Hash: ")
        return api_id, api_hash

    # if session file does not exists, obtain the credentials 
    if not os.path.exists(f"{session_name}.session"):
        api_id, api_hash = get_credentials()
        with Client(session_name, api_id, api_hash) as app:
            print("Você está autenticado!")
    else:
        print("Usando sessão existente.")
        
class Banner:
    def __init__(self, banner):
        self.banner = banner
        self.lg = Fore.LIGHTGREEN_EX
        self.w = Fore.WHITE
        self.cy = Fore.CYAN
        self.ye = Fore.YELLOW
        self.r = Fore.RED
        self.n = Fore.RESET

    def print_banner(self):
        colors = [self.lg, self.r, self.w, self.cy, self.ye]
        f = pyfiglet.Figlet(font='slant')
        banner = f.renderText(self.banner)
        print(f'{random.choice(colors)}{banner}{self.n}')
        print(f'{self.r}  Version: v 1.0.0 https://github.com/viniped \n{self.n}')

def show_banner():
    banner = Banner('Vidsender')
    banner.print_banner()
