from colorama import init, Fore, Back, Style

MSG_PREFIX="========== "
MSG_SUFFIX=" =========="
MODE1="EXAM"
MODE2="TRAINING"

#  return True if Exam mode have been choosed False otherwise
def chooseMode():
    init(convert=True)
    while(True):
        print(Style.RESET_ALL)
        mode = input("Which mode do you want to run ? ("+ MODE1 + "|" + MODE2 + ") :> ")
        if(mode.upper() == MODE1):
            return True
        elif(mode.upper() == MODE2):
            return False
        else:
            printError("The given mode does not exist" )
    return mode


def chooseProbabilities(n_uplet):
    lp=[]
    for intitule in n_uplet:
        proba = input("Choose the propabilities for : " + intitule)
        lp.append(proba)
    return lp

def  printInformation(message):
    print(Fore.CYAN + MSG_PREFIX + message + MSG_SUFFIX + "\n")
    print(Fore.RESET)

def printError(message):
    print(Fore.RED + MSG_PREFIX + message + MSG_SUFFIX + "\n")
    print(Fore.RESET)

def printWarning(message):
    print(Fore.YELLOW + MSG_PREFIX + message + MSG_SUFFIX + "\n")
    print(Fore.RESET)
