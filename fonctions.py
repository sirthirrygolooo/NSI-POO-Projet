import csv
from tkinter import *
from tkinter import filedialog, messagebox
from tkinter_files.fenetre import *
from classes import *


################################## GESTION CONCOURS ##################################

def creer_equipe(nom):
    """Fonction permettant de créer une équipe"""
    concours.equipes.append(Equipe(nom))

def supprimer_equipe(nom, fenetre):
    """Fonction permettant de supprimer une équipe"""
    for equipe in concours.equipes:
        valide = False
        if equipe.nom == nom:
            for i in concours.classement:
                if i[6] == nom:
                    i[6] = None
            concours.equipes.pop(concours.equipes.index(equipe))
            valide = True
        if not valide:
            messageErreur("L'équipe n'existe pas")
        else:
            fenetre.destroy()
        

def supprimer_joueur(nom):
    """Fonction permettant de supprimer un joueur"""
    for joueur in concours.classement:
        if joueur[0] == nom:
            concours.classement.pop(concours.classement.index(joueur))

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

def saveFile():
    """Fonction permettant de sauvegarder le concours"""
    file = filedialog.asksaveasfile(mode='w', defaultextension=".csv")
    if file is None:
        messageErreur('Veuillez recommencer !')
        menu(window)
    else:
        exportInCSV(file)

##### Configuration du menu de la fenêtre #####
def menu(window):
    """Fonction permettant d'afficher la fenêtre d'accueil"""
    menu_bar = Menu(window)
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Ouvrir", command=browseFiles)
    file_menu.add_command(label="Enregistrer", command=saveFile)
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
################################## TKINTER ##################################


############################## FENETRE TKINTER ##############################
def tableau():
    if (len(concours.classement) == 0):
        messageErreur("Il n'y a actuellement aucun participant")
    else:
        fenetre = Tk()
        fenetre.title("Tableau des scores")
        fenetre.maxsize(1280, 720)
        concours.trierclassement()
        for i in range(len(concours.classement)):
            player = concours.classement[i]
            print(f"Concours : {player}")
            if (player[5] == 'o' or player[5] == 'O'):
                entry = Entry(fenetre, width=100, fg='green', font=('Arial',16,'bold'))
            else:
                entry = Entry(fenetre, width=100, fg='red', font=('Arial',16,'bold'))
            entry.grid(row=i, column=1)
            status = "Qualifié !"
            equipe = ""
            if player[6] == None:
                equipe = "Aucune"
            else:
                equipe = player[6] 
            if player[5] != 'o' and player[5] != 'O':
                status = "Disqualifié !"
            siuu = f"{player[1]}.      Nom : {player[0]}     Nombre de Points : {player[2]}      Pénalités : {player[3]}      Total : {player[4]}     Etat : {status}     Equipe : {equipe}"
            entry.insert(END, siuu)
        fenetre.mainloop()

def verificationIsNotEmptyPlayer(entry1, entry2, entry3, entry4, fenetre):
    """Fonction permettant de valider l'ajout d'un joueur"""
    if entry1.get() == "" or not entry2.get().isdigit() or not entry3.get().isdigit() or entry4.get().lower() != "o" and entry4.get().lower() != "n":
        messageErreur("Veuillez vérifier que toutes les valeurs sont valides")
    else:
        for joueur in concours.classement:
            if joueur[0] == entry1.get():
                supprimer_joueur(joueur[0])
        concours.saisieJ(Joueur(entry1.get(), entry2.get(), entry3.get(), entry4.get()))
        fenetre.destroy()

def verificationIsNotEmptyEquipe(entry1, entry2, fenetre):
    """Fonction permettant de valider l'ajout d'une équipe"""
    if entry1.get() == "":
        messageErreur("Veuillez vérifier que toutes les valeurs sont valides")
    else:
        concours.saisieE(Equipe(entry1.get()))
        if entry2.get() != "":
            valide = False
            for i in concours.classement:
                if i[0] == entry2.get():
                    i[6] = entry1.get()
                    valide = True
            if not valide:
                messageErreur("Le joueur n'existe pas")
        fenetre.destroy()

def verificationIsNotEmptyJoueurEquipe(entry1, entry2, fenetre):
    """Fonction permettant de valider l'ajout d'un joueur dans une équipe"""
    if entry1.get() == "" or entry2.get() == "":
        messageErreur("Veuillez vérifier que toutes les valeurs sont valides")
    else:
        valide = False
        for i in concours.equipes:
            if i[0] == entry1.get():
                for j in concours.classement:
                    if j[0] == entry2.get():
                        j.append(entry1.get())
                        i.append(j)
                        valide = True
        if not valide:
            messageErreur("Le joueur/l'équipe n'existe pas")

        fenetre.destroy()

########## Gérer les équipes ##########

def ajouterEquipe():
    """Fonction permettant d'ajouter une équipe"""
    fenetre = Tk()
    fenetre.title("Ajouter une équipe")
    fenetre.maxsize(1280, 720)

    frame = Frame(fenetre)

    Label(frame, width=20, font=('Arial', 20), text="Nom").grid(row=0)
    Label(frame, width=20, font=('Arial', 20), text="Joueurs").grid(row=1)

    entry1 = Entry(frame, width=20, fg='blue', font=('Arial', 20))
    entry2 = Entry(frame, width=20, fg='blue', font=('Arial', 20))
    entry1.grid(row=0, column=1)
    entry2.grid(row=1, column=1)

    valider = Button(frame, text="Valider", command=lambda: verificationIsNotEmptyEquipe(entry1, entry2, fenetre)).grid(row=5, column=0, sticky=W, pady=4)
    annuler = Button(frame, text="Annuler", command=fenetre.destroy).grid(row=5, column=1, sticky=W, pady=4)

    afficherFrame(frame)

# def ajouterJoueurEquipe():
#     """Fonction permettant d'ajouter un joueur à une équipe"""
#     fenetre = Tk()
#     fenetre.title("Ajouter un joueur à une équipe")
#     fenetre.maxsize(1280, 720)

#     frame = Frame(fenetre)

#     Label(frame, width=20, font=('Arial', 20), text="Nom").grid(row=0)
#     Label(frame, width=20, font=('Arial', 20), text="Equipe").grid(row=1)

#     entry1 = Entry(frame, width=20, fg='blue', font=('Arial', 20))
#     entry2 = Entry(frame, width=20, fg='blue', font=('Arial', 20))
#     entry1.grid(row=0, column=1)
#     entry2.grid(row=1, column=1)

#     valider = Button(frame, text="Valider", command=lambda: verificationIsNotEmptyJoueurEquipe(entry1, entry2, fenetre)).grid(row=5, column=0, sticky=W, pady=4)
#     annuler = Button(frame, text="Annuler", command=fenetre.destroy).grid(row=5, column=1, sticky=W, pady=4)

#     afficherFrame(frame)


def supprimerEquipe():
    """Fonction permettant de supprimer une équipe"""
    fenetre = Tk()
    fenetre.title("Supprimer un équipe")
    fenetre.maxsize(1280, 720)

    frame = Frame(fenetre)

    Label(frame, width=20, font=('Arial', 20), text="Nom").grid(row=0)

    entry1 = Entry(frame, width=20, fg='blue', font=('Arial', 20))
    entry1.grid(row=0, column=1)

    valider = Button(frame, text="Valider", command=lambda: supprimer_equipe(entry1.get(), fenetre)).grid(row=5, column=0, sticky=W, pady=4)
    annuler = Button(frame, text="Annuler", command=fenetre.destroy).grid(row=5, column=1, sticky=W, pady=4)

    afficherFrame(frame)
    


########## Gérer les joueurs ##########
def modifierJoueur():
    """Fonction permettant de modifier un joueur"""
    fenetre = Tk()
    fenetre.title("Modifier un joueur")
    fenetre.maxsize(1280, 720)

    frame = Frame(fenetre)
    
    Label(frame, text="Veuillez indiquer le nom du joueur que vous souhaitez modifier")

    name = Entry(frame)
    name.focus_set()
    name.pack(pady=25)

    verifier = Button(frame, text="Vérifier", command= lambda: verification(name)).pack(pady=20)
    annuler = Button(frame, text="Annuler", command=fenetre.destroy).pack(pady=20)

    afficherFrame(frame)

    def verification(name):
        """Fonction permettant de vérifier que le joueur existe"""
        for i in concours.classement:
            if i.getName == name:

                frame = Frame(fenetre)

                Label(frame, width=20, font=('Arial', 20), text="Nom").grid(row=0)
                Label(frame, width=20, font=('Arial', 20), text="Temps (en secondes)").grid(row=1)
                Label(frame, width=20, font=('Arial', 20), text="Penalité").grid(row=2)
                Label(frame, width=20, font=('Arial', 20), text="État [O/N]").grid(row=3)

                entry1 = Entry(frame, width=20, fg='blue', font=('Arial', 20))
                entry2 = Entry(frame, width=20, fg='blue', font=('Arial', 20))
                entry3 = Entry(frame, width=20, fg='blue', font=('Arial', 20))
                entry4 = Entry(frame, width=20, fg='blue', font=('Arial', 20))

                entry1.grid(row=0, column=1)
                entry2.grid(row=1, column=1)
                entry3.grid(row=2, column=1)
                entry4.grid(row=3, column=1)

                valider = Button(frame, text="Valider", command=lambda: verificationIsNotEmptyPlayer(entry1, entry2, entry3, entry4, fenetre)).grid(row=5, column=0, sticky=W, pady=4)
                annuler = Button(frame, text="Annuler", command=lambda: fenetre.destroy).grid(row=5, column=1, sticky=W, pady=4)

                return afficherFrame(frame)

        messageErreur("Le joueur n'existe pas")

def supprimerJoueur():
    """Fonction permettant de supprimer un joueur"""
    fenetre = Tk()
    fenetre.title("Supprimer un joueur")
    fenetre.maxsize(1280, 720)

    frame = Frame(fenetre)
    
    Label(frame, text="Veuillez indiquer le nom du joueur que vous souhaitez supprimer")

    name = Entry(frame)
    name.focus_set()
    name.pack(pady=25)

    verifier = Button(frame, text="Vérifier", command= lambda: verification(name)).pack(pady=20)
    annuler = Button(frame, text="Annuler", command=fenetre.destroy).pack(pady=20)

    afficherFrame(frame)

    def verification(name):
        """Fonction permettant de vérifier que le joueur existe"""
        for i in concours.classement:
            if i.getName == name:
                supprimer_joueur(name)
                return fenetre.destroy()

        messageErreur("Le joueur n'existe pas")

def ajouterJoueur():
    """Fonction permettant d'ajouter un joueur"""
    fenetre = Tk()
    fenetre.title("Ajouter un joueur")
    fenetre.maxsize(1280, 720)

    frame = Frame(fenetre)

    Label(frame, width=20, font=('Arial', 20), text="Nom").grid(row=0)
    Label(frame, width=20, font=('Arial', 20), text="Temps (en secondes)").grid(row=1)
    Label(frame, width=20, font=('Arial', 20), text="Penalité").grid(row=2)
    Label(frame, width=20, font=('Arial', 20), text="État [O/N]").grid(row=3)

    entry1 = Entry(frame, width=20, fg='blue', font=('Arial', 20))
    entry2 = Entry(frame, width=20, fg='blue', font=('Arial', 20))
    entry3 = Entry(frame, width=20, fg='blue', font=('Arial', 20))
    entry4 = Entry(frame, width=20, fg='blue', font=('Arial', 20))

    entry1.grid(row=0, column=1)
    entry2.grid(row=1, column=1)
    entry3.grid(row=2, column=1)
    entry4.grid(row=3, column=1)


    valider = Button(frame, text="Valider", command=lambda: verificationIsNotEmptyPlayer(entry1, entry2, entry3, entry4, fenetre)).grid(row=5, column=0, sticky=W, pady=4)
    annuler = Button(frame, text="Annuler", command=fenetre.destroy).grid(row=5, column=1, sticky=W, pady=4)

    afficherFrame(frame)


############################## FENETRE TKINTER ##############################

################################## CSV ##################################
########### Importation ###########
def importJoueursInCSV(file):
    """Fonction permettant d'importer la liste des joueurs dans un fichier CSV"""
    with open(file.name, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in reader:
            concours.classement.append(Joueur(row[0], row[1], row[2], row[3], row[4]))

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
        concours.classement = []
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
    exportEquipesInCSV(concours.equipes)
    exportRulesInCSV(concours.rules)
################################## CSV ##################################
