from tkinter import *
from  tkinter import ttk
from tkinter import messagebox
from inventory.core import (
    view_history_inventory, view_inventory, add_item, remove_item,
    summary, export_csv, clear_inventory
)
from inventory.lib.utilities import get_string, get_int

root = Tk()
style = ttk.Style()


class InventoryTrackerApp(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        root.title("Inventory Tracker")
        root.minsize(width=500, height=400)
        root.columnconfigure(0, weight=1)
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
        frame.columnconfigure(0, weight=1)
        self.init_style(frame)
        self.grid_with_padding(ttk.Label(frame, text="Welcome to Inventory Tracker"), row=1, columnspan=3)
        self.menu_buttons_view(frame)

    def init_frame(self):
        if self.active_frame:
            self.active_frame.destroy()
        self.active_frame = ttk.Frame(padding=10)
        self.active_frame.grid()
        return self.active_frame

    def init_style(self, frame):
        style.configure('Bold.TLabel', font=('Segoe UI', 10, 'bold'))
        self.grid_with_padding(ttk.Label(frame, text="Choose Theme:"), column=0, row=0)
        style_var = StringVar()
        style_choose = ttk.Combobox(frame, textvariable=style_var, state="readonly")
        style_choose['values'] = ('default', 'vista','clam', 'alt')
        style_choose.current(0)
        self.grid_with_padding(style_choose, column=1, row=0)

        def change_theme(event):
            selected = style_var.get()
            try:
                style.theme_use(selected)
            except TclError:
                messagebox.showerror("Error", f"Theme '{selected}' not supported.")
        style_choose.bind("<<ComboboxSelected>>", change_theme)

    def grid_with_padding(self, widget, **grid_options):
        grid_options.setdefault('padx', 5)
        grid_options.setdefault('pady', 5)
        widget.grid(**grid_options)

    def btn_grid_with_padding(self, widget, **grid_options):
        grid_options.setdefault('padx', 5)
        grid_options.setdefault('pady', 5)
        grid_options.setdefault('sticky', "ew")
        widget.grid(**grid_options)

    def menu_buttons_view(self, frame):
        buttons_frame_1 = ttk.Frame(frame)
        buttons_frame_1.grid(column=0, row=2, columnspan=3, sticky="ew")
        for i in range(3):
            buttons_frame_1.columnconfigure(i, weight=1)
        self.btn_grid_with_padding(ttk.Button(buttons_frame_1, text="Add Item", command=self.add_item_frame), column=0, row=0)
        self.btn_grid_with_padding(ttk.Button(buttons_frame_1, text="Remove Item", command=self.remove_item_frame), column=1, row=0)
        self.btn_grid_with_padding(ttk.Button(buttons_frame_1, text="Clear Inventory", command=self.clear_inventory_frame), column=2, row=0)
        
        buttons_frame_2 = ttk.Frame(frame)
        buttons_frame_2.grid(column=0, row=3, columnspan=3, sticky="ew")
        for i in range(3):
            buttons_frame_2.columnconfigure(i, weight=1)
        self.btn_grid_with_padding(ttk.Button(buttons_frame_2, text="View Inventory", command=self.view_inventory_frame), column=0, row=1)
        self.btn_grid_with_padding(ttk.Button(buttons_frame_2, text="View all previously stocked items", command=self.view_inventory_history_frame), column=1, row=1)
        self.btn_grid_with_padding(ttk.Button(buttons_frame_2, text="Summary", command=self.summary_frame), column=2, row=1)

        buttons_frame_3 = ttk.Frame(frame)
        buttons_frame_3.grid(column=0, row=4, columnspan=3)
        buttons_frame_3.columnconfigure(1, weight=1)
        self.btn_grid_with_padding(ttk.Button(buttons_frame_3, text="Export current inventory to csv", command=self.export_to_csv_frame), column=0, row=4)

        buttons_frame_4 = ttk.Frame(frame)
        buttons_frame_4.grid(column=0, row=5, columnspan=3)
        buttons_frame_4.columnconfigure(1, weight=1)
        self.btn_grid_with_padding(ttk.Button(buttons_frame_4, text="Exit", command=root.destroy), column=0, row=5)

    def summary_frame(self):
        frame = self.init_frame()
        if summary() is None:
            self.grid_with_padding(ttk.Label(frame, text=f"No items in stock!"), row=0)
        else:
            total_in_stock, unique_items, most_in_stock, least_in_stock = summary()
            style.configure('Bold.TLabel', font=('TkDefaultFont', 10, 'bold'))
            self.grid_with_padding(ttk.Label(frame, text=f"Total number of items in stock: {total_in_stock}", style='Bold.TLabel'), column= 0, row=0)
            self.grid_with_padding(ttk.Label(frame, text=f"Total unique item types: {unique_items}", style='Bold.TLabel'), column=0, row=1)
            self.grid_with_padding(ttk.Label(frame, text=f"Most stocked item: {most_in_stock}", style='Bold.TLabel'), column=0, row=2)
            self.grid_with_padding(ttk.Label(frame, text=f"Least stocked item: {least_in_stock}", style='Bold.TLabel'), column=0, row=3)

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
        clear_inventory()
        messagebox.showinfo("Info", "Inventory is now empty!")

    def export_to_csv_frame(self):
        export_msg = export_csv()
        messagebox.showifo("Success", export_msg)

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
            if item_name.get() != "" and item_qty.get() != "" and not item_qty.get().__contains__('-') and item_qty.get() != '0':
                command = add_item(name=get_string(item_name.get()), qty=get_int(item_qty.get()))
                messagebox.showinfo("Info", command)
                self.view_inventory_frame()
            else:
                messagebox.showerror("Invalid input", "Item name and quantity are required. \nQuantity must be a positive number.")

        self.btn_grid_with_padding(ttk.Button(form, text='Add', command=on_add), row=2, columnspan=2)

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
            if item_name.get() != "" and item_qty.get() != "" and not item_qty.get().__contains__('-') and item_qty.get() != '0':
                command = remove_item(name=get_string(item_name.get()), qty=get_int(item_qty.get()))
                messagebox.showinfo("Info", command)
                self.view_inventory_frame()
            else:
                messagebox.showerror("Invalid input", "Item name and quantity are required. \nQuantity must be a positive number. \nItem must be in inventory!")

        self.btn_grid_with_padding(ttk.Button(form, text='Remove', command=on_remove), row=2, columnspan=2)
