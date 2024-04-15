from flask import Flask, jsonify
from fct_app import *

app = Flask(__name__)

@app.route('/get_info')
def route():
    d = {
        "object" : "masina"
    }
    return d


if __name__ == "__main__":
    app.run(debug=True, port=5000)