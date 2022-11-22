from tkinter import *
from fonctions import *

# Settings for the window
window = Tk()
window.title("Concours de voitures")
window.geometry("1280x720")
window.resizable(width=NO, height=NO)

# Settings for the navbar
menu_bar = Menu(window)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Ouvrir", command=browseFiles)
file_menu.add_command(label="Enregistrer", command=saveFile)
menu_bar.add_cascade(label="Fichier", menu=file_menu)
window.config(menu=menu_bar)

def homeFrame():
    # Settings for the frame
    frame = Frame(window)
    frame.pack(expand=YES)

    # Settings for the widgets
    Label(frame, text="Bienvenue sur notre programme", font=("Arial", 40)).pack(expend=YES)

    # Settings for the buttons
    button = Button(frame, text="Commencer", font=("Arial", 16), command=gameFrame)
    button.pack(expand=YES)
