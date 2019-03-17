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