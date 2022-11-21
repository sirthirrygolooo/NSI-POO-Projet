from tkinter import *

from fonctions import *

# Paramètres de la fenêtre
window = Tk()
window.title("Concours de F1")
window.geometry("1280x720")
window.minsize(1280, 720)
window.maxsize(1280, 720)


################################## ACCUEIL ##################################
accueil = Frame(window)

##### Message d'accueil #####
message = Label(accueil, text="Bienvenue sur notre programme", font=("Arial", 40)).pack(expand=YES)
copyright = Label(accueil, text="Développé par Arthur, JB et Alan", font=("Arial", 20)).pack(expand=YES)

##### Boutton pour créer un nouveau concours #####
button = Button(accueil, text="Créer un nouveau concours", font=("Arial", 20), fg='#0000FF', command= lambda: changerFrame(accueil, creer_regles)).pack(pady=25)
accueil.pack(expand=YES)
################################## ACCUEIL ##################################


################################## CREER CONCOURS ##################################
creer_regles = Frame(window)

message = Label(creer_regles, text="Veuillez entrer le nombre de points par secondes", font=("Arial", 40)).pack(expand=YES)

timePoints = Entry(creer_regles, font=("Arial", 20), fg='#0000FF')
timePoints.focus_set()
timePoints.pack(pady=25)

button = Button(creer_regles, text="Valider", font=("Arial", 20), fg='#0000FF', command= lambda: modifier_regles(timePoints.get(), creer_regles, menu_principal)).pack(pady=20)
################################## CREER CONCOURS ##################################


##################################### MENU PRINCIPAL #####################################
menu_principal = Frame(window)

message = Label(menu_principal, text="Veuillez sélectionner une option ci-dessous", font=("Arial", 40)).pack(expand=YES)

afficherTableau = Button(menu_principal, text="Afficher le tableau", font=("Arial", 20), fg='#0000FF', command= tableau).pack(pady=25)
equipes = Button(menu_principal, text="Gérer les équipes", font=("Arial", 20), fg='#0000FF', command= lambda: changerFrame(menu_principal, equipes)).pack(pady=25)
joueurs = Button(menu_principal, text="Gérer les joueurs", font=("Arial", 20), fg='#0000FF', command= lambda: changerFrame(menu_principal, joueurs)).pack(pady=25)
regles = Button(menu_principal, text="Gérer les règles", font=("Arial", 20), fg='#0000FF', command= lambda: changerFrame(menu_principal, creer_regles)).pack(pady=25)
quitter = Button(menu_principal, text="Quitter", font=("Arial", 20), fg='#0000FF', command= lambda: window.destroy()).pack(pady=25)
##################################### MENU PRINCIPAL #####################################



################################## GERER LES EQUIPES ##################################
equipes = Frame(window)

message = Label(equipes, text="Veuillez sélectionner une option ci-dessous", font=("Arial", 40)).pack(expand=YES)

ajouter = Button(equipes, text="Ajouter une équipe", font=("Arial", 20), fg='#0000FF', command= ajouterEquipe).pack(pady=25)
supprimer = Button(equipes, text="Supprimer une équipe", font=("Arial", 20), fg='#0000FF', command= supprimerEquipe).pack(pady=25)
retour = Button(equipes, text="Retour", font=("Arial", 20), fg='#0000FF', command= lambda: changerFrame(equipes, menu_principal)).pack(pady=25)
################################## GERER LES EQUIPES ##################################


################################## GERER LES JOUEURS ##################################
joueurs = Frame(window)

message = Label(joueurs, text="Veuillez sélectionner une option ci-dessous", font=("Arial", 40)).pack(expand=YES)

ajouter = Button(joueurs, text="Ajouter un joueur", font=("Arial", 20), fg='#0000FF', command= ajouterJoueur).pack(pady=25)
modifier = Button(joueurs, text="Modifier un joueur", font=("Arial", 20), fg='#0000FF', command= modifierJoueur).pack(pady=25)
supprimer = Button(joueurs, text="Supprimer un joueur", font=("Arial", 20), fg='#0000FF', command= supprimerJoueur).pack(pady=25)
retour = Button(joueurs, text="Retour", font=("Arial", 20), fg='#0000FF', command= lambda: changerFrame(joueurs, menu_principal)).pack(pady=25)
################################## GERER LES JOUEURS ##################################

menu(window)

# Lancement de la fenêtre
def afficher_fenetre():
    window.mainloop()

