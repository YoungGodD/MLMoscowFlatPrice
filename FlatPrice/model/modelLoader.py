"""
ML MODEL
"""
import pandas as pd
import joblib


class Model:
    def __init__(self) -> None:
        self.scaler = joblib.load('/Users/igorrazgulaev/Yandex.Disk.localized/MLFaltPrice/FlatPrice/model/scaler.pkl')
        self.model = joblib.load('/Users/igorrazgulaev/Yandex.Disk.localized/MLFaltPrice/FlatPrice/model/model.pkl')

    def get_data(self, value: list):
        value = [[44, 28, 6.0, 23.5, 7, 1, 0, 1]]
        line = self.scaler.transform(value)

        return self.model.predict(line)

    def load_model():
        pass