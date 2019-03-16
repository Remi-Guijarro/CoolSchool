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

def constructIntituleMa(array):
	matArray=[]
	matMap={}
	for intitule in array:
		if("M_" in intitule):
			matArray.append(intitule[2:])
			matMap[intitule[2:]] = 0
			array.remove(intitule)
	return (matArray,matMap)

def constructIntituleChapters(array,matarray):
	chaptersMap={}
	for intitule in array:
		for mat  in matarray:
			if(mat in intitule):
				if(mat in chaptersMap):
					chaptersMap[mat][intitule] = 0
				else:
					chaptersMap[mat] = {}
					chaptersMap[mat][intitule] = 0
	return chaptersMap

def randSubject(fonction_repart_mat):
	print(fonction_repart_mat)
	

def randchapters(fonction_repart_chapters):
	return "choosen chapters"

def randQuestion(theme):
	if(theme.strip().upper() == "SECONDDEGRE"):
		return "ax^2+bx+c"
	elif(theme.strip().upper() == "FONCTIONSPUISSANCE"):
		return "ax^2+bx+c"

def exam_session(subjectsMap,chaptersMap):
	printInformation("Running in exam mode")
	# randSubject(subjectsMap)
	# print(chaptersMap)

def trainning_session(subjectsMap,chaptersMap):
	printInformation("Running in trainning mode")

def run():
	mode = chooseMode()
	intitules=["M_Polynome","\t Polynome_Second degre","M_Integrales","\t Integrales_Fonctions puissance","\t Integrales_Fonctions trigonometriques","\t Integrales_Fonctions logarithmiques"]
	subjectsArray,subjectsMap=constructIntituleMa(intitules)
	chaptersMap= constructIntituleChapters(intitules,subjectsArray)
	subjectsMap = chooseSubjectProbabilities(subjectsMap)
	chaptersMap = chooseChapterProbabilities(chaptersMap,subjectsMap)
	print(chaptersMap)
	# intitule_proba_mat,	intitules_proba_chapters=constructIntitileProbaArrays(intitules,probabilites)	
	# fonction_repatition_mat=func_repart(intitule_proba_mat)
	# fonction_repatition_sousChap=func_repart(intitules_proba_chapters)

	if(mode):
		exam_session(subjectsMap,chaptersMap)
	else:
		trainning_session(subjectsMap,chaptersMap)

run()