#!/usr/bin/python
import random
import math
random.randint.__doc__

# Générer un Polynôme aléatoire ax²+bx+c
# ATTENTION Renvoi 3 valeurs a, b, c


def randomPolynomial():
    # Nombre alétaoire pour ax²+bx+c compris entre [-10:10]
    a = random.uniform(-10, 10.5)
    b = random.uniform(-10, 10.5)
    c = random.uniform(-10, 10.5)
    # Conversion du nombre aléatoire par pas de 0.5
    a = round(a * 2) / 2
    b = round(b * 2) / 2
    c = round(c * 2) / 2
    return (a, b, c)


# sauvegarde du polynome
polynome = randomPolynomial()


def discriminant(randomPolynomial):
        delta = randomPolynomial[1] * randomPolynomial[1] - 4 * randomPolynomial[0] * randomPolynomial[2]
        return delta

    # Calcul racine pour Delta>0

def positive_root(polynom, delta):
    x1 = (-polynom[1] + math.sqrt(delta)) / 2 * polynom[0]
    x2 = (-polynom[1] - math.sqrt(delta)) / 2 * polynom[0]
    return x1, x2

    # Calcul racine pour Delta=0
def null_root(polynom):
    x = -polynom[1] / 2 * polynom[0]
    return x,None

    # Calcul racine pour Delta<0

def negative_root():
    return None,None


# Traitement compare réponse user 

def polynomSolution(polynome, answer):
    # FONCTION Calculer du discriminant b²-4ac
    # sauvegarde de delta
    delta = discriminant(polynome)
    # Calcul des racines selon la valeur de delta
    root = 0
    if delta < 0:
        root = negative_root()
    elif delta == 0:
        root = null_root(polynome)
    else:
        root = positive_root(polynome, delta)

    solu = 0

    # Comparaison solution selon nombre de racine
    if len(root) == 2:
        if root[0]+root[1] == answer[0]+answer[1]:
            solu = True
        else:
            solu = False
    elif len(root) <= 1:
        if root == answer:
            solu = True
        else:
            solu = False
    
    return solu
