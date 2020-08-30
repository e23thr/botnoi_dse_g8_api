import pandas as pd
import pickle
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))  # application file root
APP_MODEL = os.path.join(APP_ROOT, 'Model/')  # Model folder


def predict_house_price(area, bedrooms, restrooms, floors):
    # Load pre-train model
    model = pickle.load(open(APP_MODEL + 'house_price_model.p', "rb"))
    # Predict price
    input_df = pd.DataFrame({"area": [area], "bedrooms": [bedrooms], "restrooms": [restrooms], "floors": [floors]})
    predict = model.predict(input_df)
    return predict[0]
