from setuptools import setup, find_packages

setup(
    name='inventory-tracker',
    version='0.1.0',
    author='Beatrice M. Antoniu',
    description='A CLI tool to track and manage inventory with persistent storage.',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'inventory=inventory.main:main',
        ],   
    },
    classifiers=[
        'Programming Language :: Python 3.11',
        'Operating System :: Windows 11',
    ],
    python_requires='>=3.11',
)