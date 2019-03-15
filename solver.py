#!/usr/bin/python
import random
import math
random.randint.__doc__

#Générer un Polynôme aléatoire ax²+bx+c 
#ATTENTION Renvoi 3 valeurs a, b, c
def randomPolynomial():
    #Nombre alétaoire pour ax²+bx+c compris entre [-10:10]
    a = random.uniform(-10,10.5)
    b = random.uniform(-10,10.5)
    c = random.uniform(-10,10.5)
    #Conversion du nombre aléatoire par pas de 0.5
    a = round(a * 2) / 2
    b = round(b * 2) / 2
    c = round(c * 2) / 2
    return a, b, c

#FONCTION Calculer du discriminant
def discriminant(param):
    delta = param[1] * param[1] - 4 * param[0] * param[2] 
    return delta

#print(randomPolynomial())
(a, b, c) = randomPolynomial()
print( a, b, c)
print(discriminant(randomPolynomial()))  

#Récupérer du résultat du user
def compareSolution(param1, param2):
    solu = 0
    if param1 != param2:
        solu = False
    else:
        solu = True
    return solu

#Calcul racine pour Delta>0
def positive_root(para1, para2, para3, delta):
    x1 = (-para2 + math.sqrt(delta)) / 2 * para1
    x2 = (-para2 - math.sqrt(delta)) / 2 * para1
    return x1, x2

#Calcul racine pour Delta=0
def null_root(par1, par2):
    x = -par2 / 2 * par1
    return x

#Calcul racine pour Delta<0
def negative_root():
    x = "pas de solution"
    return x

