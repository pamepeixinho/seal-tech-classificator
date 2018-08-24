from sklearn import tree
import pandas
import numpy
from sklearn.externals import joblib

class Predictor:
    dataset_filename = 'dataset.csv'
    model_filename = 'model.pkl'

    def __init__(self):
        self.inputs = []
        self.targets = []

    def _load_csv(self):
        with open(self.dataset_filename) as csvfile:
            data = pandas.read_csv(csvfile)
            self.data_set = numpy.array(data)

    def _split_input_target_from_csv(self):
        self.inputs = self.data_set[:, 0:8]
        self.targets = self.data_set[:, 8]
        print(self.inputs)
        print(self.targets)

    def _save_model(self):
        joblib.dump(self.clf, self.model_filename)

    def load_model(self):
        self.clf = joblib.load(self.model_filename)

    def train(self):
        self._load_csv()
        self._split_input_target_from_csv()

        self.clf = tree.DecisionTreeRegressor()

        self.clf.fit(self.inputs, self.targets)
        self._save_model()

    def predict(self, emotions):
        return self.clf.predict(emotions)

predictor = Predictor()
predictor.train()
