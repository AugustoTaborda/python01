from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index(): 
    usuario = {
        'name': "Arombado",
        'idade': 5 
    }
    itens = [ 'coca podre','pananas','cerveja']
    
    context = {
        'usuario': usuario,
        'itens': itens,
        'esta_logado': True,
        'dado': {'nome': 'flask','versao': 2.0}
    }
    
    return render_template('index.html', **context)

@app.route('/detalhes/')
def detalhes():
    usuario = {
        'nome': 'GordoFobia',
        'idade': 999 
        }
    return render_template('detalhes.html', usuario=usuario)

if __name__ == '__main__':
    app.run(debug=True, port=4000)