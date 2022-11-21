class Joueur:
    def __init__(self, nom, points, penalite, etat):
        self.nom = nom
        self.points = points
        self.penalite = penalite
        self.etat = etat
        self.total = int(self.points) + int(self.penalite)
    
    def __str__(self):
        return self.nom + " Points : " + str(self.points) + "    Points de pénalités : " + str(self.penalite) +"    SCORE total : " + str(self.total)


    def getName(self):
        nom = self.nom
        return nom
    
    def getPoints(self):
        points = self.points
        return int(points)
    
    def getPenalite(self):
        penalite = self.penalite
        return int(penalite)
    
    def getTotal(self):
        total = self.total
        return total

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
        self.joueurs = []
        self.equipes = []
        self.rules = None

    def trierclassement(self):
        self.classement.sort(key=lambda a: a[3])
        print(self.classement)
        for i in range(len(self.classement)):
            self.classement[i][1] = i+1

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
        self.classement.append([Joueur.getName(), Joueur.getPoints() * int(self.rules), Joueur.getPenalite(), (Joueur.getPoints() * int(self.rules)) + Joueur.getPenalite(), Joueur.getEtat()])

    def saisieE(self, Equipe):
        self.equipes.append(Equipe)

    def afficherE(self):
        for i in self.equipes:
            print(i.nom, i.listeJoueurs())


concours = Concours()
equipe = Equipe('Equipe 1')