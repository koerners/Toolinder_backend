import pandas as pd
import regex as re

# Gibt alle Tools zurück
def loadAll():
    tools = pd.read_json(r'./data/tools.json')
    return tools.to_json(orient='records')



# Lädt die Fragen aus dem JSON File und gibt sie zurück
def getQuestions():
    df = pd.read_json(r'./data/questions.json')
    return df.to_json(orient='records')


# Findet das Keyword basierend auf seiner ID
def getKeywordById(id):
    df = pd.read_json(r'./data/keywords.json')
    # TODO: Hier möchten wir natürlich nur das eine, gefragte Keyword zurückbekommen und nicht alle
    df = df.loc[df['id'].isin([id])]
    return df.to_json(orient='records')


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

# test_input = ['{"q_id": 0,"response": true}', '{"q_id": 1,"response": false}']

def calculateResult(content):
    tools = pd.read_json(r'./data/tools.json')
    questionsAndKeywords = pd.read_json(r'./data/questionKeyword.json')

    answers = pd.DataFrame(content)

    print("------Antworten--------")
    print(answers)
    print("------Fragen und ihre Keywords--------")
    print(questionsAndKeywords)
    print("------Alle Tools--------")
    print(tools)

    keywordsAndAnswers = pd.merge(answers, questionsAndKeywords, on='q_id')
    print(keywordsAndAnswers)

    keywordsAndAnswers['keyword'] = keywordsAndAnswers.apply(lambda x: x.true if x.response is True else x.false, axis=1)
    keywordsAndAnswers = keywordsAndAnswers.drop(['true', 'false'], axis=1)

    #keywordsAndTools = pd.merge(keywordsAndAnswers, tools, on=)
    print(keywordsAndAnswers)

    return tools.to_json(orient='records')

# calculateResult(test_input)