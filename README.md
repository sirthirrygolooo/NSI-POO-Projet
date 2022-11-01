# NSI-POO-Projet 👨‍💻
 NSI projet POO octobre/novembre 2022

## **Calcul des Points**

- 30 points par minute (0.5 par sec.)
 - Pénalités à +2,5/+5/+10 pts ? (équivalent 5/10/20sec pénalité) --> à définir
- moins de points --> victoire 

- Pour le calcul des points juste prise en compte des fautes et après (temps en sec /2 + temps pénalités) donc un truc du genre 
```python
score  = int(time)/2 + nombre_penalite * 10    # temps de pénalité à définir donc 10 pas sur
```

