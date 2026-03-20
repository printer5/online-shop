from flask import Flask, render_template
import database
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    products = database.get_products()
    return render_template("index.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)