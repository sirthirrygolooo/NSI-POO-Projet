import os

from src.gui import start

try:
    import tkinter as tk
except ImportError:
    print('Veuillez installer Tkinter')
    os.system('cls & pause')
    exit()

start()