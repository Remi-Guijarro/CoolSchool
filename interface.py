from colorama import init, Fore, Back, Style
from os import system, name
import utils
import time
import parser
from math import * 

PROBA_CHOICE_MSG="\n Veuillez entrer les probabilites de chaque sujets et chapitres : \n \t -Notez que si vous assigner  0 sur un sujet ou un  chapitre, aucune question en vous seront poser sur ces sujets ou themes \n Voici les choix possibles \n"
THEME_CHOICE_MSG="De 0 a 10, notez votre preference sur ce theme : "
MSG_PREFIX="========== "
MSG_SUFFIX=" =========="
MODE1="EXAM"
MODE2="ENTRAINNEMENT"
HELP="AIDE"
MODE_NOT_EXIST_ERROR="Ce mode m'existe pas ou pas encore"
HELP_MODE_MESSAGE="\n Examen : Une serie de 10 questions \n Entrainnement : un mode sans fin ou vous decidez de vous arreter quand vous le voulez \n"

#  return True if Exam mode have been choosed False otherwise
def chooseMode():
    init()
    while(True):
        print(Style.RESET_ALL)
        mode = input("Quel type de session voulez vous lancer ? ("+ MODE1 + "|" + MODE2 + "|" + HELP + ") :> ")
        mode = mode.upper().strip(' ')
        if(mode == MODE1):
            return mode
        elif(mode == MODE2):
            return mode
        elif(mode == HELP):
            clear()
            printHelp(HELP_MODE_MESSAGE)
            chooseMode()
        else:
            printError(MODE_NOT_EXIST_ERROR)

# Print the possible possible choice about (subjects) and 
# Todo : for the Chapters
def displayDifferentchoice(n_uplet):
    printHelp(PROBA_CHOICE_MSG)
    for intitule in n_uplet:
        if "M_" in intitule: 
            print(intitule[2:])
        else:
            print(intitule)

# Ask the user to define the probabilities for the subjects
# Return a dictionnary <Subject, probability>
def chooseSubjectProbabilities(map):
    displayDifferentchoice(map)
    values=[]
    probabilities=[]
    for key, value in map.items():
        user_input = input(THEME_CHOICE_MSG + key + "? :> ")
        user_input = int(user_input)
        values.append(user_input)
    probabilities = utils.distribute_in_probabilties(values)
    i = 0
    for key, value in map.items():
        map[key] = probabilities[i]
        i=i+1
    return map

# Ask the user to define the probabilities for the chapters
# Return a dictionnary <Subject,<chapter, probability>>
def chooseChapterProbabilities(mapchapters,mapSubject):
    values=[]
    probabilities=[]
    for key, value in mapchapters.items():
        print(key)
        for keyy, valuee in value.items():
            if(float(mapSubject[key]) != 0):                
                user_input = input(THEME_CHOICE_MSG + keyy + " :> ")
                user_input = int(user_input)
                values.append(user_input)
        probabilities = utils.distribute_in_probabilties(values)
        i=0
        for keyy, valuee in value.items():
            if(float(mapSubject[key]) != 0): 
                value[keyy] = probabilities[i]
                i=i+1
        values.clear()
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
    print("Q : " + Fore.LIGHTYELLOW_EX + str(message) + "\n")
    print(Fore.RESET)

def waitUntilReady():
    while(True):
        if(str(input("(o|n) :>")).upper() == "O"):
            clear()
            break

def printScore(nbPoint,i):
    if(float(nbPoint/i) < 0.5 and float(nbPoint/i) > 0.4):
        printWarning("Vous avez eu "+ str(nbPoint) + " /"+str(i)+" :| , Dommage ! ")
    elif(float(nbPoint/i) > 0.5 and float(nbPoint/i) < 0.80 ):
        printWarning("Vous avez eu "+ str(nbPoint) + " /"+str(i)+" , Pas mal ! ")
    elif(float(nbPoint/i) < 0.4):
        printError("Vous avez eu "+ str(nbPoint) + " /"+str(i)+" , :( Dommage ! ")
    elif(float(nbPoint/i) > 0.80):
        printInformation("Vous avez eu "+ str(nbPoint) + " /"+str(i)+" , Bravo  ! ")


def wanaQuit():
    if(str(input(" Voulez vous quitter ? (o|n) :>")).upper() == "O"):
        return True
    else:
        return False
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def wait(secs):
    time.sleep(secs)

def getUserAnswer():
    x=input("I :> ")
    if(str(x).upper() == "NONE" ):
        return "None"
    else:
        try:
            eval(parser.expr("\"{0:.2f}\".format(float("+str(x)+"),2)").compile())
            return parser.expr("\"{0:.2f}\".format(float("+str(x)+"),2)").compile()
        except:
            return "None"

def KeyBoardInterruptHandler():
    print("\n")
    if(wanaQuit()):
        return True
    else:
        return False