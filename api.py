from flask import Flask
from os import environ
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()


@app.route('/')
def index():
    return 'hello'


@app.route('/secret')
def secret():
    return environ.get('TESTE_SECRET')


app.run('0.0.0.0', environ.get('PORT') or 8000)
