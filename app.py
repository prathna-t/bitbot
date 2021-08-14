from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

url = 'https://bitcoin-bot.azurewebsites.net/qnamaker/knowledgebases/c75ab0af-4311-4ebc-b37b-e214044c80d3/generateAnswer'
end_point = 'a0381bef-9495-4bae-aa2b-a23e78757664'

headers = {
  'Authorization': 'EndpointKey ' + str(end_point).strip(),
  'Content-type': 'application/json',
  }

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/ask/<text>")
def ask(text):
    data = """{'question':'""" + text + """'}"""
    response = requests.post(
        str(url).strip(),
        headers=headers, data=data)
    information = json.loads(response.text)
    return information['answers'][0]['answer']
