# Inventory Tracker

A command-line tool for managing inventory: add, remove, view stock, and track historical items. Inventory data is saved between sessions using a JSON file.

## Installation

Clone the repo, then install it locally:
```
pip install -e .
```
---

## Getting Started
1. Make sure you have Python 3.11 installed.
2. Run the following command in your terminal:

```
inventory
```

---

## Command-Line Usage

You can also run the script with optional flags:
- `--summary` -> Show inventory summary and exit
- `--view` -> View current inventory and exit
- `--clear` -> Clear inventory and exit

### Examples:

```
inventory --summary
inventory --view
inventory --clear
```

## Features

- Add and remove items with quantity tracking
- View current stock (sorted alphabetically)
- View all previously stocked item names
- Get a summary of item stats (total, unique, most/least stocked)
- Data is saved between runs using a JSON file
- Input is validated and prompts retry on invalid input
- Colored terminal messages for better UX
---
## Planned Features

- Add unit tests
- Add CSV import/export
- Build a simple GUI on top of the logic
- Add categories or item types
---
## Project Structure

- `main.py` - menu and program runner
- `inventory.py` - inventory functions and file handling
- `inventory_current.json` - data file for saved inventory
---
## Author
Created by Beatrice M. Antoniu