from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Laboratorio Pipeline Devops vFinal - Solution Sprint"

if __name__ == '__main__':
    app.run()