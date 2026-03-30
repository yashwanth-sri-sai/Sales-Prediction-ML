from flask import Flask,request,render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            item_weight=float(request.form.get('item_weight')),
            item_mrp=float(request.form.get('item_mrp')),
            item_fat_content=request.form.get('item_fat_content'),
            outlet_size=request.form.get('outlet_size'),
            outlet_location_type=request.form.get('outlet_location_type'),
            item_type=request.form.get('item_type')
        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=f"${round(results[0], 2)}")
    

if __name__=="__main__":
    app.run(host="0.0.0.0", debug=True)        


