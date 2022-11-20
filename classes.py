from tkinter import Entry, END, Button

class Joueur:
    def __init__(self, nom, description, resultats, points, etat, penalite):
        self.nom = nom
        self.description = description
        self.resultats = resultats
        self.points = points
        self.penalite = penalite
        self.etat = etat

    def __str__(self):
        return f"Nom : {self.nom}\nDescription : {self.description}\nResultats : {self.resultats}\nPoints : {self.points}\nEtat : {self.etat}"

    def resultJ(self):
        return f"Résultats : {self.resultats}"

    def diplome(self):
        pass


class Equipe:
    def __init__(self, nom):
        self.joueurs = []
        self.nom = nom

    def __str__(self):
        liste = []
        for i in self.joueurs:
            i.append(liste)
        return liste

    def listeJoueurs(self):
        for joueur in self.joueurs:
            print(joueur.nom)

    def ajouterJoueur(self, Joueur):
        self.joueurs.append(Joueur)


class Concours:
    def __init__(self):
        self.classement = []
        self.disqualifie = []
        self.joueurs = []
        self.equipes = []
        self.rules = None

    def __classement__(self):
        self.classement.sort(key=lambda a: a[3]+a[4])
        for i in range(len(self.classement)):
            self.classement[i].resultats = i+1

    def __affiche__(self):
        listQualified = []
        listDisqualified = []
        for i in self.classement:
            if i.etat == True:
                listQualified.append(i)
            else:
                listDisqualified.append(i)
        return listQualified, listDisqualified

    def modif(self, playerPoints, playerPenality):
        self.rules = playerPoints * 2 + playerPenality
        return

    def recl(self, Joueur):
        p = Joueur
        if p.status == False:
            p.status = True
        else:
            p.status = False
        
    def chercherJoueur(self, nom):
        for i in self.classement:
            if i.nom == nom:
                return i
        return None

    def saisieJ(self, Joueur):
        if self.etat == True:
            self.classement.append(Joueur)
        else:
            self.disqualifie.append(Joueur)


concours = Concours()
