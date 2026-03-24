from flask import Flask, render_template, request, redirect, url_for
import database
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    products = database.get_products()
    return render_template("index.html", products=products)

@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        name = request.form['name']
        price = float(request.form['price'])
        description = request.form.get('description')
        image = request.files.get('image')

        filename = secure_filename(image.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(image_path)

        database.add_product(name, price, description, image_path)
        return redirect(url_for('index'))
    else:
        return render_template("add_product.html")
    
@app.route("/product/<int:product_id>")
def product(product_id):
    product = database.get_product_by_id(product_id)
    if product:
        return render_template("product.html", product=product)
    else:
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)