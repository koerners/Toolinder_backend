from klein import Klein
from responses import *
import json

app = Klein()
resource = app.resource

# Zeigt uns, dass die Verbindung besteht
@app.route('/')
def checkConnection(self):
    self.setHeader('Access-Control-Allow-Origin', '*')
    return ("Connected")

# App fragt nach den Fragen
# @return: alle Fragen als JSON
@app.route('/questions', methods=['GET'])
def returnQuestions(self):
    self.setHeader('Access-Control-Allow-Origin', '*')
    self.setHeader('Content-Type', 'application/json')
    return getQuestions()

# Soll die Daten eines Keywords zurückgeben 
# @return: EIN Keyword mit allen Daten als JSON
@app.route('/keyword/<string:id>', methods=['GET'])
def returnKeyword(self, id):
    self.setHeader('Access-Control-Allow-Origin', '*')
    self.setHeader('Content-Type', 'application/json')
    return getKeywordById(id)

# Nimmt die Antworten entgegen und gibt eine JSON mit den vorgeschlagenene Tools zurück
@app.route('/result', methods=['POST'])
def returnResult(request):
    content = json.loads(request.content.read())
    request.setHeader('Access-Control-Allow-Origin', '*')
    request.setHeader('Content-Type', 'application/json')
    return calculateResult(content)