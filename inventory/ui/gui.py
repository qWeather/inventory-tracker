from tkinter import *
from  tkinter import ttk
from inventory.core import (
    view_history_inventory, view_inventory, add_item, remove_item,
    summary, export_csv, clear_inventory
)
from inventory.lib.utilities import get_string, get_int

root = Tk()

style = ttk.Style()
try:
    style.theme_use("clam")
except TclError:
    pass

class InventoryTrackerApp(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        root.title("Inventory Tracker")
        root.minsize(width=500, height=400)
        window_width = 500
        window_height = 400
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.active_frame = None

        frame = ttk.Frame(padding=10)
        frame.grid()
        self.grid_with_padding(ttk.Label(frame, text="Welcome to Inventory Tracker"), row=0, columnspan=3)
        ttk.Button(frame, text="Add Item", command=self.add_item_frame).grid(column=0, row=1)
        ttk.Button(frame, text="Remove Item", command=self.remove_item_frame).grid(column=1, row=1)
        ttk.Button(frame, text="Clear all items in inventory", command=self.clear_inventory_frame).grid(column=2, row=1)
        ttk.Button(frame, text="View Inventory", command=self.view_inventory_frame).grid(column=0, row=2)
        ttk.Button(frame, text="View all previously stocked items", command=self.view_inventory_history_frame).grid(column=1, row=2)
        ttk.Button(frame, text="Summary", command=self.summary_frame).grid(column=2, row=2)
        ttk.Button(frame, text="Export current inventory to csv", command=self.export_to_csv_frame).grid(row=3, columnspan=3)
        ttk.Button(frame, text="Exit", command=root.destroy).grid(row=4, columnspan=3)

    def grid_with_padding(self, widget, **grid_options):
        grid_options.setdefault('padx', 5)
        grid_options.setdefault('pady', 5)
        widget.grid(**grid_options)

    def init_frame(self):
        if self.active_frame:
            self.active_frame.destroy()
        self.active_frame = ttk.Frame(padding=10)
        self.active_frame.grid()
        return self.active_frame

    def summary_frame(self):
        frame = self.init_frame()
        if summary() is None:
            self.grid_with_padding(ttk.Label(frame, text=f"No items in stock!"), row=0)
        else:
            total_in_stock, unique_items, most_in_stock, least_in_stock = summary()
            self.grid_with_padding(ttk.Label(frame, text=f"Total number of items in stock: {total_in_stock}"), column= 0, row=0)
            self.grid_with_padding(ttk.Label(frame, text=f"Total unique item types: {unique_items}"), column=0, row=1)
            self.grid_with_padding(ttk.Label(frame, text=f"Most stocked item: {most_in_stock}"), column=0, row=2)
            self.grid_with_padding(ttk.Label(frame, text=f"Least stocked item: {least_in_stock}"), column=0, row=3)

    def view_inventory_frame(self):
        frame = self.init_frame()
        if view_inventory() is None:
            ttk.Label(frame, text="Inventory is empty!").grid(row=0)
        else:
            ttk.Label(frame, text="Full Inventory List").grid(row=0, columnspan=2)
            ttk.Label(frame, text="Item").grid(column= 0, row=1)
            ttk.Label(frame, text="Quantity").grid(column= 1, row=1)
            for i, (item, qty) in enumerate(view_inventory()):
                ttk.Label(frame, text=f"{item}").grid(column=0, row=i+2)
                ttk.Label(frame, text=f"{qty}").grid(column=1, row=i+2)

    def view_inventory_history_frame(self):
        frame = self.init_frame()
        if view_inventory() is None:
            ttk.Label(frame, text="Inventory history is empty!").grid(row=0)
        else:
            ttk.Label(frame, text="Full Inventory History List").grid(row=0)
            ttk.Label(frame, text="Item").grid(row=1)
            for i, item in enumerate(view_history_inventory()):
                ttk.Label(frame, text=f"{item}").grid(row=i+1)

    def clear_inventory_frame(self):
        frame = self.init_frame()
        clear_inventory()
        ttk.Label(frame, text="Inventory is now empty!").grid(row=0)

    def export_to_csv_frame(self):
        frame = self.init_frame()
        export_msg = export_csv()
        ttk.Label(frame, text=export_msg).grid(row=0)

    def add_item_frame(self):
        frame = self.init_frame()
        form = ttk.LabelFrame(frame, text="Add Item")
        self.grid_with_padding(form, column=0, row=0)

        self.grid_with_padding(ttk.Label(form, text='Item name: '), column= 0, row=0)
        item_name = ttk.Entry(form)
        item_name.grid(column= 1, row=0)

        self.grid_with_padding(ttk.Label(form, text='Quantity: '), column= 0, row=1)
        item_qty = ttk.Entry(form)
        item_qty.grid(column= 1, row=1)

        def on_add():
            command = add_item(name=get_string(item_name.get()), qty=get_int(item_qty.get()))
            ttk.Label(form, text=f'{command}').grid(row=3, columnspan=2)

        ttk.Button(form, text='Add', command=on_add).grid(row=2, columnspan=2)

    def remove_item_frame(self):
        frame = self.init_frame()
        form = ttk.LabelFrame(frame, text="Remove Item")
        self.grid_with_padding(form, column=0, row=0)

        self.grid_with_padding(ttk.Label(form, text='Item Name: '), column= 0, row=0)
        item_name = ttk.Entry(form)
        item_name.grid(column= 1, row=0)

        self.grid_with_padding(ttk.Label(form, text='Quantity: '), column= 0, row=1)
        item_qty = ttk.Entry(form)
        item_qty.grid(column= 1, row=1)

        def on_remove():
            command = remove_item(name=get_string(item_name.get()), qty=get_int(item_qty.get()))
            ttk.Label(form, text=f'{command}').grid(row=3, columnspan=2)

        ttk.Button(form, text='Remove', command=on_remove).grid(row=2, columnspan=2)
