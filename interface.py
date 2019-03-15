MODE1="EXAM"
MODE2="TRAINING"

def chooseMode():
    mode = raw_input("Which mode do you want to run ? ("+ MODE1 + "|" + MODE2 + ")")
    return mode


def chooseProbabilities(n_uplet):
    lp=[]
    for intitule in n_uplet:
        proba = raw_input("Choose the propabilities for : " + intitule)
        lp.append(proba)
    return lp