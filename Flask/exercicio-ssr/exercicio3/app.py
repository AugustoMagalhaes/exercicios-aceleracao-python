from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__ )

movies = [
    {"title": "A vida é bela", "year": 1999},
    {"title": "Titanic", "year": 1997},
    {"title": "Cidade de Deus", "year": 2002},
    {"title": "O Fabuloso Destino de Amélie Poulain", "year": 2001}
]


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html', movies=movies)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
