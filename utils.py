import csv


def compute_stat(user_name):
    print("getting stat")

#save the score of the current 'player' in the current mode
def save():
    print("writing file")

#return a list of objects ( dictionnary )
def get_subjects():
    objectsList=[]
    with open('subjects.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            line={}
            line["subject"]=row[0]
            line["chapter"]=row[1]
            line["theme"]=row[2]
            line["structure"]=row[3]
            objectsList.append(line)
    return objectsList
