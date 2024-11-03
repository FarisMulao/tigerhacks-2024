from flask import Flask, request
from flask_cors import CORS
from flask_mysqldb import MySQL
import hashlib
import random
import time
import re
import requests
import keras
from PIL import Image
import os
from keras.layers import *
import tensorflow as tf
import numpy as np  # Added import for numpy

model2 = tf.saved_model.load("modelexport")

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./uploads"
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'plidbackend'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'pliddb'
app.config['CORS_HEADERS'] = 'Content-Type'

mysql = MySQL(app)

@app.route('/upload', methods=['POST'])
def uploadImage():
    print("HERE", request.files)
    if 'image' not in request.files:
        print("No file found in request.")
        return 'file not found', 406  #Changed format to ('message', status code)
    file = request.files['image']
    if file.filename == '':
        print("No file uploaded")
        return 'no file uploaded', 406  #Changed format to ('message', status code)

    # Save file with `file.filename` instead of `filename`
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Open, resize, and prepare the image for prediction
    image = Image.open(file_path)
    image = image.resize((256, 256))
    #print(image.size)
    testimg = np.array(image)
    print(testimg.shape)
    testimg = np.reshape(testimg, (1, 256, 256, 3))

    test = model2.serve(testimg)  # <-- Ensure this is the correct way to call model2

    # Return based on model output
    if np.max(test) > 0.4:
        return str(int(np.argmax(test))), 200  # <-- Changed format to (response, status code)
    else:
        return "100", 200  # Changed format to (response, status code)

# Run in debug mode to help with any future debugging
if __name__ == "__main__":
    app.run('localhost', 5000, debug=True)  # Added debug mode
