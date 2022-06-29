import os
import logging

from flask import Flask, request, jsonify, render_template

from model.model import Translate

app = Flask(__name__)

# define model path
model_path = './model/model.h5'

# create instance
model = Translate(model_path)
logging.basicConfig(level=logging.INFO)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/v1/translate", methods=["GET", "POST"])
def predict():
    """Provide main prediction API route. Responds to both GET and POST requests."""
    logging.info("Predict request received!")
    text = request.args.get("to-translate")
    prediction = model.predict(text)

    logging.info("prediction from model= {}".format(prediction))
    return jsonify({"translation": str(prediction)})

# Create the main driver function
port = int(os.environ.get("PORT", 5000)) # <-----
app.run(host='0.0.0.0', port=port)       # <-----
