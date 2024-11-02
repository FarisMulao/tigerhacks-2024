from flask import Flask, request
from flask_cors import CORS
from flask_mysqldb import MySQL
import hashlib
import random
import time
import re
import requests

app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'plidbackend'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'pliddb'
app.config['CORS_HEADERS'] = 'Content-Type'

mysql = MySQL(app)

# #token format is [username, tokenId, expireTimeStamp]
# tokens = []

# def verifyAuth(token):
#     for row in tokens:
#         if token == row[1]:
#             return row[0]
#     return ""

# def getGameAccount(accountId):
#     # this is a bad approach, but we will be using gdbrowser instead of querying robtop's database directly
#     try:
#         idRequest = requests.get("https://gdbrowser.com/u/" + str(accountId), allow_redirects=False)
#     except Exception as e:
#         print("error during request")
#         print(e)
#         return False
#     if idRequest.status_code == 302:
#         print("account id " + str(accountId) + " not found when querying gdbrowser")
#         return False
#     if idRequest.status_code != 200:
#         print("unknown error occured")
#         print(idRequest.status_code)
#         print(idRequest.text)
#         return False

#     # now that we found a valid profile, grab the username, stars, moons, and num demons
#     # get profile name from title of page
#     username = re.findall("<title>([a-zA-X0-9]+)'s Profile</title>", idRequest.text)
#     if len(username) != 1:
#         print("trouble finding username for account id " + str(accountId))
#         return False
#     username = username[0]

#     # get num stars
#     numStars = re.findall("Stars: ([0-9]+) \|", idRequest.text)
#     if len(numStars) == 0:
#         print("trouble getting number of stars")
#         return False
#     numStars = numStars[0]
#     if not numStars.isdigit():
#         print("Trouble Processing stars")
#         print(numStars)
#         return False

#     # get num moons
#     numMoons = re.findall("id=\"moons\">([0-9]+)</span>", idRequest.text)
#     if len(numMoons) == 0:
#         print("trouble getting number of moons")
#         return False
#     numMoons = numMoons[0]
#     if not numMoons.isdigit():
#         print("Trouble Processing Moons")
#         print(numMoons)
#         return False

#     # get num demons
#     numDemons = re.findall("\| Demons: ([0-9]+) \|", idRequest.text)
#     if len(numDemons) == 0:
#         print("trouble getting number of demons")
#         return False
#     numDemons = numDemons[0]
#     if not numDemons.isdigit():
#         print("Trouble Processing demons")
#         print(numDemons)
#         return False

#     # now that we got everything, insert into game account database
#     cursor = mysql.connection.cursor()
#     cursor.execute(f'INSERT INTO cs2300project.game_account (player_id, username, stars, moons, demons) VALUES (\'{accountId}\', \'{username}\', \'{numStars}\', \'{numMoons}\', \'{numDemons}\')')
#     try:
#         mysql.connection.commit()
#     except Exception as e:
#         print("error during game account addition")
#         print(e)
#         return False
#     return True

# @app.route('/login', methods=['POST'])
# def performLogin():
#     if 'Username' not in request.headers.keys() or 'Password' not in request.headers.keys():
#         return '', 400
#     username = request.headers.get("Username")
#     password = request.headers.get("Password")

#     # check if account exists
#     cursor = mysql.connection.cursor()
#     cursor.execute(f'SELECT username FROM cs2300project.user WHERE username=\'{username}\' AND password=\'{password}\'')
#     data = cursor.fetchall()
#     if len(data) == 0:
#         # account doesn't exist
#         return '', 404
#     else:
#         # generate a key
#         token = hashlib.md5(bytes(username+password+str(random.randbytes(10)), 'utf-8')).hexdigest()
#         expireTimeStamp = time.time() + 60*60
#         username = data[0][0] #select first row and then first column
#         tokens.append([username, token, expireTimeStamp])
#         return token, 200

# @app.route('/createaccount', methods=['POST'])
# def createAccount():
#     if 'Username' not in request.headers.keys() or 'Password' not in request.headers.keys() or 'Email' not in request.headers.keys():
#         print(request.headers.keys())
#         print(request.headers.to_wsgi_list())
#         return '', 400
#     username = request.headers.get("Username")
#     password = request.headers.get("Password")
#     email = request.headers.get("Email")
#     isGameAccount = False
#     if 'Gameaccountid' in request.headers.keys():
#         gameAccountId = request.headers.get("Gameaccountid")
#         isGameAccount = True

#     # check that the username doesn't exist
#     cursor = mysql.connection.cursor()
#     cursor.execute(f'SELECT username FROM cs2300project.user WHERE username=\'{username}\'')
#     data = cursor.fetchall()
#     if len(data) != 0:
#         # account with username already exists
#         return 'user account already exists', 400

#     # if game account is supplied, check if it exists in the database
#     if isGameAccount:
#         cursor = mysql.connection.cursor()
#         cursor.execute(f'SELECT player_id FROM cs2300project.game_account WHERE player_id={gameAccountId}')
#         data = cursor.fetchall()
#         if len(data) == 0:
#             # attempt to add geme id
#             if not getGameAccount(gameAccountId):
#                 return 'Cant Find Game Account', 404

#     # add account to table
#     cursor = mysql.connection.cursor()
#     if isGameAccount:
#         cursor.execute(f'INSERT INTO cs2300project.user (username, game_account_id, email, is_admin, password) VALUES (\'{username}\', {gameAccountId}, \'{email}\', 0, \'{password}\')')
#     else:
#         cursor.execute(f'INSERT INTO cs2300project.user (username, email, is_admin, password) VALUES (\'{username}\', \'{email}\', 0, \'{password}\')')
#     try:
#         mysql.connection.commit()
#     except Exception as e:
#         print("error during account creation")
#         print(e)
#         return '', 500
#     return '', 200

# @app.route("/filterLevel", methods=['GET'])
# def filterLevel():
#     byCreator = False
#     byDifficulty = False
#     byAvgTime = False
#     creator_id = ""
#     lowDifficultyRating = ""
#     highDifficultyRating = ""
#     lowAvgTime = ""
#     highAvgTime = ""
#     if "Creatorname" in request.headers.keys():
#         #get ID of creator with given name
#         creator_name = request.headers.get("Creatorname")
#         cursor = mysql.connection.cursor()
#         cursor.execute(f'SELECT player_id FROM cs2300project.game_account WHERE username=\'{creator_name}\'')
#         data = cursor.fetchall()
#         if len(data) == 0:
#             # creator name not found
#             return "creator name not found", 404
#         creator_id = data[0][0]
#         byCreator = True

#     if "Lowdifficultyrating" in request.headers.keys() and "Highdifficultyrating" in request.headers.keys():
#         lowDifficultyRating = int(request.headers.get("Lowdifficultyrating"))
#         highDifficultyRating = int(request.headers.get("Highdifficultyrating"))
#         byDifficulty = True
#     if "Lowavgtime" in request.headers.keys() and "Highavgtime" in request.headers.keys():
#         lowAvgTime = int(request.headers.get("Lowavgtime"))
#         highAvgTime = int(request.headers.get("Highavgtime"))
#         byAvgTime = True
#     if not (byCreator or byDifficulty or byAvgTime):
#         return "no search parameters provided", 400
#     cursor = mysql.connection.cursor()
#     creatorQuery = f"creator_id={creator_id}" if byCreator else ""
#     difficultyQuery = (" AND " if byCreator and byDifficulty else "") + (f"difficulty > {lowDifficultyRating} AND difficulty < {highDifficultyRating}" if byDifficulty else "")
#     avgTimeQuery = (" AND " if (byCreator or byDifficulty) and byAvgTime else "") + (f"avg_time > {lowAvgTime} AND avg_time < {highAvgTime}" if byAvgTime else "")
#     print(f'SELECT level_id, level_name, difficulty FROM cs2300project.level WHERE {creatorQuery}{difficultyQuery}{avgTimeQuery}')
#     cursor.execute(f'SELECT level_id, level_name, difficulty FROM cs2300project.level WHERE {creatorQuery}{difficultyQuery}{avgTimeQuery}')
#     data = cursor.fetchall()
#     output = []
#     for row in data:
#         output.append({"levelId": row[0], "levelName": row[1], "difficulty": row[2]})
#     return output, 200

# @app.route("/addRating", methods=['POST'])
# def addRating():
#     # verify authentication
#     if "Token" in request.headers.keys():
#         username = verifyAuth(request.headers.get("Token"))
#     else:
#         return "Token not provided", 400
#     if username == "":
#         return "Invalid Token", 401

#     isUserTimeRating = False
#     # Verify all form fields are valid
#     if "Levelid" not in request.form.keys() or "Enjoyment" not in request.form.keys() or "Difficultyrating" not in request.form.keys():
#         return "Invalid fields", 400

#     levelId = request.form.get("Levelid")
#     if "Usertimerating" in request.form.keys():
#         userTimeRating = request.form.get('Usertimerating')
#         isUserTimeRating = True
#         userTimeRating = int(userTimeRating)
#     enjoyment = request.form.get("Enjoyment")
#     difficultyRating = request.form.get("Difficultyrating")

#     levelId = int(levelId)
#     enjoyment = int(enjoyment)
#     difficultyRating = int(difficultyRating)
  

#     # Verify that the level exists and that its type matches what is expected
#     cursor = mysql.connection.cursor()
#     cursor.execute(f'SELECT level_id, is_platformer FROM cs2300project.level WHERE level_id={levelId}')
#     data = cursor.fetchall()
#     if len(data) == 0:
#         return "level doesnt exist", 404
#     if int(data[0][1]) != int(isUserTimeRating):
#         return "Incorrect Level Type for Rating Submission", 400

#     # Verify that a rating doesnt already exist
#     cursor = mysql.connection.cursor()
#     cursor.execute(f'SELECT level_id, username FROM cs2300project.rating WHERE level_id={levelId} AND username=\'{username}\'')
#     if len(cursor.fetchall()) != 0:
#         return "Rating already created for this level", 400

#     # Add Rating
#     cursor = mysql.connection.cursor()
#     if isUserTimeRating:
#         cursor.execute(f'INSERT INTO cs2300project.rating (level_id, username, user_time_rating, enjoyment, difficulty) VALUES ({levelId}, \'{username}\', {userTimeRating}, {enjoyment}, {difficultyRating})')
#     else:
#         cursor.execute(f'INSERT INTO cs2300project.rating (level_id, username, enjoyment, difficulty) VALUES ({levelId}, \'{username}\', {enjoyment}, {difficultyRating})')
#     try:
#         mysql.connection.commit()
#     except Exception as e:
#         print("error during rating submission")
#         print(e)
#         return '', 500
#     return '', 200

# @app.route("/deleteRating", methods=['POST'])
# def deleteRating():
#     # verify authentication
#     if "Token" in request.headers.keys():
#         username = verifyAuth(request.headers.get("Token"))
#     else:
#         return "Token not provided", 400
#     if username == "":
#         return "Invalid Token", 401

#     # check if level_id provided in body
#     if "Levelid" not in request.form.keys():
#         return "level id not provided", 400
#     levelId = request.form.get("Levelid")

#     # check if rating exists
#     cursor = mysql.connection.cursor()
#     cursor.execute(f'SELECT level_id, username FROM cs2300project.rating WHERE level_id={levelId} AND username=\'{username}\'')
#     if len(cursor.fetchall()) == 0:
#         return "Rating does not exist", 404

#     # delete rating
#     cursor = mysql.connection.cursor()
#     cursor.execute(f"DELETE FROM cs2300project.rating WHERE level_id={levelId} AND username=\'{username}\'")
#     try:
#         mysql.connection.commit()
#     except Exception as e:
#         print("error during rating deletion")
#         print(e)
#         return '', 500
#     return '', 200

# @app.route("/getRatings", methods=["GET"])
# def getRatings():
#     # verify parameters provided
#     if "Levelid" not in request.headers.keys():
#         return "level id not provided", 400
#     levelId = int(request.headers.get("Levelid"))

#     # check that the level ID exists
#     cursor = mysql.connection.cursor()
#     cursor.execute(f'SELECT level_id FROM cs2300project.level WHERE level_id={levelId}')
#     if len(cursor.fetchall()) == 0:
#         return "level does not exist", 404

#     # pull top 10 ratings
#     cursor = mysql.connection.cursor()
#     cursor.execute(f'SELECT * FROM cs2300project.rating WHERE level_id={levelId} LIMIT 10')
#     data = cursor.fetchall()
#     output = []
#     for rating in data:
#         output.append({"username": rating[1], "userTimeRating": rating[2], "enjoyment": rating[3], "difficulty": rating[4]})
#     return output, 200

# @app.route("/getLevelInformation", methods=["GET"])
# def getLevelInformation():
#     # verify parameters provided
#     if "Levelid" not in request.headers.keys():
#         return "level id not provided", 400
#     levelId = int(request.headers.get("Levelid"))

#     # check that the level ID exists and get the level info
#     cursor = mysql.connection.cursor()
#     cursor.execute(f'SELECT * FROM cs2300project.level WHERE level_id={levelId}')
#     levelData = cursor.fetchall();
#     if len(levelData) == 0:
#         return "level does not exist", 404

#     levelData = levelData[0]

#     # get creator name
#     cursor = mysql.connection.cursor()
#     cursor.execute(f'SELECT username FROM cs2300project.game_account WHERE player_id={levelData[4]}')
#     creatorName = cursor.fetchall()[0][0]

#     # get wr play id (may not exist)
#     wrName = None
#     if levelData[6] != None:
#         cursor = mysql.connection.cursor()
#         cursor.execute(f'SELECT username FROM cs2300project.game_account WHERE player_id={levelData[6]}')
#         wrData = cursor.fetchall()
#         if len(wrData) != 0:
#             wrName = wrData[0][0]


#     # get all songs that are used in the level
#     cursor = mysql.connection.cursor()
#     cursor.execute(f'SELECT song_id FROM cs2300project.level_song WHERE level_id={levelId}')
#     songIds = cursor.fetchall()
#     if len(songIds) == 0:
#         finalSongList = []
#     else:
#         cursor = mysql.connection.cursor()
#         songIdString = "("
#         for song in songIds:
#             songIdString += "\'" + str(song[0]) + "\', "
#         songIdString = songIdString[:-2] + ")"
#         print(f"SELECT song_name, artist_name FROM cs2300project.song WHERE song_id IN {songIdString}")
#         cursor.execute(f"SELECT song_name, artist_name FROM cs2300project.song WHERE song_id IN {songIdString}")
#         songData = cursor.fetchall()
#         finalSongList = []
#         for song in songData:
#             finalSongList.append({"songName": song[0], "artistName": song[1]})

#     # get the average rating
#     avgEnjoyment = None
#     cursor = mysql.connection.cursor()
#     cursor.execute(f"SELECT AVG(enjoyment) FROM cs2300project.rating WHERE level_id={levelId}")
#     data = cursor.fetchall()
#     if len(data) != 0:
#         avgEnjoyment = data[0][0]

#     # return [level name, difficulty, distinction, creator name, length, wr holder name, wr time, avg time, is platformer]
#     return {"levelName": levelData[1], "difficulty": levelData[2], "distinction": levelData[3], "creator_username": creatorName, "length": levelData[5], "wrUsername": wrName, "wrTime": levelData[7], "avgTime": levelData[8], "is_platformer": levelData[9], "songs": finalSongList, "avgEnjoyment": avgEnjoyment}, 200

# @app.route("/admin/addLevel", methods=["POST"])
# def addLevel():
#     if "Token" in request.headers.keys():
#         username = verifyAuth(request.headers.get("Token"))
#     else:
#         return "Token not provided", 400
#     if username == "":
#         return "Invalid Token", 401

#     # check if user is an admin
#     cursor = mysql.connection.cursor()
#     cursor.execute(f"SELECT is_admin FROM cs2300project.user WHERE username=\'{username}\'")
#     data = cursor.fetchall()
#     if len(data) == 0:
#         print("Somehow, the user wasnt found")
#         return "", 500
#     if data[0][0] == 0:
#         return "Admin permission required", 403

#     # check that level id is provided
#     if "Levelid" not in request.headers:
#         return "Level id not provided", 400
#     levelId = int(request.headers.get("Levelid"))


#     # check that level is not already in database
#     cursor = mysql.connection.cursor()
#     cursor.execute(f"SELECT level_id FROM cs2300project.level WHERE level_id={levelId}")
#     if len(cursor.fetchall()) != 0:
#         return "level already in database", 400

#     # try to pull level from gdbrowser
#     try:
#         idRequest = requests.get("https://gdbrowser.com/" + str(levelId), allow_redirects=False)
#     except Exception as e:
#         print("error during request")
#         print(e)
#         return "error during request to gdbrowser", 500
#     if idRequest.status_code == 302:
#         print("level id " + str(levelId) + " not found when querying gdbrowser")
#         return "Level not found", 404
#     if idRequest.status_code != 200:
#         print("unknown error occured")
#         print(idRequest.status_code)
#         print(idRequest.text)
#         return "error", 500


#     title = re.findall("<title>([a-zA-X0-9 \-]+) \([0-9]+\)</title>", idRequest.text)
#     print(title)
#     if len(title) != 1:
#         print("trouble finding title ")
#         return "Internal Error", 500
#     title = title[0]

#     difficulty = re.findall("\| Stars: ([0-9]+) \|", idRequest.text)
#     print(difficulty)
#     if len(difficulty) == 0:
#         print("trouble getting number of stars")
#         return "Internal Error", 500
#     difficulty = difficulty[0]

#     distinction = re.findall("/assets/feature/([0-9])\.png", idRequest.text)
#     print(distinction)
#     if len(distinction) == 0:
#         print("trouble getting distinction")
#         return "Internal Error", 500
#     distinction = distinction[0]

#     creatorId = re.findall("authorLink\" href=\"\.\./u/([0-9]+)\.\">", idRequest.text)
#     print(creatorId)
#     if len(creatorId) == 0:
#         print("trouble getting creator id")
#         return "Internal Error", 500
#     creatorId = creatorId[0]

#     # check if creatorId in game account db
#     cursor = mysql.connection.cursor()
#     cursor.execute(f'SELECT player_id FROM cs2300project.game_account WHERE player_id={creatorId}')
#     data = cursor.fetchall()
#     if len(data) == 0:
#         # attempt to add geme id
#         if not getGameAccount(creatorId):
#             print("found creator id, but couldnt find creator")
#             return 'Internal Error', 500


#     length = re.findall("\| Length: ([a-zA-z]+) \| ", idRequest.text)
#     if len(length) == 0:
#         print("Error trying to find length property")
#         return 'Internal Error', 500
#     try:
#         length = lengthMap[length[0].upper()]
#     except Exception as e:
#         print("Trouble getting length map")
#         print(e)
#         return 'Internal Error', 500

#     wr_player_id = None
#     wr_player_time = None
#     avg_time = None
#     is_platformer = re.findall("\| Length: Plat \| ", idRequest.text)
#     if len(is_platformer) == 0:
#         is_platformer = False
#     else:
#         is_platformer = True

#     # Run Insert
#     cursor = mysql.connection.cursor()
#     #print(f"INSERT INTO cs2300project.level (level_id, level_name, difficulty, distinction, creator_id, length, wr_player_id, wr_time, avg_time, is_platformer) VALUES ({levelId}, \'{title}\', {difficulty}, {distinction}, {creatorId}, {length}, NULL, NULL, NULL, {int(is_platformer)});")
#     cursor.execute(f"INSERT INTO cs2300project.level (level_id, level_name, difficulty, distinction, creator_id, length, wr_player_id, wr_time, avg_time, is_platformer) VALUES ({levelId}, \'{title}\', {difficulty}, {distinction}, {creatorId}, {length}, NULL, NULL, NULL, {int(is_platformer)});")
#     try:
#         mysql.connection.commit()
#     except Exception as e:
#         print("error during level addition")
#         print(e)
#         return '', 500
#     #return "", 200

#     # Now, pull song
#     songName = re.findall("\| Song: ([0-9a-zA-Z \-\(\)]+) \([0-9]+\)\"", idRequest.text)
#     if len(songName) == 0:
#         print("trouble getting song name for level id: " + str(levelId))
#         return '', 500
#     songName = songName[0]

#     songId = re.findall("\| Song: [0-9a-zA-Z \-\(\)]+ \(([0-9]+)\)\"", idRequest.text)
#     if len(songId) == 0:
#         print("trouble getting song id for level id: " + str(levelId))
#         return '', 500
#     songId = songId[0]

#     artistName = re.findall(">By: ([a-zA-Z0-9 \-\(\)]+)<", idRequest.text)
#     if len(artistName) == 0:
#         print("trouble getting artist name")
#         print(re.findall("\"By: ([a-zA-Z0-9 \-])"))
#         return '', 500
#     print(artistName)
#     artistName = artistName[0]

#     # check if song already exists or not
#     cursor = mysql.connection.cursor()
#     cursor.execute(f"SELECT song_id FROM cs2300project.song WHERE song_id={songId}")
#     data = cursor.fetchall()
#     if len(data) == 0:
#         # song not found, so add it
#         print(f"INSERT INTO cs2300project.song (song_id, song_name, artist_name) VALUES ({songId}, \'{songName}\', \'{artistName}\'")
#         cursor = mysql.connection.cursor()
#         cursor.execute(f"INSERT INTO cs2300project.song (song_id, song_name, artist_name) VALUES ({songId}, \'{songName}\', \'{artistName}\');")
#         try:
#             mysql.connection.commit()
#         except Exception as e:
#             print("error during song")
#             print(e)
#             return '', 500

#     # add relation between song id and level id
#     print(f"INSERT INTO cs2300project.level_song (level_id, song_id) VALUES ({levelId}, {songId})")
#     cursor.execute(f"INSERT INTO cs2300project.level_song (level_id, song_id) VALUES ({levelId}, {songId})")
#     try:
#         mysql.connection.commit()
#     except Exception as e:
#         print("Error during song")
#         print(e)
#         return '', 500

#     return '', 200

# @app.route("/admin/manualAddSong", methods=["POST"])
# def manualAddSong():
#     if "Token" in request.headers.keys():
#         username = verifyAuth(request.headers.get("Token"))
#     else:
#         return "Token not provided", 400
#     if username == "":
#         return "Invalid Token", 401

#     # check if user is an admin
#     cursor = mysql.connection.cursor()
#     cursor.execute(f"SELECT is_admin FROM cs2300project.user WHERE username=\'{username}\'")
#     data = cursor.fetchall()
#     if len(data) == 0:
#         print("Somehow, the user wasnt found")
#         return "", 500
#     if data[0][0] == 0:
#         return "Admin permission required", 403

#     # check that headers provided
#     if "Songid" not in request.headers or "Songname" not in request.headers or "Songartist" not in request.headers:
#         return "invalid headers", 400
#     songId = int(request.headers.get("Songid"))
#     songName = request.headers.get("Songname")
#     songArtist = request.headers.get("Songartist")

#     # make sure song id doesnt already exist
#     cursor = mysql.connection.cursor()
#     cursor.execute(f"SELECT song_id FROM cs2300project.song WHERE song_id={songId}")
#     if len(cursor.fetchall()) != 0:
#         return "song already in database", 400

#     cursor = mysql.connection.cursor()
#     cursor.execute(f"INSERT INTO cs2300project.song (song_id, song_name, artist_name) VALUES ({songId}, \'{songName}\', \'{songArtist}\')")
#     try:
#         mysql.connection.commit()
#     except Exception as e:
#         print("error during song addition")
#         print(e)
#         return '', 500
#     return "", 200

# @app.route("/admin/manualAddSongLevel", methods=['POST'])
# def manualAddSongLevel():
#     if "Token" in request.headers.keys():
#         username = verifyAuth(request.headers.get("Token"))
#     else:
#         return "Token not provided", 400
#     if username == "":
#         return "Invalid Token", 401

#     # check if user is an admin
#     cursor = mysql.connection.cursor()
#     cursor.execute(f"SELECT is_admin FROM cs2300project.user WHERE username=\'{username}\'")
#     data = cursor.fetchall()
#     if len(data) == 0:
#         print("Somehow, the user wasnt found")
#         return "", 500
#     if data[0][0] == 0:
#         return "Admin permission required", 403

#     # check that headers are provided
#     if "Levelid" not in request.headers or "Songid" not in request.headers:
#         return "invalid headers", 400
#     levelId = int(request.headers.get("Levelid"))
#     songId = int(request.headers.get("Songid"))

#     # check that the level exists
#     cursor = mysql.connection.cursor()
#     cursor.execute(f"SELECT level_id FROM cs2300project.level WHERE level_id={levelId}")
#     if len(cursor.fetchall()) == 0:
#         return "level id not found", 400

#     # check that the song exists
#     cursor = mysql.connection.cursor()
#     cursor.execute(f"SELECT song_id FROM cs2300project.song WHERE song_id={songId}")
#     if len(cursor.fetchall()) == 0:
#         return "song id not found", 400

#     # check that the combination doesnt already exist
#     cursor = mysql.connection.cursor()
#     cursor.execute(f"SELECT song_id FROM cs2300project.level_song WHERE song_id={songId} AND level_id={levelId}")
#     if len(cursor.fetchall()) != 0:
#         return "song level relation already exists", 400
#     cursor = mysql.connection.cursor()
#     cursor.execute(f"INSERT INTO cs2300project.level_song (level_id, song_id) VALUES ({levelId}, {songId})")
#     try:
#         mysql.connection.commit()
#     except Exception as e:
#         print("error during song level addition")
#         print(e)
#         return '', 500
#     return "", 200

# @app.route("/admin/addWr", methods=['POST'])
# def adminAddWr():
#     if "Token" in request.headers.keys():
#         username = verifyAuth(request.headers.get("Token"))
#     else:
#         return "Token not provided", 400
#     if username == "":
#         return "Invalid Token", 401

#     # check if user is an admin
#     cursor = mysql.connection.cursor()
#     cursor.execute(f"SELECT is_admin FROM cs2300project.user WHERE username=\'{username}\'")
#     data = cursor.fetchall()
#     if len(data) == 0:
#         print("Somehow, the user wasnt found")
#         return "", 500
#     if data[0][0] == 0:
#         return "Admin permission required", 403

#     # check that headers are provided
#     if "Levelid" not in request.headers or "Wrid" not in request.headers:
#         return "invalid headers", 400
#     levelId = int(request.headers.get("Levelid"))
#     wrId = int(request.headers.get("Wrid"))

#     # check that level id exists. if so, get platformer status
#     cursor = mysql.connection.cursor()
#     cursor.execute(f"SELECT is_platformer FROM cs2300project.level WHERE level_id={levelId}")
#     data = cursor.fetchall()
#     if len(data) == 0:
#         return "level id not found", 400
#     isPlatformer = data[0][0]

#     # check if wrTime field is present and if it should be present
#     if (int(bool(isPlatformer)) + int(bool("Wrtime" in request.headers)) == 1):
#         return 'conflict between level type and wrtime', 400
#     if "Wrtime" in request.headers:
#         wrTime = int(request.headers.get("Wrtime"))

#     # check that account exists. if not, try to add it
#     cursor = mysql.connection.cursor()
#     cursor.execute(f'SELECT player_id FROM cs2300project.game_account WHERE player_id={wrId}')
#     data = cursor.fetchall()
#     if len(data) == 0:
#         # attempt to add geme id
#         if not getGameAccount(wrId):
#             print("found creator id, but couldnt find creator")
#             return 'Error finding account id', 400

#     # edit level entry
#     cursor = mysql.connection.cursor()
#     if isPlatformer:
#         cursor.execute(f"UPDATE cs2300project.level SET wr_player_id = {wrId}, wr_time = {wrTime} WHERE level_id = {levelId}")
#     else:
#         cursor.execute(f"UPDATE cs2300project.level SET wr_player_id = {wrId} WHERE level_id = {levelId}")
#     try:
#         mysql.connection.commit()
#     except Exception as e:
#         print("error during song level addition")
#         print(e)
#         return '', 500
#     return "", 200
# app.run('localhost', 5000)*\