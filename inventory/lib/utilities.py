# ASCII Colours
GREEN = '\033[92m' # Success
RED = '\033[91m' # Errors
YELLOW = '\033[93m' # Warnings or info
CYAN = '\033[96m' # Neutral/system
RESET = '\033[0m'

def get_string(prompt: str) -> str:
    while True:
        try:
            return input(prompt).strip(' ').lower()
        except Exception as err:
            print(f'{err}')

def get_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt).strip(' '))
        except Exception as err:
            print(f'{RED}{err}. Invalid number. Please try again.{RESET}')
