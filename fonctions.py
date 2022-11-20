import csv
from tkinter import *
from tkinter import filedialog, messagebox
from classes import Concours, Equipe, Joueur, concours

################################## GESTION CONCOURS ##################################

def creer_equipe(nom):
    """Fonction permettant de créer une équipe"""
    concours.equipes.append(Equipe(nom))

def supprimer_equipe(nom):
    """Fonction permettant de supprimer une équipe"""
    for equipe in concours.equipes:
        if equipe.nom == nom:
            concours.equipes.remove(equipe)

def supprimer_joueur(nom):
    """Fonction permettant de supprimer un joueur"""
    for joueur in concours.joueurs:
        if joueur.nom == nom:
            concours.joueurs.remove(joueur)

def modifier_regles(points, frame1, frame2):
    """Fonction permettant de modifier les règles du concours"""
    if points == None or not points.isdigit():
        messageErreur("Veuillez entrer un nombre de points valide")
    else:   
        concours.rules = points
        changerFrame(frame1, frame2)
################################## GESTION CONCOURS ##################################


##################################### TKINTER #####################################
##### Sélection du fichier CSV #####
def browseFiles():
    """Fonction permettant de parcourir les fichiers et de retourner le contenu d'un fichier CSV"""
    file = filedialog.askopenfile(mode='r', title="Select file", filetypes=(("CSV Files","*.csv"),))
    if file is not None:
        importInCSV(file)
    return None

##### Configuration du menu de la fenêtre #####
def menu(window):
    """Fonction permettant d'afficher la fenêtre d'accueil"""
    menu_bar = Menu(window)
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Nouveau", command=browseFiles)
    file_menu.add_command(label="Ouvrir", command=browseFiles)
    file_menu.add_command(label="Enregistrer", command=browseFiles)
    file_menu.add_command(label="Enregistrer sous...", command=browseFiles)
    file_menu.add_separator()
    file_menu.add_command(label="Quitter", command=window.destroy)
    menu_bar.add_cascade(label="Fichier", menu=file_menu)
    window.config(menu=menu_bar)
    window.mainloop()

def masquerFrame(frame):
    """Fonction permettant de masquer un frame"""
    frame.pack_forget()

def afficherFrame(frame, expand=True):
    """Fonction permettant d'afficher un frame"""
    if expand:
        frame.pack(expand=YES)
    else:
        frame.pack()

def changerFrame(frame1, frame2):
    """Fonction permettant de changer de frame"""
    masquerFrame(frame1)
    afficherFrame(frame2)

def messageErreur(message):
    """Fonction permettant d'afficher un message d'erreur"""
    messagebox.showerror("Erreur", message)

def tableau():
    if (len(concours.classement) == 0):
        messageErreur("Il n'y a actuellement aucun participant")
    else:
        tableau = Tk()
        tableau.title("Tableau des scores")
        for i in range(len(concours.classement)):
            for j in range(5):
                label = Label(tableau, width=20, fg='blue', font=('Arial',16,'bold'))
                label.grid(row=i, column=j)
                label.insert(END, concours.classement[i][j])
        tableau.mainloop()
################################## TKINTER ##################################


################################## CSV ##################################
########### Importation ###########
def importJoueursInCSV(file):
    """Fonction permettant d'importer la liste des joueurs dans un fichier CSV"""
    with open(file.name, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in reader:
            Concours.joueurs.append(Joueur(row[0], row[1], row[2], row[3], row[4]))

def importEquipesInCSV(file):
    """Fonction permettant d'importer la liste des équipes dans un fichier CSV"""
    with open(file.name, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in reader:
            Concours.equipes.append(Equipe(row[0], row[1]))

def importRulesInCSV(file):
    """Fonction permettant d'importer les règles du concours dans un fichier CSV"""
    with open(file.name, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in reader:
            Concours.rules = row[0]

def importInCSV(file):
    """Fonction permettant d'importer les données du concours dans un fichier CSV"""
    with open(file.name, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        Concours.joueurs = []
        Concours.equipes = []
        for row in reader:
            if row[4]:
                exportJoueursInCSV(Concours)
            elif row[1]:
                exportEquipesInCSV(Equipe)
            elif row[0]:
                exportRulesInCSV(Concours)
            else:
                print("Erreur lors de l'importation du fichier")

########### Exportation ###########
def exportEquipesInCSV(file):
    """Fonction permettant d'exporter la liste des équipes dans un fichier CSV"""
    with open(file.csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for equipe in Equipe:
            writer.writerow([equipe.nom, equipe.joueurs])

def exportJoueursInCSV(Concours):
    """Fonction permettant d'exporter la liste des joueurs dans un fichier CSV"""
    with open('joueurs.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for joueur in Concours.classement:
            writer.writerow([joueur.nom, joueur.description, joueur.resultats, joueur.points, joueur.etat])

def exportRulesInCSV(Concours):
    """Fonction permettant d'exporter les règles du concours dans un fichier CSV"""
    with open('rules.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([Concours.rules])

def exportInCSV(file):
    """Fonction permettant d'exporter les données du concours dans un fichier CSV"""
    exportJoueursInCSV(file)
    exportEquipesInCSV(file)
    exportRulesInCSV(file)
################################## CSV ##################################