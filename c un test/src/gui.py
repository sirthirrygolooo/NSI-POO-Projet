from tkinter import *
from src.fonctions import *
from src.contest import contest

window = Tk()
window.title('Concours de F1')
window.geometry('1280x720')
window.minsize(1280, 720)
window.maxsize(1280, 720)

def homeFrame():
    frame = Frame(window)
    
    Label(frame, text="Bienvenue sur notre programme", font=('Arial', 40)).pack(expand=YES)
    Label(frame, text="Développé par Alan, JB et Arthur", font=('Arial', 20)).pack(expand=YES)
    Button(frame, text="Créer un nouveau concours", font=("Arial", 20), fg='#0000FF', command= lambda: changeFrame(frame, rulesFrame())).pack(pady=25)
    
    return frame

def rulesFrame():
    frame = Frame(window)

    Label(frame, text="Veuillez entrer le nombre de points par secondes", font=("Arial", 40)).pack(expand=YES)
    timePoints = Entry(frame, font=("Arial", 20), fg='#0000FF')
    timePoints.focus_set()
    timePoints.pack(pady=25)
    Button(frame, text="Valider", font=("Arial", 20), fg='#0000FF', command=lambda: editRules(timePoints.get(), frame, mainMenuFrame())).pack(pady=20)
    
    return frame

def mainMenuFrame():
    frame = Frame(window)

    Label(frame, text="Veuillez sélectionner une option ci-dessous", font=("Arial", 40)).pack(expand=YES)
    Button(frame, text="Afficher le tableau", font=("Arial", 20), fg='#0000FF', command= tableauWindow).pack(pady=25)
    Button(frame, text="Gérer les équipes", font=("Arial", 20), fg='#0000FF', command= lambda: changeFrame(frame, manageTeamFrame())).pack(pady=25)
    Button(frame, text="Gérer les joueurs", font=("Arial", 20), fg='#0000FF', command= lambda: changeFrame(frame, managePlayerFrame())).pack(pady=25)
    Button(frame, text="Gérer les règles", font=("Arial", 20), fg='#0000FF', command= lambda: changeFrame(frame, rulesFrame())).pack(pady=25)
    Button(frame, text="Quitter", font=("Arial", 20), fg='#0000FF', command= lambda: window.destroy()).pack(pady=25)

    return frame


################################################################################
################################ SHOW LEADERBOARD ##############################
################################################################################
def tableauWindow():
    if (len(contest.classement) == 0):
        errorMessage("Il n'y a actuellement aucun participant")
    else:

        tableauWindow = Tk()
        tableauWindow.title("Tableau des scores")
        tableauWindow.geometry("1500x800")
        tableauWindow.minsize(1500, 800)
        tableauWindow.maxsize(1500, 800)

        contest.sortClassement()
        for i in range(len(contest.classement)):
            player = contest.classement[i]
            player.set('classification', i+1)
            status = None
            if (player.get('state') is True):
                entry = Entry(tableauWindow, width=100, fg='green', font=('Arial',16,'bold'))
                status = "Qualifié"
            else:
                entry = Entry(tableauWindow, width=100, fg='red', font=('Arial',16,'bold'))
                status = "Disqualifié"
            entry.grid(row=i, column=1)

            equipe = None
            if player.get('team') is not None:
                equipe = player.get('team').get('name')
            else:
                equipe = "Aucune"
            
            stats = f"{player.get('classification')}.      Nom : {player.get('name')}     Nombre de Points : {player.get('points')}      Pénalités : {player.get('penalty')}      Total : {player.get('total')}     Equipe : {equipe}     Etat : {status}"
            entry.insert(END, stats)
        tableauWindow.mainloop()
################################################################################
################################ SHOW LEADERBOARD ##############################
################################################################################


################################################################################
################################ MANAGE PLAYER #################################
################################################################################
def managePlayerFrame():
    frame = Frame(window)

    Label(frame, text="Veuillez sélectionner une option ci-dessous", font=("Arial", 40)).pack(expand=YES)
    Button(frame, text="Ajouter un joueur", font=("Arial", 20), fg='#0000FF', command= addPlayerWindow).pack(pady=25)
    Button(frame, text="Modifier un joueur", font=("Arial", 20), fg='#0000FF', command= editPlayerWindow).pack(pady=25)
    Button(frame, text="Supprimer un joueur", font=("Arial", 20), fg='#0000FF', command= removePlayerWindow).pack(pady=25)
    Button(frame, text="Afficher les joueurs", font=("Arial", 20), fg='#0000FF', command= showAllPlayersWindow).pack(pady=25)
    Button(frame, text="Retour", font=("Arial", 20), fg='#0000FF', command= lambda: changeFrame(frame, mainMenuFrame())).pack(pady=25)

    return frame

def showAllPlayersWindow():
    if (len(contest.players) == 0):
        errorMessage("Il n'y a actuellement aucun participant")
    else:
        showAllPlayersWindow = Tk()
        showAllPlayersWindow.title("Liste des joueurs")
        showAllPlayersWindow.geometry("1500x800")
        showAllPlayersWindow.minsize(1500, 800)
        showAllPlayersWindow.maxsize(1500, 800)

        for i in range(len(contest.players)):
            player = contest.players[i]
            entry = Entry(showAllPlayersWindow, width=100, fg='green', font=('Arial',16,'bold'))
            entry.grid(row=i, column=1)

            equipe = None
            if player.get('team') is not None:
                equipe = player.get('team')
            else:
                equipe = "Aucune"
            
            stats = f"Nom : {player.get('name')}      Equipe : {equipe}"
            entry.insert(END, stats)
        showAllPlayersWindow.mainloop()

def addPlayerWindow():
    addPlayerWindow = Tk()
    addPlayerWindow.title("Ajouter un joueur")
    addPlayerWindow.geometry("800x800")
    addPlayerWindow.minsize(800, 800)
    addPlayerWindow.maxsize(800, 800)

    frame = Frame(addPlayerWindow)

    Label(frame, width=20, font=('Arial', 20), text="Nom").grid(row=0)
    Label(frame, width=20, font=('Arial', 20), text="Temps (en secondes)").grid(row=1)
    Label(frame, width=20, font=('Arial', 20), text="Penalité").grid(row=2)
    Label(frame, width=20, font=('Arial', 20), text="État [O/N]").grid(row=3)
    Label(frame, width=20, font=('Arial', 20), text="Nom de l'équipe").grid(row=4)

    playerName = Entry(frame, width=20, fg='blue', font=('Arial', 20))
    playerPoints = Entry(frame, width=20, fg='blue', font=('Arial', 20))
    playerPenalty = Entry(frame, width=20, fg='blue', font=('Arial', 20))
    playerState = Entry(frame, width=20, fg='blue', font=('Arial', 20))
    playerTeamName = Entry(frame, width=20, fg='blue', font=('Arial', 20))

    playerName.grid(row=0, column=1)
    playerPoints.grid(row=1, column=1)
    playerPenalty.grid(row=2, column=1)
    playerState.grid(row=3, column=1)
    playerTeamName.grid(row=4, column=1)

    Button(frame, text="Valider", command=lambda: addPlayer(playerName.get(), playerPoints.get(), playerPenalty.get(), playerState.get(), playerTeamName.get(), addPlayerWindow)).grid(row=5, column=0, sticky=W, pady=4)
    Button(frame, text="Annuler", command=addPlayerWindow.destroy).grid(row=5, column=1, sticky=W, pady=4)

    frame.pack()

    return addPlayerWindow.mainloop()

def editPlayerWindow():
    editPlayerWindow = Tk()
    editPlayerWindow.title("Modifier un joueur")
    editPlayerWindow.geometry("800x800")
    editPlayerWindow.minsize(800, 800)
    editPlayerWindow.maxsize(800, 800)

    frame = Frame(editPlayerWindow)

    Label(frame, width=20, font=('Arial', 20), text="Veuillez entrer le nom du joueur").pack(expand=YES)
    name = Entry(frame, width=20, fg='blue', font=('Arial', 20))
    name.focus_set()
    name.pack(pady=25)
    Button(frame, text="Rechercher", command=lambda: editPlayerCheck(name.get(), frame, editPlayerFrame())).pack(expand=YES)

    frame.pack()

    editPlayerWindow.mainloop()
    return editPlayerWindow

def editPlayerFrame():

    frame = Frame(editPlayerWindow())

    player = contest.temp

    Label(frame, width=20, font=('Arial', 20), text="Nom").grid(row=0)
    Label(frame, width=20, font=('Arial', 20), text="Temps (en secondes)").grid(row=1)
    Label(frame, width=20, font=('Arial', 20), text="Penalité").grid(row=2)
    Label(frame, width=20, font=('Arial', 20), text="État [O/N]").grid(row=3)
    Label(frame, width=20, font=('Arial', 20), text="Nom de l'équipe").grid(row=4)

    playerPoints = Entry(frame, width=20, fg='blue', font=('Arial', 20)).insert(END, player.getPoints())
    playerPenalty = Entry(frame, width=20, fg='blue', font=('Arial', 20)).insert(END, player.getPenalty())
    playerState = Entry(frame, width=20, fg='blue', font=('Arial', 20)).insert(END, player.getState())
    playerTeamName = Entry(frame, width=20, fg='blue', font=('Arial', 20)).insert(END, player.getTeamName())

    playerPoints.grid(row=1, column=1)
    playerPenalty.grid(row=2, column=1)
    playerState.grid(row=3, column=1)
    playerTeamName.grid(row=4, column=1)

    Button(frame, text="Valider", command=lambda: editPlayer(playerPoints.get(), playerPenalty.get(), playerState.get(), playerTeamName.get(), editPlayerWindow)).grid(row=5, column=0, sticky=W, pady=4)
    Button(frame, text="Annuler", command=editPlayerWindow.destroy).grid(row=5, column=1, sticky=W, pady=4)

    frame.pack()

    return frame

def removePlayerWindow():
    removePlayerWindow = Tk()
    removePlayerWindow.title("Supprimer un joueur")
    removePlayerWindow.geometry("800x800")
    removePlayerWindow.minsize(800, 800)
    removePlayerWindow.maxsize(800, 800)

    frame = Frame(removePlayerWindow)

    Label(frame, width=20, font=('Arial', 20), text="Nom").grid(row=0)
    playerName = Entry(frame, width=20, fg='blue', font=('Arial', 20))
    playerName.grid(row=0, column=1)

    Button(frame, text="Valider", command=lambda: removePlayer(playerName.get(), removePlayerWindow)).grid(row=5, column=0, sticky=W, pady=4)
    Button(frame, text="Annuler", command=removePlayerWindow.destroy).grid(row=5, column=1, sticky=W, pady=4)

    frame.pack()

    removePlayerWindow.mainloop()
################################################################################
################################ MANAGE PLAYER #################################
################################################################################


################################################################################
################################# MANAGE TEAMS #################################
################################################################################
def manageTeamFrame():
    frame = Frame(window)

    Label(frame, text="Veuillez sélectionner une option ci-dessous", font=("Arial", 40)).pack(expand=YES)
    Button(frame, text="Créer une équipe", font=("Arial", 20), fg='#0000FF', command= addTeamWindow).pack(pady=25)
    Button(frame, text="Supprimer une équipe", font=("Arial", 20), fg='#0000FF', command= removeTeamWindow).pack(pady=25)
    Button(frame, text="Afficher les équipes", font=("Arial", 20), fg='#0000FF', command= showAllTeams).pack(pady=25)
    Button(frame, text="Retour", font=("Arial", 20), fg='#0000FF', command= lambda: changeFrame(frame, mainMenuFrame())).pack(pady=25)

    return frame

def addTeamWindow():
    teamWindow = Tk()
    teamWindow.title("Ajouter une équipe")
    teamWindow.geometry("1280x720")
    teamWindow.minsize(1280, 720)
    teamWindow.maxsize(1280, 720)

    frame = Frame(teamWindow)

    Label(frame, width=20, font=('Arial', 20), text="Nom de l'équipe").grid(row=0)
    entry = Entry(frame, width=20, fg='blue', font=('Arial', 20))
    entry.grid(row=0, column=1)
    Button(frame, text="Valider", command=lambda: addTeam(entry.get(), teamWindow)).grid(row=5, column=0, sticky=W, pady=4)
    Button(frame, text="Annuler", command=teamWindow.destroy).grid(row=5, column=1, sticky=W, pady=4)

    frame.pack()
    teamWindow.mainloop()

def removeTeamWindow():
    teamWindow = Tk()
    teamWindow.title("Supprimer une équipe")
    teamWindow.geometry("1280x720")
    teamWindow.minsize(1280, 720)
    teamWindow.maxsize(1280, 720)

    frame = Frame(teamWindow)

    Label(frame, width=20, font=('Arial', 20), text="Nom de l'équipe").grid(row=0)
    entry = Entry(frame, width=20, fg='blue', font=('Arial', 20))
    entry.grid(row=0, column=1)
    Button(frame, text="Valider", command=lambda: removeTeam(entry.get(), teamWindow)).grid(row=5, column=0, sticky=W, pady=4)
    Button(frame, text="Annuler", command=teamWindow.destroy).grid(row=5, column=1, sticky=W, pady=4)

    frame.pack()
    teamWindow.mainloop()

def showAllTeams():
    if (len(contest.teams) == 0):
        errorMessage("Il n'y a actuellement aucune équipe")
    else:

        tableauWindow = Tk()
        tableauWindow.title("Liste des équipes")
        tableauWindow.geometry("1500x800")
        tableauWindow.minsize(1500, 800)
        tableauWindow.maxsize(1500, 800)

        entry = Entry(tableauWindow, width=20, fg='blue', font=('Arial', 20))

        for i in range(len(contest.teams)):
            team = contest.teams[i]
            listPlayers = team.get('listPlayers')
            print(team.get('name'))
            row = team.get('name') + f" | {len(listPlayers)} Participant(s) : "
            for player in listPlayers:
                row += "      " + player.get('name')
            
            entry.insert(END, row)

        tableauWindow.mainloop()
################################################################################
################################# MANAGE TEAMS #################################
################################################################################


def start():
    homeFrame().pack(expand=YES)
    window.mainloop()
