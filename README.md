# Inventory Tracker

A Python GUI app for managing inventory: add, remove, view stock, track historical items, and export data.  
Inventory data is saved between sessions using a JSON file.

---

## Getting Started

1. **Install Python 3.11**  
2. **Clone this repository:**
   ```
   git clone https://github.com/qWeather/inventory-tracker.git
   cd inventory-tracker
   ```
## Install dependencies (optional, if using virtualvenv):
```
pip install -r requirements.txt
```

## Run the app:
```
inventory
```

## Features
- Add and remove items with quantity tracking
- View current inventory and inventory history
- Get summary statistics
- Export current inventory to CSV
- Data persistence via JSON file
- Clean, user-friendly Tkinter GUI

Project Structure
```
inventory-tracker/

	inventory/              # Core package
		__init__.py
		core.py             # Business logic
		main.py				# Entry point
		ui/gui.py           # Tkinter GUI
		lib/utilities.py    # Helpers and formatting
	tests/                  # Unit tests
		__init__.py
		test_core.py
	inventory_current.json  # Saved data
	inventory_current.csv   # Optional export
	README.md
	setup.py
	.pre-commit-config.yaml
```

## Testing
This project uses **unittest** for test coverage.
To run tests:
```
python -m unittest discover -s tests -p "test_*.py"
```

## Pre-commit Hook (Optional but Recommended)
Use pre-commit to automatically run tests before each commit.
Setup:
1. Install:
```
pip install pre-commit
```
2. Install hooks:
```
pre-commit install
```
Now every time you commit, unit tests will automatically run.
If any test fails, the commit will be blocked.

## Planned Features
- CSV import
- Dark/light theme toggle for GUI
- Search inventory items
- Undo last action
- More robust error feedback in the GUI

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
Created by Beatrice M. Antoniu