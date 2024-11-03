"""Python Flask WebApp Auth0 integration example
"""

import json
from os import environ as env
from urllib.parse import quote_plus, urlencode
from PIL import Image
import os
from keras.layers import *
import tensorflow as tf
from authlib.integrations.flask_client import OAuth
from dotenv import find_dotenv, load_dotenv
from flask import Flask, redirect, render_template, session, url_for

model2 = tf.saved_model.load("modelexport")

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

app = Flask(__name__)
app.secret_key = env.get("APP_SECRET_KEY")


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


# Controllers API
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=env.get("PORT", 5000))
