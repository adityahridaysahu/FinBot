from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask app running in a Docker container!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
