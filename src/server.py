from flask import Flask

appName = 'FocaAi'

my_dev_host = '0.0.0.0'
my_dev_port = 5000

app = Flask(appName)


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


setup_app(app)

if __name__ == '__main__':
    app.run(host=my_dev_host, port=my_dev_port)
