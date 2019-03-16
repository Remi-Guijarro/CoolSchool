import interface
from  utils import *

def run():
	mode = interface.chooseMode()

	intitules=("Second degré","Intégrales","Fonctions puissance","Fonctions trigonométriques","Fonctions logarithmiques")
	probabilites = interface.chooseProbabilities(intitules)
	intitule_proba_mat=[]
	intitules_proba_chapters=[]
	for i in range(0, 2):
		intitule_proba_mat.append((intitules[i],probabilites[i]))
	for i in range(2, 5):
		intitules_proba_chapters.append((intitules[i],probabilites[i]))
		
	print(func_repart(intitule_proba_mat))	
	print(func_repart(intitules_proba_chapters))	

run()