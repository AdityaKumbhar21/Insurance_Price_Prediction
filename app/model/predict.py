import joblib
import pandas as pd


MODEL_VERSION = '1.0.0'


with open('../models/insurance_price_pipeline.pkl', 'rb') as f:
    model = joblib.load(f)


def predict_output(user_input: dict):
    df = pd.DataFrame([user_input])
    output = model.predict(df)[0]
    return output
