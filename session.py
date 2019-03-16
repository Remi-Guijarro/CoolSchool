from interface import *
from  utils import *


def exam_session(fonction_repart_mat,fonction_repart_chapters):
	printInformation("Running in exam mode")
def trainning_session(fonction_repart_mat,fonction_repart_chapters):
	printInformation("Running in trainning mode")

def run():
	mode = chooseMode()

	intitules=("Second degré","Intégrales","Fonctions puissance","Fonctions trigonométriques","Fonctions logarithmiques")
	probabilites = chooseProbabilities(intitules)
	intitule_proba_mat=[]
	intitules_proba_chapters=[]
	for i in range(0, 2):
		intitule_proba_mat.append((intitules[i],probabilites[i]))
	for i in range(2, 5):
		intitules_proba_chapters.append((intitules[i],probabilites[i]))

	fonction_repatition_mat=func_repart(intitule_proba_mat)
	fonction_repatition_sousChap=func_repart(intitules_proba_chapters)


	if(mode):
		exam_session(fonction_repatition_mat,fonction_repatition_sousChap)
	else:
		trainning_session(fonction_repatition_mat,fonction_repatition_sousChap)

run()