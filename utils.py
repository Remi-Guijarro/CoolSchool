import operator
import random
import collections

def func_repart(orederedCollec):
    repartition=[]
    for key,value in orederedCollec.items():        
        repartition.append(get_coef_cumul(orederedCollec,key))
    return repartition

def get_coef_cumul(orederedCollec, key):
    coef_cumul = 0
    for keyy, value in orederedCollec.items():
        if(keyy == key):
            coef_cumul = coef_cumul + float(orederedCollec[keyy])
            return coef_cumul
        else:
            coef_cumul = coef_cumul + float(orederedCollec[keyy])


def get_rand():
    return random.uniform(0, 1)