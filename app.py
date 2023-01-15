from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))
sc = StandardScaler()
Cat_Col = ['category','city','type']
Num_Col = ['room_count','bathroom_count' , 'size']
oe= OrdinalEncoder()
Pipeline = ColumnTransformer([
    ("num", StandardScaler(), Num_Col),
    ('cat', OrdinalEncoder(),Cat_Col)
])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sub", methods = ["POST"])
def submit():

    if request.method == "POST":
        Category = request.form["Category"]
        Room_count = request.form["Room_count"]
        bathroom_count = request.form["bathroom_count"]
        size = request.form["size"]
        Type = request.form["type"]
        city = request.form["city"]
        data=[[Category,Room_count,bathroom_count,size,Type,city],["Maisons et Villas",6.0,2.0,500.0,"À Vendre","Tunis"]]
        df = pd.DataFrame(data, columns=["category","room_count","bathroom_count","size","type","city"])
        float_features=Pipeline.fit_transform(df)
        prediction = model.predict(float_features)
    return render_template("sub.html", round(n = 10**prediction[0]))


if __name__ == "__main__" :
    app.run(debug=True)



