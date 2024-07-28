from flask import Flask, render_template
import requests
import json
# Abrir terminal neste arquivo, executar o comando "python -m flask run" para rodar a aplicação.
#Python versão 3.12.4
#Flask versão 3.0.3
app = Flask(__name__)
@app.route('/' , methods=['GET'])

# função para tratar dados da API 'Random User API', pego somente primeiro nome, foto de maior qualidade e E-mail.
def buscar_dados():
    req = requests.get("https://randomuser.me/api/?results=100")
    data = json.loads(req.content)
    data = data['results']
    nome = []
    email = []
    picture = []
    for pessoa in data:
        primeiroNome = pessoa['name'].get('first')
        primeiraFoto = pessoa['picture'].get('large')
        nome.append(primeiroNome)
        email.append(pessoa['email'])
        picture.append(primeiraFoto)
   
    return render_template('index.html', len = len(nome),nomes=nome, emails=email, pic=picture)
      