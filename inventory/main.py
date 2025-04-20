from .core import (
    load_inventory, view_inventory, view_history_inventory,
    add_item, remove_item, save_inventory, summary,
    clear_inventory, export_csv
)
from .lib.utilities import CYAN, YELLOW, RESET, get_int, get_string
import sys
import argparse

parser = argparse.ArgumentParser(description='')
summary_arg = parser.add_argument('--summary', action='store_true')
view_arg = parser.add_argument('--view', action='store_true')
clear_arg = parser.add_argument('--clear', action='store_true')

args = parser.parse_args()

def menu() -> None:
    load_inventory()
    while True:
        print(f'{CYAN}Welcome to Inventory Tracker{RESET}')
        print(f'''{CYAN}
            1. View Inventory
            2. Add Item
            3. Remove Item
            4. View all previously stocked items
            5. Clear all items in inventory
            6. Summary
            7. Export current inventory to csv
            8. Exit
        {RESET}''')
        choice = get_string(f'{CYAN}Choose an option: {RESET}')

        if choice == '1':
            view_inventory()
        elif choice == '2':
            item_name = get_string(f'{CYAN}What item would you like to add: {RESET}')
            item_qty = get_int(f'{CYAN}How many of this item: {RESET}')
            add_item(item_name, item_qty)
            save_inventory()
        elif choice == '3':
            item_name = get_string(f'{CYAN}What item would you like to remove: {RESET}')
            item_qty = get_int(f'{CYAN}Would you like to remove only one item of this or fully: {RESET}')
            remove_item(item_name, item_qty)
            save_inventory()
        elif choice == '4':
            view_history_inventory()
        elif choice == '5':
            confirm = get_string(f'{YELLOW}Are you sure you want to clear the inventory? (y/n){RESET}')
            if confirm == 'y':
                clear_inventory()
                save_inventory()
            else:
                continue
        elif choice == '6':
            summary()
        elif choice == '7':
            export_csv()
        elif choice == '8':
            confirm = get_string(f'{YELLOW}Are you sure you want to exit? (y/n){RESET}')
            if confirm == 'y':
                save_inventory()
                print(f'{CYAN}Goodbye!{RESET}')
                sys.exit(0)
            else:
                continue
        else:
            continue

def main():
    if args.summary:
        load_inventory()
        summary()
        sys.exit()
    elif args.view:
        load_inventory()
        view_inventory()
        sys.exit()
    elif args.clear:
        load_inventory()
        clear_inventory()
        save_inventory()
        sys.exit()
    else:
        menu()

if __name__ == '__main__':
    main()