import json
from pathlib import Path

INVENTORY = dict()
INVENTORY_HISTORY = set()
INVENTORY_FILE = Path(__file__).resolve().parent.parent / 'inventory_current.json'

# ASCII Colours
GREEN = '\033[92m' # Success
RED = '\033[91m' # Errors
YELLOW = '\033[93m' # Warnings or info
CYAN = '\033[96m' # Neutral/system
RESET = '\033[0m'

def load_inventory(file: str=INVENTORY_FILE) -> None:
    try:
        with open(file, 'r') as file_open:
            inventory = json.load(file_open)
            INVENTORY.update(inventory['inventory'])
            INVENTORY_HISTORY.update(inventory['inventory_history'])
    except FileNotFoundError as err:
        print(f'{RED}{err}. No file {file} found{RESET}')

def save_inventory(file: str=INVENTORY_FILE) -> None:
    try:
        with open(file, 'w') as file_open:
            json.dump({'inventory': INVENTORY, 'inventory_history': list(INVENTORY_HISTORY)}, file_open, indent=2)
    except PermissionError as err:
        print(f"{RED}{err}. You don't have access to write to {file}{RESET}")

def summary() -> None:
    if INVENTORY:
        total_in_stock = sum(INVENTORY.values())
        unique_items = len(INVENTORY.keys())
        most_in_stock = [item for item in INVENTORY if INVENTORY[item] == max(INVENTORY.values())]
        least_in_stock = [item for item in INVENTORY if INVENTORY[item] == min(INVENTORY.values())]
        print(f'Total number of items in stock: {total_in_stock}')
        print(f'Total unique item types: {unique_items}')
        print(f'Most stocked item: {most_in_stock[0]}')
        print(f'Least stocked item: {least_in_stock[0]}')
    else:
        print(f'{YELLOW}No items in stock!{RESET}')

def view_inventory() -> None:
    if INVENTORY:
        print('Here is the full inventory list:')
        for item, qty in sorted(INVENTORY.items()):
            print(f'Item: {item} | Qty: {qty}')
    else:
        print(f'{YELLOW}Inventory is empty!{RESET}')

def view_history_inventory() -> None:
    if INVENTORY_HISTORY:
        print('Here is the full inventory list:')
        print(INVENTORY_HISTORY)
    else:
        print(f'{YELLOW}Inventory history is empty!{RESET}')

def clear_inventory() -> None:
    INVENTORY.clear()
    print(f'{YELLOW}Inventory is now empty!{RESET}')

def add_item(name: str, qty: int) -> None:
    if name not in INVENTORY.keys():
        INVENTORY[name] = qty
        INVENTORY_HISTORY.add(name)
        print(f'{GREEN}Item added to the inventory!{RESET}')
    else:
        INVENTORY[name] += qty
        print(f'{GREEN}Added more of the same to the inventory!{RESET}')

def remove_item(name: str, qty: int) -> None:
    if name not in INVENTORY.keys():
        print(f'{RED}{name} not in inventory!{RESET}')
    elif qty == INVENTORY[name]:
        del INVENTORY[name]
        print(f'{GREEN}Item completely removed from the inventory!{RESET}')
    elif qty < INVENTORY[name]:
        INVENTORY[name] -= qty
        print(f'{GREEN}Item removed from the inventory!{RESET}')
    elif qty > INVENTORY[name]:
        print(f'{RED}Not enough items to remove!{RESET}')

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