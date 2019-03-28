from interface import *
from  utils import *
from solver import *


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

def printScore(nbPoint,i):
    if(float(nbPoint/i) < 0.5 and float(nbPoint/i) > 0.4):
        printWarning("You've pointed "+ str(nbPoint) + " /"+str(i)+" :| , Try harder next time ! ")
    elif(float(nbPoint/i) > 0.5 and float(nbPoint/i) < 0.80 ):
        printWarning("You've pointed "+ str(nbPoint) + " /"+str(i)+" , that's nice ! ")
    elif(float(nbPoint/i) < 0.4):
        printError("You've pointed "+ str(nbPoint) + " /"+str(i)+" , :(  Try harder next time ! ")
    elif(float(nbPoint/i) > 0.80):
        printError("You've pointed "+ str(nbPoint) + " /"+str(i)+" , you're a monster ! ")

# Should return a random question according to the chapters given and their probabilities
#To do
def computeQuestion(theme):
    if(theme.strip().upper() == "SECONDDEGRE"):
        (a,b,c)=randomPolynomial()
        printInformation(" \n\n If there is no answers in R ( for example in the case of negative delta ) write : \n x1 :> none \n x2 :> none \n\n -If there is only one roots please write :> <your_answer>,none \n\n please note that answers are needed with a 2 digits precision")
        printQuestion("What are the roots of the following polynomial : "+format_polynome((a,b,c))) 
        x1=input("x1 :> ")
        x2=input("x2 :> ")
        if(polynomSolution((a,b,c),(x1,x2))):
            printInformation("Good !")
            return True
    elif(theme.strip().upper() == "FONCTIONSPUISSANCE"):
        x=get_rand()
        if(x < 0.5):
            (a,b)=randomIntegralBounds()
            (c,d,alpha)=randomPowValues_a()
            printWarning("\n\n Solve this integral equation , I : <Your_answer> \n\n please note that answers are needed with a 2 digits precision \n\n  For exemple if the answer is \n\t-0.000121516 ==> you should print -0.00 \n\n\t0.00121651 ==> you should print 0.00 \n\n\t 31 => you should print 31.00 \n\n\t If the Integral does not converge in the given bounds print => none \n\n note that this programm consider that if the limit of the function at one point within the given bounds exceed 300000000000 \n then the Integral does not converge ")
            printQuestion(str("("+str(c)+"x -" + str(d) + ")^"+str(alpha)).replace("--","+",1) + "\t Betwwen bounds " + str(a) + " To " + str(b))
            x=input("I :> ")
            result =powResolve_a((a,b),(c,d,alpha)) 
            return compareSolutions(result,x)
        else:
            (a,b)=randomIntegralBounds()
            c=randomPowValues_b((a,b))
            printWarning("\n\n Solve this integral equation , I : <Your_answer> \n\n please note that answers are needed with a 2 digits precision \n\n  For exemple if the answer is \n\t-0.000121516 ==> you should print -0.00 \n\n\t0.00121651 ==> you should print 0.00 \n\n\t 31 => you should print 31.00 \n\n\t If the Integral does not converge in the given bounds print => none \n\n note that this programm consider that if the limit of the function at one point within the given bounds exceed 300000000000 \n then the Integral does not converge \n\n")
            printQuestion(str("1/(x-"+str(c)+")").replace("--","+",1) + "\t Betwwen bounds " + str(a) + " To " + str(b))
            x=input("I :> ")
            result =powResolve_b((a,b),c) 
            return compareSolutions(result,x)
    elif(theme.strip().upper() == "FONCTIONSTRIGONOMETRIQUES"):
        x=get_rand()
        if(x < 0.33):
            (a,b)=randomIntegralBounds()
            c=randomTrigo()
            printWarning("\n\n Solve this integral equation , I : <Your_answer> \n\n please note that answers are needed with a 2 digits precision \n\n  For exemple if the answer is \n\t-0.000121516 ==> you should print -0.00 \n\n\t0.00121651 ==> you should print 0.00 \n\n\t 31 => you should print 31.00 \n\n\t If the Integral does not converge in the given bounds print => none \n\n note that this programm consider that if the limit of the function at one point within the given bounds exceed 300000000000 \n then the Integral does not converge ")
            printQuestion(str("cos("+str(c)+"x)") + "\t Betwwen bounds " + str(a) + " To " + str(b))
            x=input("I :> ")
            result =trigoCosResolve((a,b),c) 
            return compareSolutions(result,x)
        elif(x < 0.66):
            (a,b)=randomIntegralBounds()
            c=randomTrigo()
            printWarning("\n\n Solve this integral equation , I : <Your_answer> \n\n please note that answers are needed with a 2 digits precision \n\n  For exemple if the answer is \n\t-0.000121516 ==> you should print -0.00 \n\n\t0.00121651 ==> you should print 0.00 \n\n\t 31 => you should print 31.00 \n\n\t If the Integral does not converge in the given bounds print => none \n\n note that this programm consider that if the limit of the function at one point within the given bounds exceed 300000000000 \n then the Integral does not converge \n\n")
            printQuestion(str("sin("+str(c)+"x)") + "\t Betwwen bounds " + str(a) + " To " + str(b))
            x=input("I :> ")
            result =trigoSinResolve((a,b),c) 
            return compareSolutions(result,x)
        else:
            (a,b)=randomIntegralBounds()
            c=randomTrigo()
            printWarning("\n\n Solve this integral equation , I : <Your_answer> \n\n please note that answers are needed with a 2 digits precision \n\n  For exemple if the answer is \n\t-0.000121516 ==> you should print -0.00 \n\n\t0.00121651 ==> you should print 0.00 \n\n\t 31 => you should print 31.00 \n\n\t If the Integral does not converge in the given bounds print => none \n\n note that this programm consider that if the limit of the function at one point within the given bounds exceed 300000000000 \n then the Integral does not converge \n\n")
            printQuestion(str("tan("+str(c)+"x)") + "\t Betwwen bounds " + str(a) + " To " + str(b))
            x=input("I :> ")
            result=trigoTanResolve((a,b),c) 
            return compareSolutions(result,x)
    elif(theme.strip().upper() == "FONCTIONSLOGARITHMIQUES"):
        (a,b)=randomIntegralBounds()
        c=randomLog()
        printWarning("\n\n Solve this integral equation , I : <Your_answer> \n\n please note that answers are needed with a 2 digits precision \n\n  For exemple if the answer is \n\t-0.000121516 ==> you should print -0.00 \n\n\t0.00121651 ==> you should print 0.00 \n\n\t 31 => you should print 31.00 \n\n\t If the Integral does not converge in the given bounds print => none \n\n note that this programm consider that if the limit of the function at one point within the given bounds exceed 300000000000 \n then the Integral does not converge ")
        printQuestion(str("ln("+str(c)+"x)") + "\t Betwwen bounds " + str(a) + " To " + str(b))
        x=input("I :> ")
        result =trigoCosResolve((a,b),c) 
        return compareSolutions(result,x)      
# run the game in exam session
def exam_session(subjectsMap,chaptersMap):
    printInformation("Running in exam mode")
    nbPoint=0
    for i in range(1,19):
        printInformation("QUESTION "+ str(i))
        wait(1)
        subject=randSubject(subjectsMap)
        printInformation(subject)
        chapter=randchapters(subject,chaptersMap)
        printInformation(chapter)
        if(computeQuestion(str(chapter).replace(" ","",1).upper())):
            nbPoint+=1
        printInformation("Ready for another question ? ")        
        waitUntilReady()
        clear()
    printScore(nbPoint,20)

# Run the game in trainning session
def trainning_session(subjectsMap,chaptersMap):
    printInformation("Running in trainning mode")
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
