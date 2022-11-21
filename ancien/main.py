import os

from tkinter_files.fenetre import afficher_fenetre

try :
    import tkinter as tk
except ImportError :
    print('Veuillez installer tkinter')
    os.system('cls & pause')
    exit()

afficher_fenetre()