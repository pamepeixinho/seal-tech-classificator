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


def convert(value):
    return float(value)


@app.route('/predict')
def predict():
    emotionsDict = request.args
    emotions = [[
        convert(emotionsDict["anger"]), convert(emotionsDict["contempt"]),
        convert(emotionsDict["fear"]), convert(emotionsDict["disgust"]),
        convert(emotionsDict["happiness"]), convert(emotionsDict["neutral"]),
        convert(emotionsDict["sadness"]), convert(emotionsDict["surprise"])
    ]]

    predictedCommitment = globalPredictor.predict(emotions)
    return jsonify(commitment=predictedCommitment[0])

@app.route('/predict-average')
def predictAverage():
    # ?average_anger=0.976&average_contempt=0.00074&average_fear=0.000384723&average_disgust=0.0000000006&average_happiness=0.8&average_neutral=0.9&average_sadness=0&average_surprise=0

    # \?average_anger\=0.976\&average_contempt\=0.00074\&average_fear\=0.000384723\&average_disgust\=0.0000000006\&average_happiness\=0.8\&average_neutral\=0.9\&average_sadness\=0\&average_surprise\=0

    emotionsDict = request.args
    emotions = [[
        convert(emotionsDict["average_anger"]), convert(emotionsDict["average_contempt"]),
        convert(emotionsDict["average_fear"]), convert(emotionsDict["average_disgust"]),
        convert(emotionsDict["average_happiness"]), convert(emotionsDict["average_neutral"]),
        convert(emotionsDict["average_sadness"]), convert(emotionsDict["average_surprise"])
    ]]

    predictedCommitment = globalPredictor.predict(emotions)
    return jsonify(commitment=predictedCommitment[0])

setup_app(app)

if __name__ == '__main__':
    app.run(host=my_dev_host, port=my_dev_port)
