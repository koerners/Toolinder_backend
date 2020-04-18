import pandas as pd

# Lädt die Fragen aus dem JSON File und gibt sie zurück
def getQuestions():
    df = pd.read_json (r'./data/questions.json')
    return df.to_json(orient='index')


# Findet das Keyword basierend auf seiner ID
def getKeywordById(id):
    df = pd.read_json (r'./data/keywords.json')
    # TODO: Hier möchten wir natürlich nur das eine, gefragte Keyword zurückbekommen und nicht alle

    return df.to_json(orient='index')


# TODO: Hauptarbeit: Hier kommen die beantworteten Fragen rein und basierend darauf müssen die richtigen tools zurückgegeben werden
# @input:
# [
#   {
#     "q_id": 0,
#     "response": true
#   },
#   {
#     "q_id": 1,
#     "response": false
#   }
# ]
# ...
#
# @returns: In der vorgeschlagenen Reihenfolge:
# [{
#         "id": 0,
#         "name": "ad laborum",
#         "company": "PETICULAR",
#         "price": "nisi dolor",
#         "users": 1222,
#         "picture": "http://placehold.it/32x32",
#         "keywords": [
#             5,
#             15
#         ],
#         "pro": [
#             "cillum pariatur",
#             "aliquip deserunt"
#         ],
#         "con": [
#             "aliqua esse}",
#             "laborum est"
#         ]
#     }, ...]
# 


def calculateResult(content):
    dfTools = pd.read_json (r'./data/tools.json')
    print(content)
   # TODO: Hauptteil

    return dfTools.to_json(orient='index')