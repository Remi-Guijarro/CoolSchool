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

def displayDifferentchoice(n_uplet):
    printHelp("\n Please Enter the probabilities of each subjects and chapters : \n \t -Note that if you put 0 on a SUBJECT or a CHAPTER, no questions will be asked you about that subject \n  Theses are the possible choices \n")
    for intitule in n_uplet:
        if "M_" in intitule: 
            print(intitule[2:])
        else:
            print(intitule)

def chooseSubjectProbabilities(map):
    displayDifferentchoice(map)
    for key, value in map.items():
        proba = input("Choose the propabilities for the subject : " + key + " :> ")
        map[key] = proba
    return map


def chooseChapterProbabilities(map):
    # displayDifferentchoice(map)
    for key, value in map.items():
        for keyy, valuee in value.items():
            proba = input("Choose the propabilities for the subject : " + keyy + " :> ")
            value[keyy] = proba
    return map


def  printInformation(message):
    print(Fore.CYAN + MSG_PREFIX + message + MSG_SUFFIX + "\n")
    print(Fore.RESET)

def printError(message):
    print(Fore.RED + MSG_PREFIX + message + MSG_SUFFIX + "\n")
    print(Fore.RESET)

def printWarning(message):
    print(Fore.YELLOW + MSG_PREFIX + message + MSG_SUFFIX + "\n")
    print(Fore.RESET)

def printHelp(message):
    print(Fore.LIGHTGREEN_EX + MSG_PREFIX + message + MSG_SUFFIX + "\n")
    print(Fore.RESET)