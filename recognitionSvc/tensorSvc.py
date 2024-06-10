from flask import Flask, jsonify
import tensorflow as tf
# from tensorflow.keras import layers, models
from tensorflow.python.keras import layers, models


# app = Flask(__name__)

print(tf.__version__)

# @app.route('/get_info')
# def route():
#     d = {
#         "object" : "masina"
#     }
#     return d


# if __name__ == "__main__":
#     app.run(debug=True, port=5000)