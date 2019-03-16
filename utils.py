import operator
import random

def func_repart(intitules_proba):
    intitules_proba.sort(key = operator.itemgetter(1))
    repartition=[]
    for i in range(0, len(intitules_proba)):
        repartition.append(get_coef_cumul(intitules_proba,i))
    return repartition

def get_coef_cumul(intitules_proba, index):
    coef_cumul = 0
    for i in range(0, index+1):
        coef_cumul = coef_cumul + float(intitules_proba[i][1])
    return coef_cumul


def get_rand():
    return random.uniform(0, 1)