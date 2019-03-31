from flask import Flask, render_template,url_for
from interface import chooseChapterProbabilities,chooseSubjectProbabilities
from session import constructIntituleMa,constructIntituleChapters
from pprint import pprint

app = Flask(__name__)

intitules=["M_Polynome","\tPolynome_Second degre","M_Integrales","\tIntegrales_Fonctions puissance","\tIntegrales_Fonctions trigonometriques","\tIntegrales_Fonctions logarithmiques"]
subjectsArray,subjectsMap=constructIntituleMa(intitules)
chaptersMap= constructIntituleChapters(intitules,subjectsArray)

@app.route("/")
def home():
    pprint(chaptersMap)
    return render_template('home.html',chapters=chaptersMap)