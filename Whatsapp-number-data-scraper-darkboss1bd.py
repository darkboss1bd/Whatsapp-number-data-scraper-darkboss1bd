#BY: HACK UNDERWAY

import os
import requests
import json
import webbrowser
from dotenv import load_dotenv
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

# Load environment variables from .env
load_dotenv()

# API key and host from .env
api_key = os.getenv('RAPIDAPI_KEY')
api_host = os.getenv('RAPIDAPI_HOST')

# Function to print JSON with formatting and colors
def print_colored_json(data, level=0):
    indent = "    " * level
    if isinstance(data, dict):
        for key, value in data.items():
            print(f"{indent}{Fore.CYAN}{key}{Style.RESET_ALL}: ", end="")
            print_colored_json(value, level + 1)
    elif isinstance(data, list):
        for item in data:
            print_colored_json(item, level)
    else:
        print(f"{Fore.YELLOW}{data}{Style.RESET_ALL}")

# Function to query WhatsApp number data
def query_whatsapp_number(phone_number):
    url = f"https://{api_host}/number/{phone_number}"
    headers = {
        "x-rapidapi-key": api_key,
        "x-rapidapi-host": api_host
    }
    
    try:
        # Perform GET request to the API
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # Get response in JSON
        data = response.json()
        
        # Print formatted JSON
        print_colored_json(data)
    
    except requests.exceptions.HTTPError as http_err:
        print(f"{Fore.RED}HTTP Error: {http_err}{Style.RESET_ALL}")
    except requests.exceptions.RequestException as req_err:
        print(f"{Fore.RED}Request Error: {req_err}{Style.RESET_ALL}")
    except json.JSONDecodeError:
        print(f"{Fore.RED}Error processing JSON response.{Style.RESET_ALL}")
    except Exception as err:
        print(f"{Fore.RED}An error occurred: {err}{Style.RESET_ALL}")

def main():
    # Auto-open your links
    webbrowser.open_new_tab("https://t.me/darkvaiadmin")
    webbrowser.open_new_tab("https://serialkey.top/")

    # Banner with your info
    print(Fore.GREEN + """
     __i
    |---|    
    |[_]|    
    |:::|    
    |:::|    
    `\\   \\   
      \\_=_\\ 
    WhatsApp Number Data Lookup
    --------------------------------
    Telegram: https://t.me/darkvaiadmin
    Website : https://serialkey.top/
    --------------------------------
    """ + Style.RESET_ALL)

    phone = input("Enter the phone number (with country code): ")
    
    # Validate input
    if not phone.strip():
        print("You must enter a valid phone number.")
        return
    
    # Query number
    query_whatsapp_number(phone)

if __name__ == "__main__":
    main()
