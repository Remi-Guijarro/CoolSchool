from colorama import init, Fore, Back, Style

MODE1="EXAM"
MODE2="TRAINING"

#  return 1 if Exam mode have been choosed 0 otherwise
def chooseMode():
    init(convert=True)
    while(True):
        print(Style.RESET_ALL)
        mode = input("Which mode do you want to run ? ("+ MODE1 + "|" + MODE2 + ") :> ")
        if(mode.upper() == MODE1):
            return 1
        elif(mode.upper() == MODE2):
            return 0
        else:
            print(Fore.RED + "The given mode does not exist \n" )
    return mode


def chooseProbabilities(n_uplet):
    lp=[]
    for intitule in n_uplet:
        proba = input("Choose the propabilities for : " + intitule)
        lp.append(proba)
    return lp