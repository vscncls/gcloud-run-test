from flask import Flask
from os import environ

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello'


app.run('0.0.0.0', environ.get('PORT') or 8000)
