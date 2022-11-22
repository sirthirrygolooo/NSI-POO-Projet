from tkinter import *
from tkinter import messagebox
from src.contest import contest, Player, Team

def errorMessage(message):
    """Fonction permettant d'afficher un message d'erreur"""
    messagebox.showerror("Erreur", message)

def hideFrame(frame):
    """Function to hide a frame
    {frame} -> Object"""
    frame.pack_forget()

def showFrame(frame, expand=True):
    """Function to show a frame
    {frame} -> Object
    {expand} -> Boolean"""
    if expand:
        frame.pack(expand=YES)
    else:
        frame.pack()

def changeFrame(frame1, frame2):
    """Function to swap between 2 different frames
    {frame1} -> Object
    {frame2} -> Object"""
    hideFrame(frame1)
    showFrame(frame2)

def editRules(points, frame1, frame2):
    """Function to change the rules of contest
    {points} -> Integer
    {frame1} -> Object
    {frame2} -> Object"""
    if points is None or not points.isdigit():
        errorMessage("Veuillez entrer un nombre de points valide")
    else:
        contest.rules = points
        changeFrame(frame1, frame2)

def addPlayer(name, points, penalty, state, team, window):
    """Function to add a player to the contest
    {name} -> String
    {points} -> Integer
    {penalty} -> Integer
    {state} -> String
    {team} -> String
    {window} -> Object"""
    print(name, points, penalty, state, team)
    if name == "":
        return errorMessage("Veuillez entrer un nom")
    elif points is None or not points.isdigit():
        return errorMessage("Veuillez entrer un nombre de points valide")
    elif penalty is None or not penalty.isdigit():
        return errorMessage("Veuillez entrer un nombre de pénalités valide")
    elif state.lower() != "o" and state.lower() != "n":
        return errorMessage("L'état doit être O ou N")
    else:
        state = True if state.lower() == "o" else False
        player =Player(name, points, penalty, state)
        contest.addPlayer(player)
        if player == False:
            return errorMessage("Le joueur existe déjà")
        if team:
            teamExist = False
            for i in contest.teams:
                if i.get("name") == team:
                    i.addPlayerInTeam(player)
                    teamExist = True
            if not teamExist:
                team = Team(team)
                team.addPlayerInTeam(player)
                contest.teams.append(team)
        window.destroy()

def removePlayer(name, window):
    """Function to remove a player from the contest"""
    if name == "":
        return errorMessage("Veuillez entrer un nom")
    else:
        playerExist = False
        for player in contest.classement:
            if player.get('name') == name:
                contest.classement.remove(player)
                playerExist = True
                if player.get('team'):
                    for i in contest.teams:
                        if i.get('name') == player.get('team').get('name'):
                            i.removePlayerInTeam(player)
        if playerExist is False:
            return errorMessage("Le joueur n'existe pas") 
        else:
            window.destroy()

def editPlayerCheck(name, frame1, frame2):
    """Function to check if the player exist"""
    if name == "":
        return errorMessage("Veuillez entrer un nom")
    else:
        playerExist = False
        for player in contest.classement:
            if player.get('name') == name:
                playerExist = True
                contest.temp = player
        if playerExist is False:
            return errorMessage("Le joueur n'existe pas")
        else:
            changeFrame(frame1, frame2)

def editPlayer(points, penalty, state, team, window):
    """Function to edit a player from the contest"""
    if points is None or not points.isdigit():
        return errorMessage("Veuillez entrer un nombre de points valide")
    elif penalty is None or not penalty.isdigit():
        return errorMessage("Veuillez entrer un nombre de pénalités valide")
    elif state.lower() != "o" and state.lower() != "n":
        return errorMessage("L'état doit être O ou N")
    else:
        player = contest.temp
        player.set("points", points)
        player.set("penalty", penalty)
        player.set("state", state)
        if not team or team == player.get('team').get('name'):
            pass
        else:
            teamExist = False
            for i in contest.teams:
                if i.get("name") == team:
                    i.addPlayerInTeam(player)
                    teamExist = True
            if not teamExist:
                team = Team(team)
                team.addPlayerInTeam(player)
                contest.teams.append(team)
        contest.temp.delattr()
        window.destroy()

def addTeam(name, window):
    """Function to add a team to the contest"""
    if name == "":
        return errorMessage("Veuillez entrer un nom")
    else:
        teamExist = False
        for team in contest.teams:
            if team.get('name') == name:
                teamExist = True
        if teamExist is False:
            contest.teams.append(Team(name))
            window.destroy()
        else:
            return errorMessage("L'équipe existe déjà")

def removeTeam(name, window):
    """Function to remove a team from the contest"""
    if name == "":
        return errorMessage("Veuillez entrer un nom")
    else:
        teamExist = False
        for team in contest.teams:
            if team.get('name') == name:
                contest.teams.remove(team)
                teamExist = True
        if teamExist is False:
            return errorMessage("L'équipe n'existe pas")
        else:
            window.destroy()