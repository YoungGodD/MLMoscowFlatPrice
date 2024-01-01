"""
ML MODEL
"""
import pandas as pd
import joblib


def get_data():
    scaler = joblib.load('FlatPrice\App\model\scaler.pkl')
    model = joblib.load('FlatPrice\App\model\model.pkl')

    value = [[44, 28, 6.0, 23.5, 7, 1, 0, 1]]
    line = scaler.transform(value)

    return model.predict(line)

def model():
    pass