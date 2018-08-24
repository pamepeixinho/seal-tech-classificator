from flask import Flask, request, jsonify
from commitmentClassificator import NeuralNetworks
from TestingScikitLearn import Predictor

appName = 'FocaAi'

my_dev_host = '0.0.0.0'
my_dev_port = 5000

app = Flask(appName)

globalPredictor = Predictor()
globalPredictor.load_model()

def setup_app(app):
    return 1


@app.route('/')
def home():
    return 'home'


@app.route('/health-check')
def health_check():
    return "Hello, I'm alive!"


@app.route('/upload')
def upload():
    # develop it
    return True


@app.route('/dashboard')
def dashboard():
    # develop it
    return True


@app.route('/classificate')
def classificate():
    emotions = request.args
    commitment = NeuralNetworks.classificate(emotions=emotions)
    return jsonify(commitment=commitment)


@app.route('/prediction-train')
def predictionTrain():
    predictor = Predictor()
    predictor.train()
    globalPredictor.load_model()


@app.route('/predict')
def predict():
    print(request.data)
    predictedCommitment = globalPredictor.predict(request.data)
    return jsonify(commitment=predictedCommitment)


setup_app(app)

if __name__ == '__main__':
    app.run(host=my_dev_host, port=my_dev_port)
