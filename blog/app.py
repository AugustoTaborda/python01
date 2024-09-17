from flask import Flask, render_template

app = Flask(__name__)


@app.route('/listas_dicionario')
def listas_dicionario():
    usuarioinfos = [
        {"id": 1,
        "titulo":  "revista das famosas",
        "conteudo": "quem sabe? vc sabe? onde sabe?"},
        
        {"id": 2,
        "titulo":  "lista do livro da famosas",
        "conteudo": "la tem tudo? vc deve conhecer? só o submundo sabe?"},
        
        {"id": 3,
        "titulo":  "lista do livro do arrow",
        "conteudo": "aqui esta o historio do arrow"}
        ]
    return render_template('index.html',usuarioinfos=usuarioinfos )

if __name__ == '__main__':
    app.run(debug=True)