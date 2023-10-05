from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello world with Flask'

@app.route('ladu')
def ladu():
    return 'Love from Ladu'

