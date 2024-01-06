"""
ML MODEL
"""
import joblib


class Model:
    def __init__(self) -> None:
        self.scaler = joblib.load('model/scaler.pkl')
        self.model = joblib.load('model/model.pkl')

    def get_predict(self, value: list):
        line = self.scaler.transform(value)

        return self.model.predict(line)

    def load_model():
        pass