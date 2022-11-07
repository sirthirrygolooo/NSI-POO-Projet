class Joueur:
    def __init__(self, nom, description, resultats, points, etat):
        self.nom = nom
        self.description = description
        self.resultats = resultats
        self.points = points
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
    def __init__(self, Equipe):
        self.classement = []

    def __classement__(self):
        self.classement.sort(key=lambda a: a[3])

    def __affiche__(self):
        return f"Classement : {self.classement}"

    def modif(self):
        pass

    def recl(self, Joueur):
        pass

    def saisieE(self, Equipe):
        self.classement.append(Equipe)


