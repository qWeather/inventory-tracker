import json
import csv
from typing import Optional
from importlib.resources import files

INVENTORY = dict()
INVENTORY_HISTORY = set()
INVENTORY_FILE = files("inventory.data").joinpath("inventory_current.json")

def load_inventory(file: str=INVENTORY_FILE) -> str | FileNotFoundError:
    try:
        with open(file, 'r') as file_open:
            inventory = json.load(file_open)
            INVENTORY.update(inventory['inventory'])
            INVENTORY_HISTORY.update(inventory['inventory_history'])
            return f'Loaded inventory successfully from {file}'
    except FileNotFoundError as err:
        raise FileNotFoundError(f'No file {file} found!')

def save_inventory(file: str=INVENTORY_FILE) -> str | PermissionError:
    try:
        with INVENTORY_FILE.open("w") as file_open:
            json.dump({'inventory': INVENTORY, 'inventory_history': list(INVENTORY_HISTORY)}, file_open, indent=2)
            return f'Successfully saved inventory to {file}'
    except PermissionError as err:
        raise PermissionError(f"You don't have access to write to {file}")

def summary() -> Optional[tuple[str, str, str, str]]:
    if INVENTORY:
        most_in_stock = [item for item in INVENTORY if INVENTORY[item] == max(INVENTORY.values())]
        least_in_stock = [item for item in INVENTORY if INVENTORY[item] == min(INVENTORY.values())]
        return sum(INVENTORY.values()), len(INVENTORY.keys()), most_in_stock[0], least_in_stock[0]
    else:
        return None

def view_inventory() -> Optional[dict]:
    if INVENTORY:
        return sorted(INVENTORY.items())
    else:
        return None

def view_history_inventory() -> Optional[list[str]]:
    if INVENTORY_HISTORY:
        return sorted(INVENTORY_HISTORY)
    else:
        return None

def clear_inventory() -> None:
    INVENTORY.clear()
    save_inventory()

def add_item(name: str, qty: int) -> str:
    if name not in INVENTORY.keys():
        INVENTORY[name] = qty
        INVENTORY_HISTORY.add(name)
        save_inventory()
        return 'Item added to the inventory!'
    else:
        INVENTORY[name] += qty
        save_inventory()
        return 'Added more of the same to the inventory!'

def remove_item(name: str, qty: int) -> str:
    if name not in INVENTORY.keys():
        return f'{name} not in inventory!'
    elif qty == INVENTORY[name]:
        del INVENTORY[name]
        save_inventory()
        return 'Item completely removed from the inventory!'
    elif qty < INVENTORY[name]:
        INVENTORY[name] -= qty
        save_inventory()
        return 'Item removed from the inventory!'
    elif qty > INVENTORY[name]:
        return 'Not enough items to remove!'

def export_csv(inventory: dict = INVENTORY, filename: str = 'inventory_current.csv') -> str | PermissionError:
    try:
        with open(filename, 'w', newline='') as csv_file:
            dict_writer = csv.DictWriter(csv_file, fieldnames=['item', 'quantity'])
            dict_writer.writeheader()
            for item, qty in inventory.items():
                dict_writer.writerow({'item': item, 'quantity': qty})
            return f'Successfully exported to CSV as {filename}'
    except PermissionError:
        raise PermissionError(f"You don't have access to write to {filename}")