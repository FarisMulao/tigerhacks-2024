from flask import Flask, request
#from flask_cors import CORS
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

model2 = tf.saved_model.load("modelexport")

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./uploads"
#CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'plidbackend'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'pliddb'
app.config['CORS_HEADERS'] = 'Content-Type'

mysql = MySQL(app)


@app.route('/upload', methods=['POST'])
def uploadImage():
    if 'file' not in request.files:
        return 404, 'file not found'
    file = request.files['file']
    if file.filename == '':
        return 404, 'no file uploaded'
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    image = Image.open(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    image = image.resize((256, 256))
    testimg = np.array(image)
    testimg = np.reshape(testimg, (1, 256, 256, 3))
    test = model2.serve((testimg))
    if np.max(test) > .4:
        return 200, int(np.argmax(test))
    else:
        return 200, 100
              

app.run('localhost', 5000)