# Projet POO NSI 2022

Par Cunin Alan, Brouillet Arthur et Froehly Jean-Baptiste

***

## Le projet 

Nous avons choisi de faire un tableau d'affichage pour course automobile. Or, il se trouve que en automobile, tout est déterminé par le temps effectué mais le cahier des charges exige l'utilisation d'un calcul à un moment. C'est pourquoi nous avons choisi d'attrbiuer un nombre de points en fonction du temps effectué à hateur de ... par ... auquel nous ajouterons un nombre de points donné selon les pénalités qui peuvent être également appliquées (collision, mauvaise trajectoire, etc...) ainsi, moins le concurrent à de points, mieux il est classé. 

## Notre code en quelques lignes 

Pour ce qui est des classe, on retrouve donc une classe `Joueur` qui a pour attributs les différentes infos relatives au pilote telles que son nom, sa description, ses résultats, ses points et son état (attente ou course effectuée). On trouve également des méthodes pour retourner ces-dites infos ainsi que ses résultats et finalement une dernière pour afficher le "diplôme" mais qui reste facultative. 

Nous avons ensuite la classe `Equipe` qui permet de gérer ces différents joueurs, d'en ajouter, de les lister et d'instancier avec la classe `Joueur`.

Puis vient la classe `Concours` qui prend pour attribut le classement sous forme de liste et à pour méthodes 
