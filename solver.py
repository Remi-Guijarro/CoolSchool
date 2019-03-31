#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from  math import * 
random.randint.__doc__
from random import choice
from random import randint
from sys import exit
from utils import *
from interface import *
from scipy.integrate import quad
from sympy import *
from numpy import arange

LIMIT_MAX = 3000000000000
LIMIT_MIN = -3000000000000
TAN_MAXIMUM_GAP_BOUNDS=2

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
        # print(delta)
        return delta

# Calcul racine pour Delta>0
def positive_root(polynom, delta):
    x1 = ((-polynom[1]) + sqrt(delta)) / (2 * polynom[0])
    x2 = (-polynom[1] - sqrt(delta)) / (2 * polynom[0])
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
    # print(len(root))
    if str(root[0]).upper() == "NONE"  and str(root[1]).upper() == "NONE":
        if (str(root[0]).upper() == str(answer[0]).upper() ) and (str(root[1]).upper() == str(answer[1]).upper() ) or (str(root[0]).upper() == str(answer[1]).upper() ) and ( str(root[1]).upper() == str(answer[0]).upper() ):
            solu = True
        else:
            printError("La solution etait :> "+ str(root[0]) + "  " +str(root[1])) 
            solu = False
    else:     
        if (str("{0:.2f}".format(round(float(root[0]),2))) == str(answer[0])) and ( str("{0:.2f}".format(round(float(root[1]),2))) == str(answer[1])) or  (str("{0:.2f}".format(round(float(root[0]),2))) == str(answer[1])) and ( str("{0:.2f}".format(round(float(root[1]),2))) == str(answer[0])):
            solu = True
        else:
            printError(str("{0:.2f}".format(round(float(root[0]),2))) + "  " +str("{0:.2f}".format(round(float(root[1]),2)))) 
            solu = False
    return solu


#Integral a & b random values in range[-10,10] = A
def randomIntegralBounds(min=-10,max=10):
    a = 0
    b = 0
    while a == b:    
        a = randint(min,max)
        b = randint(min,max)
    t = 0
    if a > b:
        t = a
        a = b
        b = t
    return a, b

def randomFloatIntegralBounds(min=-10,max=10):
    a = 0
    b = 0
    while a == b:    
        a = round(random.uniform(min,max),2)
        b = round(random.uniform(min,max),2)
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


def get_tanIntegralVariables():
    while(True):        
        min_=get_rand();
        c=randomTrigo() 
        (a,b)=randomFloatIntegralBounds(min_,min_+(TAN_MAXIMUM_GAP_BOUNDS/(c/2)))
        if(not isHomoGraphicalF_NotContinuous("cos("+str(c)+"*x)",(a,b))):
            return a,b,c


def powResolve_a(bounds,c_d_alpha):
    a,b=bounds
    c,d,al=c_d_alpha
    if(computeLimitFunction(bounds,str("("+str(c)+"*x"+ "-"+str(d)+")"+"**"+str(al)))):
        return "none"
    I = (1/(c*(al+1))*( pow((b*c-d), al+1) - pow((a*c-d), al+1)))
    return "{0:.2f}".format(float(I),2)

#Integral Puissance question 2.1.b -> c, d, alpha random value in A (with exceptions)
def randomPowValues_b(bounds):
    c = choice([i for i in range(-10,10) if i not in [bounds[0], bounds[1]]])
    return c

def powResolve_b(bounds,c):
    if(computeLimitFunction(bounds,str("1/(x"+" -"+str(c)+")"))):
        return "none"
    I = log(abs(bounds[1]-c)) - log(abs(bounds[0]-c))
    return "{0:.2f}".format(float(I),2)

def randomTrigo():
    c = choice([i for i in range(-10,10) if i not in [0]])
    return c

def trigoCosResolve(bounds,c):
    I = 0
    if(computeLimitFunction(bounds,str("cos("+str(c)+"*x)"))):
        return "none"
    I = (sin(bounds[1]*c) - sin(bounds[0]*c)) / c
    return "{0:.2f}".format(float(I),2)

def trigoSinResolve(bounds,c):
    I = 0
    if(computeLimitFunction(bounds,str("sin("+str(c)+"*x)"))):
        return "none"
    I = - (cos(bounds[1]*c) - cos(bounds[0]*c)) / c
    return "{0:.2f}".format(float(I),2)

def trigoTanResolve(bounds,c):
    I = 0
    A = bounds[0]*c
    B = bounds[1]*c
    if(isHomoGraphicalF_NotContinuous("tan("+str(c)+"*x)",bounds)):
        return "none"
    I = -(log(abs(cos(B))) - (log(abs(cos(A))))) / c 
    return "{0:.2f}".format(float(I),2)
#TEST
# gg = log(abs(cos(-2)))
# ggg = cos(2)

# print(gg)
# print(ggg)

# (billout)=randomIntegralBounds()
# print(billout)
# t = randomTrigo()
# print(t)
# f = trigoSinResolve(billout,t)
# print("sinus =", round(f,2))
# g = trigoCosResolve(billout,t)
# print("Cosinus = ",round(g,2))
# h = trigoTanResolve(billout,t)
# print("Tangente = ", round(h,2))
# print(tan(t))

def computeLimitFunction(bounds,function):
    print('Chargement', end='\n\r')
    idx = 0
    for i in arange(int(bounds[0]),int(bounds[1]),0.3):
        animation = "|/-\\"
        print(animation[idx % len(animation)], end="\r")
        idx += 1        
        lim=str(limit(function,Symbol("x"),i))
        if (lim == "oo" or float(lim) > LIMIT_MAX or float(lim) < LIMIT_MIN ):
            return True
            
# Log function | random value for c (contraintes spéciale)
def randomLog():
    c = random.uniform(0.5, 10.5)
    c = round(c * 2) / 2
    return c

# def logResolve(bounds,c):
#     I = (bounds[1]*(log1p(bounds[1]*c))) - (bounds[0]*(log1p(bounds[0]*c))) - (c*(bounds[1]-bounds[0]))
#     return I


def logResolve(bounds,c):
    def logReturnFunction(x):
        return log(c*x)
    I,J = quad(logReturnFunction,bounds[0],bounds[1])
    return "{0:.2f}".format(float(I-J),2)  


def isHomoGraphicalF_NotContinuous(denominator,bounds):
    x=evalFunctionStatusAt(str(denominator).replace('x',str(bounds[0])))    
    for i in arange(int(bounds[0]),int(bounds[1]),0.0001):        
        y = evalFunctionStatusAt(str(denominator).replace('x',str(i)))
        if(y != x):
            return True
        x = y
    return False

def evalFunctionStatusAt(function):
    if(eval(function) >= 0):
        return True
    else:
        return False

