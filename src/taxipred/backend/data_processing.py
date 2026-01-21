import joblib
from taxipred.utils.constants import MODEL_PATH


class TaxiData:
    def __init__(self):
        artifact = joblib.load(MODEL_PATH)

        self.model = artifact["model"]
        self.features = artifact["features"]