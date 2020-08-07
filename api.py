from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello'


app.run('0.0.0.0', 8000)
