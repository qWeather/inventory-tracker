from inventory.core import load_inventory
from inventory.ui.gui import InventoryTrackerApp, root

def main():
    load_inventory()
    app = InventoryTrackerApp(root)
    app.mainloop()

if __name__ == '__main__':
    main()
