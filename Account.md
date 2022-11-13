# Projet POO NSI 2022

Par Cunin Alan, Brouillet Arthur et Froehly Jean-Baptiste

***

## Le projet 

Nous avons choisi de faire un tableau d'affichage pour course automobile. Or, il se trouve que en automobile, tout est déterminé par le temps effectué mais le cahier des charges exige l'utilisation d'un calcul à un moment. C'est pourquoi nous avons choisi d'attrbiuer un nombre de points en fonction du temps effectué à hateur de ... par ... auquel nous ajouterons un nombre de points donné selon les pénalités qui peuvent être également appliquées (collision, mauvaise trajectoire, etc...) ainsi, moins le concurrent à de points, mieux il est classé. 

## Notre code en quelques lignes 

Pour ce qui est des classe, on retrouve donc une classe `Joueur` qui a pour attributs les différentes infos relatives au pilote telles que son nom, sa description, ses résultats, ses points et son état (attente ou course effectuée). On trouve également des méthodes pour retourner ces-dites infos ainsi que ses résultats et finalement une dernière pour afficher le "diplôme" mais qui reste facultative. 

Nous avons ensuite la classe `Equipe` qui permet de gérer ces différents joueurs, d'en ajouter, de les lister et d'instancier avec la classe `Joueur`. Elle prend pour attributs les joueurs sous forme de liste et le nom du joueur à ajouter. Les différentes méthodes permettent ensuite respectivement d'afficher, de lister ou d'ajouter les diférents concurrents. 

Puis vient la classe `Concours` qui prend pour attribut le classement sous forme de liste et à pour méthodes classement, qui permet de trier les différents présents dans `classement`, mais aussi une méthode affiche pour afficher ce classement ; on retrouve aussi modif pour modifier un élement recl pour reclasser un participant et saisieE pour ajouter une équipe au classement. 

## Notre méthode de calcul de points

Comme dit précédemment, la problématique pour déterminer le classement en allant plus loin qu'un simple tri en fonction du temps effectué à l'arrivée est de déterminer un nombre de points en fonction du temps effectué. Nous sommes donc parti du principe que 1min vaut 120 points nets soit 2 points par seconde. On se retrouve donc avec un équivalent points/temps qui nous permets de déterminer aisément le classement selon le temps net effectué. Cependant, nous avons décidé d'élaborer un peu plus en rajoutant un système de pénalités prenant en compte les collisions, les mauvaises trajectoires, les dépassements non autorisés, etc... qui vont valoir plus ou moins de points en fonction de la gravité de l'infraction. Bien évidemment, plus une infraction vaut de points, plus elle vous fera baisser dans le classement et inversement car pour mieux visualiser ce système, une pénalité de l'ordre de 10 points serait donc comme rajouter 5 secondes à votre temps et une autre de 100 points comme rajouter 50 secondes ce qui est peu négligeable.  
Pour ce qui est de la formule pour calculer ces points, elle ressemble donc à :
```python
nombre_points = temps_en_secondes * 2 + pénalites
```

sachant que pénalité est une variable qui prendra en compte les différentes pénalités appliquées au joueur :

```python
pénalité = type_penalite1 + type_penalite2 + type_penalite3 + ...
```

## 