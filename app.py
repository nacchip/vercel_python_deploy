from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "hi"

@app.route('/about')
def home():
    return "about"

app.run(debug=True)
