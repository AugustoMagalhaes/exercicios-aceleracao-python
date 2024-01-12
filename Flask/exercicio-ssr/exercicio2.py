from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="views")


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year


@app.route("/", methods=["GET", "POST"])
def book():
    book = None
    if request.method == "POST":
        title = request.form.get('title')
        author = request.form.get('author')
        year = request.form.get('year')

        book = Book(title=title, author=author, year=year)

    return render_template('book.html', book=book)


@app.route("/reset_book", methods=["POST"])
def reset_book():
    return redirect(url_for('book'))


if __name__ == "__main__":
    app.run(debug=True, port=8000)
