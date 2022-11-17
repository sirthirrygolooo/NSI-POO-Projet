import os
from classes import *
# Fonction principale

try :
    import tkinter as tk
except ImportError :
    print('Veuillez installer tkinter')
    os.system('cls & pause')
    exit()

def main():
    pass

def new_player():
    name = input('Entrez le Nom du coureur : ')
    description = input('Entrez l\'écurie du coureur : ')
    results = None # pour l'instant
    points = input('Entrez le nombre de points du coureur : ')
    status = input('Le coureur à-t-il fini la course ? (oui/non) : ')

    if status == 'oui' or status == 'Oui' or status == 'OUI' :
        status = True
    elif status == 'non' or status == 'Non' or status == 'NON' :
        status = False
    else :
        print('Proposition invalide, veuillez recommencer...')
        os.system('cls & pause')
        new_player()

    new = Joueur(name,description,results,points,status)

def manage_team():
    name = input('Nom du joueur à ajouter : ')

    n = Equipe(name)

    


    


