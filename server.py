from flask import Flask, render_template, url_for, redirect
from cupcakes import get_cupcakes, find_cupcake, add_cupcake_dictionary

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", cupcakes = get_cupcakes("display.csv"))

@app.route("/cupcakes")
def all_cupcakes():
    return render_template("index.html")

@app.route("/add-cupcake/<name>")
def add_cupcake(name):
    cupcake = find_cupcake("display.csv", name)

    if cupcake:
        add_cupcake_dictionary("orders.csv", cupcake)
        return redirect(url_for("home"))
    else:
        return "Sorry cupcake not found."

@app.route("/individual/<name>")
def individual_cupcake(name):
    cupcake = find_cupcake("display.csv", name)
    
    if cupcake:
        return render_template("individual.html", cupcake=cupcake)
    else:
        return "Sorry cupcake not found."

@app.route("/order")
def order():
    return render_template("order.html")

if __name__ == "__main__":
    app.env = "development"
    app.run(debug = True, port = 8000, host = "localhost")