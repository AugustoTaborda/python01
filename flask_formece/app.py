from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methonds=["GET", "POST"])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        idade = request.form['idade']
        mensagem = request.form['mensagem']
        
        #dados formulario ( salvar em um banco de dados ou enviar para um email)
        
        
        print(f"Nome:  {nome}, E-email: {email}, Idade: {idade}, Mensagem: {mensagem}")
        
        return redirect(url_for('obrigado'))
    
    return render_template('formulario.html')


@app.route('/obrigado')
def obrigado():
    return "mandou formulario"


if __name__ == '__main__':
    app.run(debug=True)