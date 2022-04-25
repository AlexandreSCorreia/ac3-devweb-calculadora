from flask import Flask, render_template, request, json, url_for,redirect, session
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/')
@app.route('/home')
def index():
    conteudo_header = {
        "titulo": "Desenvolvimento Web",
        "sub_titulo": "Projeto basico - criar uma calculadora"}

    conteudo_body = {
        "titulo": "Objetivo",
        "descricao": """
                        Criar um projeto simples de uma calculadora
                        utilizando o front-end e backend que foi ensinado em aula
                        e este projeto passar em todos os testes do script de teste
                        disponibilizado pelo professor.""",
        "nome_lista": "Teconologias"}

    tecnologias = ["HTML", "CSS", "JavaScrip", "Python", "Flask"]
    link = "https://github.com/AlexandreSCorreia/ac3-devweb-calculadora"
    return render_template("index.html",
                        data={"titulo": "Home",
                                "projeto": "AC3 - Calculadora flask"},
                        conteudo_header=conteudo_header,
                        conteudo_body=conteudo_body,
                        tecnologias=tecnologias,
                        linkgit=link)


@app.route('/resultado')
def resultado():
    result = 0

    if "ope" in request.args:
        if "a" in request.args:
            if "b" in request.args:
                try:
                    a = float(request.args["a"].replace(",", "."))
                    b = float(request.args["b"].replace(",", "."))
                except ValueError:
                    return json.dumps({
                        "ERRO": "Valor invalido, por favor informe um numero"})

                if(request.args["ope"] == "mult"):
                    result = a * b

                if(request.args["ope"] == "div"):
                    if b != 0:
                        result = float('{:.2f}'.format((a / b)))
                    else:
                        return json.dumps({
                            "ERRO": "Não é possivel dividir por zero!"})

                if(request.args["ope"] == "soma"):
                    result = a + b

                if(request.args["ope"] == "sub"):
                    result = a - b
            else:
                return json.dumps({"ERRO": "Valor de (b) não foi informado"})
        else:
            return json.dumps({"ERRO": "Valor de (a) não foi informado"})
    else:
        return json.dumps({"ERRO": "Operação não foi selecionada"})

    return json.dumps({"result": result})

@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        user = request.form['user']
        senha = request.form['senha']

        if user == "Admin" and senha == "1234":
            session["usuario_logado"] = True
            return redirect(url_for("painel_index"))

    return render_template("login.html",
                           data={"titulo": "Login"})

# PAINEL ADMIN
@app.route('/app/painel')
def painel_index():
    history = [{
            "nome": "Fulando Sei lá",
            "email": "fulano@exemple.com",
            "date": "2022-04-24",
            "type":"Member",
            "status":"offline"
        },
        {
            "nome": "Fulando2 Sei lá",
            "email": "fulano2@exemple.com",
            "date": "2022-04-22",
            "type":"Member",
            "status":"offline"
        },
        {
            "nome": "Fulando3 Sei lá",
            "email": "fulano3@exemple.com",
            "date": "2022-04-06",
            "type":"Member",
            "status":"offline"
        }]

    return render_template("dashboard.html",
                           data={"titulo": "Dashboard",
                           "history" : history},
                           nav="default")

@app.route('/app/painel/pages/home')
def painel_pages_home():
    return render_template("dashboard.html",
                           data={"titulo": "Dashboard - Home"},
                           nav="page_home")

@app.route('/app/painel/logout')
def painel_logout():
    session["usuario_logado"] = False
    return redirect(url_for("index"))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
