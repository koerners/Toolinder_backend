import pandas as pd

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


# Hier kommen die beantworteten Fragen rein und basierend darauf müssen die richtigen tools zurückgegeben werden
def calculateResult(content):
    tools = pd.read_json(r'./data/tools.json')
    questionsAndKeywords = pd.read_json(r'./data/questionKeyword.json')

    answers = pd.DataFrame(content)

    # print("------Antworten--------")
    # print(answers)
    # print("------Fragen und ihre Keywords--------")
    # print(questionsAndKeywords)
    # print("------Alle Tools--------")
    # print(tools)

    keywordsAndAnswers = pd.merge(answers, questionsAndKeywords, on='q_id')
    keywordsAndAnswers['keyword'] = keywordsAndAnswers.apply(lambda x: x.true if x.response is True else x.false,
                                                             axis=1)
    keywordsAndAnswers = keywordsAndAnswers.drop(['true', 'false', 'response'], axis=1).reset_index()

    def countKeywords(keywords):
        keyword_list = keywordsAndAnswers['keyword'].tolist()
        count = 0
        for k in keywords:
            if k in keyword_list:
                count += 1
        return count

    tools['keyword_hits'] = tools.keywords.apply(countKeywords)
    tools = tools.sort_values(['keyword_hits'], ascending=0)

    tools = tools.loc[tools.keyword_hits != 0]
    # print(tools[['name', 'keyword_hits']])

    return tools.to_json(orient='records')

