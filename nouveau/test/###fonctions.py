from tkinter import *
from gui import *

###################### TKINTER ######################
def createWindow():
    """Create a window
    {menu} -> Boolean"""
    window = Window("Concours de Voitures", "1280x720", NO)
    return window

def createFileExplorerNavbar():
    """Create a file explorer navbar"""
    navbar = Navbar()
    navbar.addNavbar()
    navbar.addCommand("Ouvrir", command=lambda: print("Ouvrir"))
    navbar.addSeparator()
    navbar.addCommand("Enregistrer", command=lambda: print("Enregistrer"))
    navbar.addCommand("Enregistrer sous", command=lambda: print("Enregistrer sous"))
    navbar.closeNavbar('Fichier')
    return navbar

def welcomeFrame(window):
    frame = Frame()
    frame.addLabel("Bienvenue sur notre programme", "Arial", 40, expand=YES)
    frame.addLabel("Développé par Arthur, JB et Alan", "Arial", 20, expand=YES)
    frame.addButton("Continuer", "Arial", 20, lambda: window.changerFrame(rulesFrame), expand=YES, pady=20)
    return frame

def rulesFrame(window):
    frame = Frame()
    frame.addLabel("Veuillez entrer le nombre de points par secondes", "Arial", 40, expand=YES, pady=20)
    frame.addEntry("Arial", 20, expand=YES, pady=20)
    frame.addButton("Valider", "Arial", 20, lambda: window.changerFrame(mainMenuFrame), expand=YES, pady=20)
    return frame

def mainMenuFrame(window):
    frame = Frame(window)
    frame.addLabel("Menu Principal", "Arial", 40, expand=YES)
    frame.addButton("Afficher le classement", "Arial", 20, lambda: window.changerFrame(classementFrame), expand=YES, pady=20)
    frame.addButton("Gérer les équipes", "Arial", 20, lambda: window.changerFrame(manageTeamFrame), expand=YES, pady=20)
    frame.addButton("Gérer les voitures", "Arial", 20, lambda: window.changerFrame(manageCarFrame), expand=YES, pady=20)
    frame.addButton("Changer les règles", "Arial", 20, lambda: window.changerFrame(rulesFrame), expand=YES, pady=20)
    return frame

def createTeamFrame(window):
    frame = Frame(window)

    Label(frame, text="Veuillez sélectionner une équipe", font=("Arial", 40)).pack(expand=YES)
    Button(frame, text="Ajouter une équipe", font=("Arial", 20), fg='#0000FF', command= ajouterEquipe).pack(pady=25)
    Button(frame, text="Supprimer une équipe", font=("Arial", 20), fg='#0000FF', command= supprimerEquipe).pack(pady=25)
    Button(frame, text="Retour", font=("Arial", 20), fg='#0000FF', command= lambda: changerFrame(equipes, menu_principal)).pack(pady=25)
    
    frame.pack(expand=YES)
    return frame