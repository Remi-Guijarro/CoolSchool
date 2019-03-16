from interface import *
from  utils import *


def constructIntitileProbaArrays(intitules,probas):
	intitule_proba_mat=[]
	intitules_proba_chapters=[]
	for i in range(0, len(intitules)):
		if("M_" in intitules[i]):
			intitule_proba_mat.append((intitules[i],probas[i]))
		else:
			intitules_proba_chapters.append((intitules[i],probas[i]))
	return (intitule_proba_mat,intitules_proba_chapters)

def randSubject(fonction_repart_mat):
	return "choosen subject"

def randchapters(fonction_repart_chapters):
	return "choosen chapters"

def randQuestion(theme):
	if(theme.strip().upper() == "SECONDDEGRE"):
		return "ax^2+bx+c"
	elif(theme.strip().upper() == "FONCTIONSPUISSANCE"):
		return "ax^2+bx+c"

def exam_session(fonction_repart_mat,fonction_repart_chapters):
	printInformation("Running in exam mode")

def trainning_session(fonction_repart_mat,fonction_repart_chapters):
	printInformation("Running in trainning mode")

def run():
	mode = chooseMode()
	intitules=("M_Polynome","\tSecond degre","M_Integrales","\tFonctions puissance","\tFonctions trigonometriques","\tFonctions logarithmiques")
	probabilites = chooseProbabilities(intitules)
	intitule_proba_mat,	intitules_proba_chapters=constructIntitileProbaArrays(intitules,probabilites)	
	fonction_repatition_mat=func_repart(intitule_proba_mat)
	fonction_repatition_sousChap=func_repart(intitules_proba_chapters)

	if(mode):
		exam_session(fonction_repatition_mat,fonction_repatition_sousChap)
	else:
		trainning_session(fonction_repatition_mat,fonction_repatition_sousChap)

run()