from colorama import init, Fore, Back, Style
from os import system, name

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

# Print the possible possible choice about (subjects) and 
# Todo : for the Chapters
def displayDifferentchoice(n_uplet):
    printHelp("\n Please Enter the probabilities of each subjects and chapters : \n \t -Note that if you put 0 on a SUBJECT or a CHAPTER, no questions will be asked you about that subject \n  Theses are the possible choices \n")
    for intitule in n_uplet:
        if "M_" in intitule: 
            print(intitule[2:])
        else:
            print(intitule)

# Ask the user to define the probabilities for the subjects
# Return a dictionnary <Subject, probability>
def chooseSubjectProbabilities(map):
    displayDifferentchoice(map)
    for key, value in map.items():
        proba = input("Choose the propabilities for the subject : " + key + " :> ")
        map[key] = proba
    return map

# Ask the user to define the probabilities for the chapters
# Return a dictionnary <Subject,<chapter, probability>>
def chooseChapterProbabilities(mapchapters,mapSubject):
    for key, value in mapchapters.items():
        for keyy, valuee in value.items():
            if(float(mapSubject[key]) != 0):                
                print(key)
                proba = input("Choose the propabilities for the chapter : " + keyy + " :> ")
                value[keyy] = proba
    return mapchapters

# Print an Information message (COLOR = CYAN)
def printInformation(message):
    print(Fore.CYAN + MSG_PREFIX + str(message)  + MSG_SUFFIX + "\n")
    print(Fore.RESET)

# Print a Error message (COLOR = RED)
def printError(message):
    print(Fore.RED + MSG_PREFIX + str(message) + MSG_SUFFIX + "\n")
    print(Fore.RESET)

# Print a Warning message (COLOR = YELLOW)
def printWarning(message):
    print(Fore.YELLOW + MSG_PREFIX + str(message) + MSG_SUFFIX + "\n")
    print(Fore.RESET)

# Print an Help message (COLOR = LIGHTGREEN)
def printHelp(message):
    print(Fore.LIGHTGREEN_EX + MSG_PREFIX + str(message) + MSG_SUFFIX + "\n")
    print(Fore.RESET)

def printQuestion(message):
    print(Fore.LIGHTYELLOW_EX + str(message) + "\n")
    print(Fore.RESET)

def waitUntilReady():
    while(True):
        if(str(input("(y|n) :>")).upper() == "Y"):
            clear()
            break
    

def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 