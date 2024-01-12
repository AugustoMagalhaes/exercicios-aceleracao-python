from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="views")
username = None


@app.route("/", methods=["GET", "POST"])
def index():
    global username
    username = request.form.get('username')

    if request.method == "POST":
        username = request.form.get('username')
        return render_template('index.html', username=username)

    return render_template('index.html', username=None)


@app.route("/reset_username", methods=["POST"])
def reset_username():
    global username
    username = None
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True, port=8000)
