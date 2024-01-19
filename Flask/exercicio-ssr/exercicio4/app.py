from flask import Flask, render_template, request, redirect, abort, url_for
app = Flask(__name__)

products = []


@app.route("/", methods=["GET", "POST"])
def index():
    product = request.form.get('product')
    if request.method == "POST" and product.strip():
        global products
        products = [*products, product] if product else products
        product = None
        return redirect(url_for("index"))
    return render_template('index.html', products=products)


@app.route("/delete_product/<product>", methods=["POST"])
def delete_product(product):
    # Encontra o produto na lista pelo id
    product = next((p for p in products if p == product), None)
    # Se o produto não existir, retorna um erro 404
    if product is None:
        abort(404, f"Produto de nome '{product}' não encontrado.")
    # Se o produto existir, remove ele da lista
    products.remove(product)
    # Retorna uma mensagem de sucesso 200
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, port=8000)
