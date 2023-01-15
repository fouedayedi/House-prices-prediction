from flask import Flask, render_template, request, jsonify
import pickle


app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sub", methods = ["POST"])
def submit():
    if request.method == "POST":
        name = request.form["username"]
    return render_template("sub.html", n = name)


if __name__ == "__main__" :
    app.run(debug=True)
