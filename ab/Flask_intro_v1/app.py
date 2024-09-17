from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    #return "rola na galera"
    
@app.route('/Variais')
def variaveis():
    nome = 'fredorento'
    return render_template('variais.html', usuario=nome)

@app.route('/listas')
def listas():
    itens = ['item 1', 'item 2', 'item 3', 'item 4']
    return render_template('listas.html', itens=itens)

@app.route('/revista')
def dicionarios():
    usuario_info = {
        "log": "famosas",
        "idade": 18,
        "onde": "revista das famosas",
        "interesses": {"quem sabe","vc sabe?","onde sabe?"}
    }
    return render_template('revista.html', usuario=usuario_info)


@app.route('/listas_revistas')
def lista_revistas():
    usuarios = [ 
                {"name": "comi quem leu",
                "onde": "revista das famosas",
                "interesse": {"quem sabe","vc sabe?","onde sabe?"}}]
    return render_template('listas_revistas.html', lista_revistas=usuarios)

@app.route('/controle_de_condicao')
def controle_condicao():
    usuario = {
        "nome": "Arombado",
        "idade": 17,
        "cidade": "jaragua do sul",
        "premium": True
    }
    
    return render_template('controle_de_condicao.html', usuario=usuario)


@app.route('/filtros_jinja')
def filtros_jinja():
     usuario = {
        "nome": "Arombado",
        "idade": 17,
        "cidade": "jaragua do sul",
    }
     mensagem = "Bem-vindo ao site"
     return render_template('filtros_jinja.html', usuario=usuario, mensagem=mensagem)
 
if __name__ == '__main__':
    app.run(debug=True)
    
    