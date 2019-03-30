import operator
import random
import collections

# Return the repartition function for Subjects
def func_repart(orederedCollec):
    repartition=[]
    for key,value in orederedCollec.items():        
        repartition.append(get_coef_cumul(orederedCollec,key))
    return repartition

# Return the addiction of the probabilities for 0 to the given key
def get_coef_cumul(orederedCollec, key):
    coef_cumul = 0
    for keyy, value in orederedCollec.items():
        if(keyy == key):
            coef_cumul = coef_cumul + float(orederedCollec[keyy])
            return coef_cumul
        else:
            coef_cumul = coef_cumul + float(orederedCollec[keyy])

# Return a random number Between 0 and 1
def get_rand():
    return random.uniform(0, 1)

def format_polynome(n_uplet):
    polynome=""
    for i in range(0,3):        
        if(n_uplet[i] > 0 and i != 0):
            polynome += "+"
        if(n_uplet[i] > 0):
            polynome+=str(n_uplet[i])+str(get_format_at(i))+" "
        elif(n_uplet[i] < 0):
            polynome+=str(n_uplet[i])+str(get_format_at(i))+" "
        elif (n_uplet[i] == 0):
            continue
    return polynome

def get_format_at(index):
    if(index == 0):
        return "x^2"
    elif(index == 1):
        return "x"
    elif(index == 2):
        return ""
    
def distribute_in_probabilties(values):
    probabilities = []
    total = sum(values)
    for i in range(0, len(values)):
        probabilities.append(values[i]/total)
    return probabilities
