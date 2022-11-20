from classes import Concours
import os

from sys import path
path.insert(1, './tkinter')
from fenetre import afficher_fenetre

try :
    import tkinter as tk
except ImportError :
    print('Veuillez installer tkinter')
    os.system('cls & pause')
    exit()

afficher_fenetre()












    


    


