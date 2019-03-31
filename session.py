from interface import *
from  utils import *
from solver import *
from sys import exit


INTEGRAL_INFO_MESSAGE="\n\n Resolvez cette integrale \n\n Les reponses sont attendues avec un arrondi au centieme. \n Si l'integrale ne converge pas dans les bornes donnees ecrivez => none \n\n Ce programme considere que si la limite d'une fonction a un point donnee depasse 10^11 \n alors l'integrale ne converge pas. \n"
POLYNOMIAL_INFO_MESSAGE=" \n\n S'il n'y a pas de racine dans R alors ecrivez : \n x1 :> none \n x2 :> none \n\n S'il n'y a qu'une seul racine ecrivez x1 :> Votre_Reponse \n x2 :> none \n\n Les reponses sont attendues avec une precision au centieme."
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
    
# Return a random chapter according subject given and their probabilities
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

def compareSolutions(result,x):
    if(result == str(x).strip()):
        printInformation("Good !")
        return True
    else:
        printError("result was " + str(result))
        return False

# Should return a random question according to the chapters given and their probabilities
#To do
def computeQuestion(theme):
    if(theme.strip().upper() == "SECONDDEGRE"):
        (a,b,c)=randomPolynomial()
        printInformation(POLYNOMIAL_INFO_MESSAGE)
        printQuestion("Quelles sont les racines du polynome suivant : "+format_polynome((a,b,c))) 
        x1=input("x1 :> ")
        x2=input("x2 :> ")
        if(polynomSolution((a,b,c),(x1,x2))):
            printInformation("Bravo !")
            return True
    elif(theme.strip().upper() == "FONCTIONSPUISSANCE"):
        x=get_rand()
        if(x < 0.5):
            (a,b)=randomIntegralBounds()
            (c,d,alpha)=randomPowValues_a()
            printWarning(INTEGRAL_INFO_MESSAGE)
            printQuestion(str("("+str(c)+"x -" + str(d) + ")^"+str(alpha)).replace("--","+",1) + "\t Borne inferieure: " + str(a) + ", borne superieure: " + str(b))
            result =powResolve_a((a,b),(c,d,alpha)) 
            return compareSolutions(result,eval(getUserAnswer()))
        else:
            (a,b)=randomIntegralBounds()
            c=randomPowValues_b((a,b))
            printWarning(INTEGRAL_INFO_MESSAGE)
            printQuestion(str("1/(x-"+str(c)+")").replace("--","+",1) + "\t Borne inferieure: " + str(a) + ", borne superieure: " + str(b))
            result =powResolve_b((a,b),c) 
            return compareSolutions(result,eval(getUserAnswer()))
    elif(theme.strip().upper() == "FONCTIONSTRIGONOMETRIQUES"):
        x=get_rand()
        if(x < 0.33):
            (a,b)=randomIntegralBounds()
            c=randomTrigo()
            printWarning(INTEGRAL_INFO_MESSAGE)
            printQuestion(str("cos("+str(c)+"x)") + "\t Borne inferieure: " + str(a) + ", borne superieure: " + str(b))
            result =trigoCosResolve((a,b),c) 
            return compareSolutions(result,eval(getUserAnswer()))
        elif(x < 0.66):
            (a,b)=randomIntegralBounds()
            c=randomTrigo()
            printWarning(INTEGRAL_INFO_MESSAGE)
            printQuestion(str("sin("+str(c)+"x)") + "\t Borne inferieure: " + str(a) + ", borne superieure: " + str(b))
            result =trigoSinResolve((a,b),c) 
            return compareSolutions(result,eval(getUserAnswer()))
        else:
            a,b,c=get_tanIntegralVariables()
            printWarning(INTEGRAL_INFO_MESSAGE)
            printQuestion(str("tan("+str(c)+"x)") + "\t Borne inferieure: " + str(a) + ", borne superieure: " + str(b))
            result=trigoTanResolve((a,b),c) 
            return compareSolutions(result,eval(getUserAnswer()))
    elif(theme.strip().upper() == "FONCTIONSLOGARITHMIQUES"):
        (a,b)=randomIntegralBounds(0,10)
        c=randomLog()
        printWarning(INTEGRAL_INFO_MESSAGE)
        printQuestion(str("ln("+str(c)+"x)") + "\t Borne inferieure: " + str(a) + ", borne superieure: " + str(b))        
        result=logResolve((a,b),c) 
        return compareSolutions(result,eval(getUserAnswer()))
# run the game in exam session
def exam_session(subjectsMap,chaptersMap):
    try:
        printInformation("Session en mode examen")
        nbPoint=0
        for i in range(1,11):
            printInformation("QUESTION "+ str(i))
            wait(0.5)
            subject=randSubject(subjectsMap)
            printInformation(subject)
            chapter=randchapters(subject,chaptersMap)
            printInformation(chapter)
            if(computeQuestion(str(chapter).replace(" ","",1).upper())):
                nbPoint+=1       
            waitUntilReady()
            clear()
        printScore(nbPoint,10)
    except KeyboardInterrupt:
        if(not KeyBoardInterruptHandlerCustom()):
            exam_session(subjectsMap,chaptersMap)
        else:
            exit()  

# Run the game in trainning session
def trainning_session(subjectsMap,chaptersMap):
    printInformation("Mode entrainement")
    nbPoint=0
    cpt=1
    while(True):    
        printInformation("QUESTION "+ str(cpt))
        subject=randSubject(subjectsMap)
        printInformation(subject)
        chapter=randchapters(subject,chaptersMap)
        printInformation(chapter)
        if(computeQuestion(str(chapter).replace(" ","",1).upper())):
            nbPoint+=1
        if(wanaQuit()): 
            print(cpt)   
            printScore(nbPoint,cpt)
            break    
        cpt+=1

# The main function of the game
def run():
    try:
        mode = chooseMode()    
        intitules=["M_Polynome","\tPolynome_Second degre","M_Integrales","\tIntegrales_Fonctions puissance","\tIntegrales_Fonctions trigonometriques","\tIntegrales_Fonctions logarithmiques"]
        subjectsArray,subjectsMap=constructIntituleMa(intitules)
        chaptersMap= constructIntituleChapters(intitules,subjectsArray)
        subjectsMap = chooseSubjectProbabilities(subjectsMap)
        chaptersMap = chooseChapterProbabilities(chaptersMap,subjectsMap)
        if(mode == MODE1):
            exam_session(subjectsMap,chaptersMap)
        elif(mode == MODE2):
            trainning_session(subjectsMap,chaptersMap)
        else:
            printError("Mode is not implemented.")
    except KeyboardInterrupt:
        if(not KeyBoardInterruptHandlerCustom()):
            run()
        else:
            exit()

