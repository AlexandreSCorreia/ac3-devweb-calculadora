from flask import Flask, render_template, request, json

STATIC_FOLDER = 'templates/assets'
app = Flask(__name__,
            static_folder=STATIC_FOLDER)


@app.route('/')
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


@app.route('/home')
def main():
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


@app.route('/calculadora')
def calculadora_index():
    return render_template("calculadora.html",
                           data={"titulo": "Calculadora"})


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


if __name__ == '__main__':
    app.run(debug=True)
