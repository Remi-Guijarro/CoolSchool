MODE1="EXAM"
MODE2="TRAINING"

def chooseMode():
    mode = input("Which mode do you want to run ? ("+ MODE1 + "|" + MODE2 + ")")
    return mode


def chooseProbabilities(n_uplet):
    lp=[]
    for intitule in n_uplet:
        proba = input("Choose the propabilities for : " + intitule)
        lp.append(proba)
    return lp