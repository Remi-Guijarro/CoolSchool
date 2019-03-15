import csv


def compute_stat(user_name):
    print("getting stat")

#save the score of the current 'player' in the current mode
def save():
    print("writing file")

def init():
    chapitre=[]
    chapitre.append(("Second degrés",0))
    chapitre.append(("intégrale",0))
    souschapitre_integrale=[]
    souschapitre_integrale.append(("puissance",0))
    souschapitre_integrale.append(("trigonométrique",0))
    souschapitre_integrale.append(("logarithmique",0))
    return (chapitre,souschapitre_integrale)