import operator

def func_repart(intitules_proba):
    intitules_proba.sort(key = operator.itemgetter(1))
    print(intitules_proba)
    # repartition=[]
    # for i in range(0, len(intitules_proba)):
    #     repartition.append(get_coef_cumul(intitules_proba,i)/get_coef_cumul(intitules_proba,len(intitules_proba)))
    # return repartition

def get_coef_cumul(intitules_proba, index):
    coef_cumul = 0
    for i in range(0, index):
        coef_cumul += intitules_proba[i][1]
    return coef_cumul
