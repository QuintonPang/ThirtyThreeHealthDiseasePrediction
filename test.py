from flask import Flask, request
import pandas as pd
import numpy as np
from joblib import load

app = Flask(__name__)
from pathlib import Path
THIS_FOLDER = Path(__file__).parent.resolve()
@app.route("/")
def hello():
    return "Welcome to machine learning model APIs!"

@app.route('/predict', methods=['POST'])
def predict():
    json_ = request.json

    # Prepare Test Data
    df_test = pd.DataFrame(columns=list(json_.keys()))
    df_test.loc[0] = np.array(list(json_.values()))

    # Load pre-trained model
    clf = load(my_file = THIS_FOLDER /"saved_model/random_forest.jobliby")
    result = clf.predict(df_test)
    #print(f"Predicted Disease: {result}")
    
    
    #return f"Predicted Disease: {result}"
    return f"{result[0]}"  




if __name__ == '__main__':
    app.run(debug=True)