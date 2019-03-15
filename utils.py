import operator

def func_repart(intitules_proba):
    intitules_proba.sort(key = operator.itemgetter(1))
    repartition=[]
    for i in range(0, intitules_proba.size())
        repartition.append(coef_cumul(intitules_proba,i)/coef_cumul(intitules_proba,intitules_proba.size()))
    return repartition

def get_coef_cumul(intitules_proba, index):
    coef_cumul = 0
    for i in range(0, index):
        coef_cumul += intitules_proba[i][1]
    return coef_cumul
