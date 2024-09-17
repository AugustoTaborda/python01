from flask import Flask, render_template

app = Flask (__name__)

@app.route('/')

def index():
    #return "Olá galera!!!"
    return render_template("index.html",titulo="pagina inicial",usuario="Godofredo")
if __name__== '__main__':
    app.run(debug=True)