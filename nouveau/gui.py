from tkinter import *
from fonctions import *

window = Tk()
window.title("Concours de F1")
window.geometry("1280x720")
window.minsize(1280, 720)
window.maxsize(1280, 720)

class Frame():
    def __init__(self):
        self.frame = Frame(window)
        self.elements = []

    def addLabel(self, text, fontfamily, fontsize):
        self.elements.append(Label(self.frame, text=(fontfamily, fontsize))).pack(expand=YES)

def accueil():
    frame = Frame(window)

    Label(frame, text="Bienvenue sur notre programme", font=("Arial", 40)).pack(expand=YES)
    Label(frame, text="Développé par Arthur, JB et Alan", font=("Arial", 20)).pack(expand=YES)

    Button(frame, text="Créer un nouveau concours", font=("Arial", 20), fg='#0000FF', command= lambda: changerFrame(frame, creer_regles)).pack(pady=25)
    frame.pack(expand=YES)
    return frame

def creer_regles():
    frame = Frame(window)

    Label(frame, text="Veuillez entrer le nombre de points par secondes", font=("Arial", 40)).pack(expand=YES)

    timePoints = Entry(frame, font=("Arial", 20), fg='#0000FF')
    timePoints.focus_set()
    timePoints.pack(pady=25)

    Button(frame, text="Valider", font=("Arial", 20), fg='#0000FF', command= lambda: modifier_regles(timePoints.get(), frame, menu_principal)).pack(pady=20)
    frame.pack(expand=YES)
    return frame

def menu_principal():
    frame = Frame(window)

    Label(frame, text="Menu principal", font=("Arial", 40)).pack(expand=YES)

    Button(frame, text="Afficher le classement", font=("Arial", 20), fg='#0000FF', command= lambda: changerFrame(frame, afficher_classement)).pack(pady=25)
    Button(frame, text="Créer une équipe", font=("Arial", 20), fg='#0000FF', command= lambda: changerFrame(frame, creer_equipe)).pack(pady=25)
    Button(frame, text="Créer une voiture", font=("Arial", 20), fg='#0000FF', command= lambda: changerFrame(frame, creer_voiture)).pack(pady=25)
    Button(frame, text="Changer règles", font=("Arial", 20), fg='#0000FF', command= lambda: changerFrame(frame, creer_course)).pack(pady=25)
    
    frame.pack(expand=YES)
    return frame

def creer_equipe_menu():
    frame = Frame(window)

    Label(frame, text="Veuillez sélectionner une équipe", font=("Arial", 40)).pack(expand=YES)
    Button(frame, text="Ajouter une équipe", font=("Arial", 20), fg='#0000FF', command= ajouterEquipe).pack(pady=25)
    Button(frame, text="Supprimer une équipe", font=("Arial", 20), fg='#0000FF', command= supprimerEquipe).pack(pady=25)
    Button(frame, text="Retour", font=("Arial", 20), fg='#0000FF', command= lambda: changerFrame(equipes, menu_principal)).pack(pady=25)
    
    frame.pack(expand=YES)
    return frame

def main():
    menu(window)
    window.mainloop()