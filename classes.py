from tkinter import Entry, END, Button

class Joueur:
    def __init__(self, nom, points, penalite, etat):
        self.nom = nom
        self.resultats = None
        self.points = points
        self.penalite = penalite
        self.etat = etat
    
    def getName(self):
        nom = self.nom
        return nom
    
    def getPoints(self):
        points = self.points
        return points
    
    def getPenalite(self):
        penalite = self.penalite
        return penalite
    
    def getEtat(self):
        etat = self.etat
        return etat

class Equipe:
    def __init__(self, nom):
        self.joueurs = []
        self.nom = nom

    def listeJoueurs(self):
        listeJoueurs = []
        for joueur in self.joueurs:
            listeJoueurs.append(joueur.getName())
        return listeJoueurs

    def ajouterJoueur(self, Joueur):
        return self.joueurs.append(Joueur)


class Concours:
    def __init__(self):
        self.classement = []
        self.disqualifie = []
        self.joueurs = []
        self.equipes = []
        self.rules = None

    def __classement__(self):
        self.classement.sort(key=lambda a: ((a[3]*self.rules)+a[4]))
        for i in range(len(self.classement)):
            self.classement[i].resultats = i+1

    def modif(self, pointsPerSeconds):
        self.rules = pointsPerSeconds

    def recl(self, Joueur):
        p = Joueur
        if p.etat == False:
            p.etat = True
        else:
            p.etat = False
        
    def chercherJoueur(self, nom):
        for i in self.classement:
            if i.nom == nom:
                return i
        return None

    def saisieJ(self, Joueur):
        if Joueur.etat == 'o':
            self.classement.append(Joueur)
        else:
            self.disqualifie.append(Joueur)
        self.joueurs.append(Joueur)


concours = Concours()
