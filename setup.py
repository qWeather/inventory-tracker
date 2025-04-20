from setuptools import setup, find_packages

setup(
    name="inventory-tracker",
    version="0.1.1",
    description="A simple GUI-based inventory tracker in Python.",
    author="Beatrice M. Antoniu",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "inventory": ["data/*.json"],
    },
    entry_points={
        "gui_scripts": [
            "inventory-tracker = inventory.main:main"
        ],
        "console_scripts": [
            "inventory-tracker = inventory.main:main"
        ]
    },
    classifiers=[
        'Programming Language :: Python 3.11',
        'Operating System :: Windows 11',
    ],
    python_requires='>=3.11',
)
