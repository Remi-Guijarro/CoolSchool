#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import math
random.randint.__doc__
from random import choice
from random import randint
from interface import printError


# Générer un Polynôme aléatoire ax²+bx+c
# ATTENTION Renvoi 3 valeurs a, b, c
def randomPolynomial():
    # Nombre alétaoire pour ax²+bx+c compris entre [-10:10]
    # a != 0 car sinon, on a un polynome de degré 1
    # Conversion du nombre aléatoire par pas de 0.5
    a = 0
    while(a == 0):
        a = random.uniform(-10, 10.5)
        a = round(a * 2) / 2
    b = random.uniform(-10, 10.5)
    b = round(b * 2) / 2
    c = random.uniform(-10, 10.5)
    c = round(c * 2) / 2
    return (a, b, c)

def discriminant(randomPolynomial):
        delta = (randomPolynomial[1] * randomPolynomial[1]) - 4 * (randomPolynomial[0] * randomPolynomial[2])
        print(delta)
        return delta

# Calcul racine pour Delta>0
def positive_root(polynom, delta):
    x1 = ((-polynom[1]) + math.sqrt(delta)) / (2 * polynom[0])
    x2 = (-polynom[1] - math.sqrt(delta)) / (2 * polynom[0])
    return float("{0:.2f}".format(round(float(x1),2))),float("{0:.2f}".format(round(float(x2),2)))

# Calcul racine pour Delta=0
def null_root(polynom):
    x = -polynom[1] / 2 * polynom[0]
    return float("{0:.2f}".format(round(float(x),2))),None

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
    print(len(root))
    if str(root[0]).upper() == "NONE"  and str(root[1]).upper() == "NONE":
        if (str(root[0]).upper() == str(answer[0]).upper() ) and (str(root[1]).upper() == str(answer[1]).upper() ) or (str(root[0]).upper() == str(answer[1]).upper() ) and ( str(root[1]).upper() == str(answer[0]).upper() ):
            solu = True
        else:
            printError("The solution was :> "+ str(root[0]) + "  " +str(root[1])) 
            solu = False
    else:     
        if (str("{0:.2f}".format(round(float(root[0]),2))) == str(answer[0])) and ( str("{0:.2f}".format(round(float(root[1]),2))) == str(answer[1])) or  (str("{0:.2f}".format(round(float(root[0]),2))) == str(answer[1])) and ( str("{0:.2f}".format(round(float(root[1]),2))) == str(answer[0])):
            solu = True
        else:
            printError(str("{0:.2f}".format(round(float(root[0]),2))) + "  " +str("{0:.2f}".format(round(float(root[1]),2)))) 
            solu = False
    return solu


#Integral a & b random values in range[-10,10] = A
def randomIntegralBounds():
    a = 0
    b = 0
    while a == b:    
        a = randint(-10,10)
        b = randint(-10,10)

    t = 0
    if a > b:
        t = a
        a = b
        b = t
    return a, b

#Integral Puissance question 2.1.a -> c, d, alpha random value in A (with exceptions)
def randomPowValues_a():
    c = choice([i for i in range(-10,10) if i not in [0]])
    d = randint(-10,10)
    alpha = choice([i for i in range(-10,10) if i not in [-1]])
    return c, d, alpha

def powResolve_a(bounds,c_d_alpha):
    I = ( 1 / c_d_alpha[0] * (c_d_alpha[2] + 1)) * ((bounds[1]*c_d_alpha[0] - c_d_alpha[1])**(c_d_alpha[2]+1) - (bounds[0]*c_d_alpha[0]-c_d_alpha[1])**(c_d_alpha[2]+1))
    return I

#Integral Puissance question 2.1.b -> c, d, alpha random value in A (with exceptions)
def randomPowValues_b(bounds):
    c = choice([i for i in range(-10,10) if i not in [bounds[0], bounds[1]]])
    return c

def powResolve_b(bounds,c):
    I = math.log(abs(bounds[1]-c)) - math.log(abs(bounds[0]-c))
    return I