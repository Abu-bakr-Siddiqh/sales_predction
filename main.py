from flask import *
import pickle
import numpy as np
import pandas as pd
import sklearn
import re
import random
from random import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,3)
    loaded_model = pickle.load(open("sales_prediction.pkl", "rb"))
    sales = loaded_model.predict(to_predict)
    return sales[0]


@app.route('/result', methods=['GET','POST'])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if (len(to_predict_list)==3):
            sales = ValuePredictor(to_predict_list)
    sales = round(sales,3)
    return(render_template('index.html', prediction = "Sales of your products is {}".format(sales)))

if __name__ == "__main__":
    app.run(debug=True)