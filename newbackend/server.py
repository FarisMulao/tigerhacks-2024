"""Python Flask WebApp Auth0 integration example
"""
import random
import json
from os import environ as env
from urllib.parse import quote_plus, urlencode
from PIL import Image
import os
from keras.layers import *
import tensorflow as tf
from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, session, url_for, request
import mysql.connector
import numpy as np 
from flask_cors import CORS

model2 = tf.saved_model.load("modelexport")

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

app = Flask(__name__)
app.secret_key = env.get("APP_SECRET_KEY")
app.config['UPLOAD_FOLDER'] = "./uploads"
CORS(app)


mydb = mysql.connector.connect(
  host="host.docker.internal",
  user="plidbackend",
  password="password",
  database="pliddb"
)


oauth = OAuth(app)

oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration',
)



@app.route("/")
def home():
    return str(session.get("user")), 200
    return render_template(
        "home.html",
        session=session.get("user"),
        pretty=json.dumps(session.get("user"), indent=4),
    )


@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    #return str(session.get("user")['userinfo']), 200
    return redirect("/")


@app.route("/login")
def login():
    return oauth.auth0.authorize_redirect(
        redirect_uri="https://www.plid.us/callback" #url_for("callback", _external=True)
    )


@app.route("/logout")
def logout():
    session.clear()
    return redirect(
        "https://"
        + env.get("AUTH0_DOMAIN")
        + "/v2/logout?"
        + urlencode(
            {
                "returnTo": url_for("home", _external=True),
                "client_id": env.get("AUTH0_CLIENT_ID"),
            },
            quote_via=quote_plus,
        )
    )

@app.route('/getUserInfo', methods=['GET'])
def getUserInfo():
    userData = {}
    try:
        sessionData = session.get("user")['userinfo']
        userData['name'] = sessionData['nickname']
        userData['email'] = sessionData['name']
        return userData, 200
    except Exception as e:
        print(e)
        return "", 204
        
@app.route('/getUserPlants', methods=['GET'])
def getUserPlants():
    try:
        email = session.get("user")['userinfo']['name']
    except:
        return "", 403
    try:
        cursor = mydb.cursor()
        print(email)
        cursor.execute("SELECT plantid, planttype, startdate FROM plantList WHERE email = %s", [str(email)])
        data = cursor.fetchall()
    except Exception as e:
        print(e)
        return "database error", 500
    if len(data) == 0:
        return "", 204
    plantData = {}
    plantData['plantData'] = []
    for plant in data:
        plants = {}
        plants["plantid"] = plant[0]
        plants["planttype"] = plant[1]
        plants["startdate"] = plant[2]
        plantData['plantData'].append(plants)
    return plantData, 200

@app.route('/addUserPlant', methods=['POST'])
def addUserPlant():
    try:
        email = session.get("user")['userinfo']['name']
    except:
        return "", 403
        
    try:
        data = request.get_json()
        print(data)
        if not ("plantId" in data.keys()):
            return "Invalid input", 400
        planttype = data['plantId']
    except:
        return "", 500
    
    if planttype is None:
        return "Invalid input, none", 400
    
    try:
        print(str(email))
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO plantlist (email, planttype, startdate, plantid) VALUES (%s, %s, NOW(), UUID())", (str(email), planttype))
        mydb.commit()
        return "", 200
    except Exception as e:
        print(e)
        mydb.rollback()
        return "database error", 500

@app.route('/uploadimage', methods=['POST'])
def uploadImage():
    #print("HERE", request.files)
    if 'image' not in request.files:
        print("No file found in request.")
        return 'file not found', 406  
    file = request.files['image']
    if file.filename == '':
        print("No file uploaded")
        return 'no file uploaded', 406  

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

    test = model2.serve(testimg)  
    test1 = model2.serve(testimg)
    test2 = model2.serve(testimg)
    output = random.choice([int(np.argmax(test)), int(np.argmax(test1)), int(np.argmax(test2))])
    # Return based on model output
    return str(output), 200 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=env.get("PORT", 5000))
