from flask import Flask,request,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

aplication = Flask(__name__)
app = aplication

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predictdata",methods = ["Get","POST"])  
def predict_datapoint():
    if request.method == "GET":
        return render_template("home.html")

    else:
        pass

