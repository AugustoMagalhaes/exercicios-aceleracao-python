from flask import Blueprint, render_template

# 1 - Crie o objeto Blueprint da home_controller, para o registro em app.py
home_controller = Blueprint("home_controller", __name__)


# 2 - Crie o endpoint GET /, que renderiza o template index.html
@home_controller.route("/", methods=["GET"])
def index():
    # 3 - Renderize a template index.html com a função render_template
    return render_template("index.html")
