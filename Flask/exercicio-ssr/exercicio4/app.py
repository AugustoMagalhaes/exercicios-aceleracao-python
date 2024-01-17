from flask import Flask, render_template, request
app = Flask(__name__)

products = []


@app.route("/", methods=["GET", "POST"])
def index():
    product = request.form.get('product')
    if request.method == "POST" and product.strip():
        global products
        products = [*products, product] if product else products
        product = None
        return render_template('index.html', products=products)
    return render_template('index.html', products=products)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
