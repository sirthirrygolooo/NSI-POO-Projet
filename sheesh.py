# Fichier regroupant toutes les classes

class Concours:
    """Classe principale du concours permettant de créer le tableau de base"""
    
    def __init__(self):
        tab = []

    def __classement__(self):
        pass

    def __affiche__(self):
        pass

    def listeJoueurs(self):
        pass

    def modif(self):
        pass

    def recl(self):
        pass

    def saisieJ(self):
        pass

    def demarre(self):
        pass


class Ekip:
    """Permet de créer les éléments de l’attribut listeJoueurs"""

    def __init__(self,nom,marque,ecurie,etat) -> None:
        self.nom = nom
        self.marque = marque
        self.ecurie = ecurie
        self.resultats = ''
        self.points = ''
        self.etat = etat

    def __str__(self) -> str:
        return(f'Nom : {self.nom} Marque : {self.marque} Ecurie : {self.ecurie} Statut : {self.etat} Points : {self.points}')

    def resultJ(self):
        pass
