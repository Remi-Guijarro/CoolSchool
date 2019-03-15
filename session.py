import interface
import utils

def run():
	mode = interface.chooseMode()

	intitules=("Second degré","Intégrales","Fonctions puissance","Fonctions trigonométriques","Fonctions logarithmiques")
	probabilites = interface.chooseProbabilities(intitules)

	intitules_proba=[]
	for i in range(0, 5):
		intitules_proba.append((intitules[i],probabilites[i])

	# Main loop
	
