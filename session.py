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

def randSubject(subjectsMap):
	orderedCollec = collections.OrderedDict(sorted(subjectsMap.items(), key=lambda kv: kv[1]))
	randnb = get_rand()
	cpt=0
	func_repart_sub=func_repart(orderedCollec)
	for key,value in orderedCollec.items():
		if(func_repart_sub[cpt] >= randnb):
			return key 
		else:
			cpt+=1
	

def randchapters(fonction_repart_chapters):
	return "choosen chapters"

def randQuestion(theme):
	if(theme.strip().upper() == "SECONDDEGRE"):
		return "ax^2+bx+c"
	elif(theme.strip().upper() == "FONCTIONSPUISSANCE"):
		return "ax^2+bx+c"

def exam_session(subjectsMap,chaptersMap):
	printInformation("Running in exam mode")
	#cpt_i=0.0
	#cpt_p=0.0
	for i in range(0,20):
		print(randSubject(subjectsMap))
		# TO DO : Implement the choose of the chapters acccording to the subject		
		# ======= This was on a test purpose ========	
		# if(m == "Integrales"):
		# 	cpt_i+=1
		# else:
		# 	cpt_p+=1
	# print("proba Integral = ",cpt_i/5000)
	# print("proba Integral = ",cpt_p/5000)

def trainning_session(subjectsMap,chaptersMap):
	printInformation("Running in trainning mode")
	userInput=""
	while(True):
		if(userInput == "QUIT"):
			break		
		print(randSubject(subjectsMap))
		userInput = input("your Anwer :> ")
		# TO DO : Implement the choose of the chapters acccording to the subject		

def run():
	mode = chooseMode()
	intitules=["M_Polynome","\t Polynome_Second degre","M_Integrales","\t Integrales_Fonctions puissance","\t Integrales_Fonctions trigonometriques","\t Integrales_Fonctions logarithmiques"]
	subjectsArray,subjectsMap=constructIntituleMa(intitules)
	chaptersMap= constructIntituleChapters(intitules,subjectsArray)
	subjectsMap = chooseSubjectProbabilities(subjectsMap)
	chaptersMap = chooseChapterProbabilities(chaptersMap,subjectsMap)
	if(mode):
		exam_session(subjectsMap,chaptersMap)
	else:
		trainning_session(subjectsMap,chaptersMap)

run()