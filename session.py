from interface import *
from  utils import *
from solver import *


# initialize a dictionnary <String, Int>  <==>  <Subject, probability>  with the probabilities at 0
def constructIntituleMa(array):
	matArray=[]
	matMap={}
	for intitule in array:
		if("M_" in intitule):
			matArray.append(intitule[2:])
			matMap[intitule[2:]] = 0
			array.remove(intitule)
	return (matArray,matMap)

# initialize a dictionnary <String,<String, Int>>  <==>  <Subject,<chapter, probability>>  with the probabilities at 0
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

# Return a random subject according to their probabilities
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
	
# Should return a random chapter according subject given and their probabilities
# To do 
def randchapters(subject_name,chaptersMap):
	possibleChapters=chaptersMap[subject_name]
	orderedPossibleChapters=collections.OrderedDict(sorted(possibleChapters.items(), key=lambda kv: kv[1]))
	randnb = get_rand()
	cpt=0
	func_repart_chap=func_repart(orderedPossibleChapters)
	for key,value in orderedPossibleChapters.items():
		if(func_repart_chap[cpt] >= randnb):
			substr=int(2+len(subject_name))
			return key[substr:]
		else:
			cpt+=1



# Should return a random question according to the chapters given and their probabilities
#To do
def randQuestion(theme):
	print(theme)
	if(theme.strip().upper() == "SECONDDEGRE"):
		return format_polynome(randomPolynomial())
		

# run the game in exam session
def exam_session(subjectsMap,chaptersMap):
	printInformation("Running in exam mode")
	for i in range(0,20):
		printInformation("QUESTION "+ str(i))
		subject=randSubject(subjectsMap)
		printInformation(subject)
		chapter=randchapters(subject,chaptersMap)
		printInformation(chapter)
		print(randQuestion(str(chapter).replace(" ","",1).upper()))
		userInput = input("your Anwer :> ")
		clear()


# Run the game in trainning session
def trainning_session(subjectsMap,chaptersMap):
	printInformation("Running in trainning mode")
	userInput=""
	while(True):
		if(userInput == "QUIT"):
			break		
		print(randSubject(subjectsMap))
		userInput = input("your Anwer :> ")
		# TO DO : Implement the choose of the chapters acccording to the subject		

# The main function of the game
def run():
	mode = chooseMode()
	intitules=["M_Polynome","\tPolynome_Second degre","M_Integrales","\tIntegrales_Fonctions puissance","\tIntegrales_Fonctions trigonometriques","\tIntegrales_Fonctions logarithmiques"]
	subjectsArray,subjectsMap=constructIntituleMa(intitules)
	chaptersMap= constructIntituleChapters(intitules,subjectsArray)
	subjectsMap = chooseSubjectProbabilities(subjectsMap)
	chaptersMap = chooseChapterProbabilities(chaptersMap,subjectsMap)
	if(mode):
		exam_session(subjectsMap,chaptersMap)
	else:
		trainning_session(subjectsMap,chaptersMap)
