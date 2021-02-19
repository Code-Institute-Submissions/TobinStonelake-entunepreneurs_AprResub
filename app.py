import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_tracks")
def get_tracks():
    '''Makes sure that the correct sets are found and presented to the user.'''
    sets = list(mongo.db.sets.find())
    tracks = list(mongo.db.tracks.find())
    return render_template("tracks.html", tracks=tracks, sets=sets)


@app.route("/search", methods=["GET", "POST"])
def search():
    '''Allows users to search playlists to find the artists they like.'''
    query = request.form.get("query")
    sets = list(mongo.db.sets.find({"$text": {"$search": query}}))
    tracks = list(mongo.db.tracks.find())
    return render_template("tracks.html", sets=sets, tracks=tracks)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        '''Check whether username exists.'''
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        '''Put the new user into 'session' cookie.'''
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return render_template("tracks.html", username=session["user"])

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        '''Check if username exists in MongoDB.'''
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            '''Ensure hashed password matches input.'''
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                '''If an invalid password is put forward'''
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            '''If an invalid username is put forward'''
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    '''Get the session user's username from the database.'''
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("tracks.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    '''Remove user from session cookies.'''
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_set", methods=["GET", "POST"])
def add_set():
    '''Allows the user to create a new set and insert it into MongoDB.'''
    if request.method == "POST":
        sets = {
            "set_name": request.form.get("set_name"),
            "genre": request.form.get("genre"),
            "venue": request.form.get("venue"),
            "uploaded_by": session["user"],
            "artists_page": request.form.get("artists_page"),
            "date": request.form.get("date")
        }
        mongo.db.sets.insert_one(sets)
        flash("Set Successfully Added!")
        return redirect(url_for("add_tracks"))

    return render_template("new_set.html")


@app.route("/edit_set/<set_id>", methods=["GET", "POST"])
def edit_set(set_id):
    '''Allows user to edit an existing set & insert changes.'''
    if request.method == "POST":
        submit = {
            "set_name": request.form.get("set_name"),
            "genre": request.form.get("genre"),
            "venue": request.form.get("venue"),
            "uploaded_by": session["user"],
            "artists_page": request.form.get("artists_page"),
            "date": request.form.get("date")
        }
        mongo.db.sets.update({"_id": ObjectId(set_id)}, submit)
        flash("Set Successfully Updated!")

    '''Ensures the correct set is selected'''
    set = mongo.db.sets.find_one({"_id": ObjectId(set_id)})
    set_selector = mongo.db.sets.find().sort("set_name", 1)
    return render_template(
        "edit_set.html", set=set, set_selector=set_selector)


@app.route("/delete_set/<set_id>")
def delete_set(set_id):
    '''Allows the user to delete their set.'''
    mongo.db.sets.remove({"_id": ObjectId(set_id)})
    flash("Set Successfully Deleted")
    return redirect(url_for("get_tracks"))


@app.route("/add_tracks", methods=["GET", "POST"])
def add_tracks():
    '''Allows the user to add tracks to the specific set.'''
    if request.method == "POST":
        tracks = {
            "set_name": request.form.get("set_name"),
            "track_no": request.form.get("track_no"),
            "artist": request.form.get("artist"),
            "remix": request.form.get("remix"),
            "track_name": request.form.get("track_name"),
            "track_genre": request.form.get("track_genre"),
            "download_link": request.form.get("download_link"),
            "preview": request.form.get("preview"),
            "folder": request.form.get("folder"),
            "key": request.form.get("key"),
            "bpm": request.form.get("bpm"),
            "mixable": request.form.get("mixable")
        }
        mongo.db.tracks.insert_one(tracks)
        flash("Track Successfully Added!")
        return redirect(url_for("add_tracks"))

    '''Ensures the correct set is selected.'''
    set_selector = mongo.db.sets.find().sort("set_name", 1)
    return render_template("new_tracks.html", set_selector=set_selector)


@app.route("/edit_track/<track_id>", methods=["GET", "POST"])
def edit_track(track_id):
    if request.method == "POST":
        '''Allows user to edit an existing track & insert changes.'''
        submit = {
            "set_name": request.form.get("set_name"),
            "track_no": request.form.get("track_no"),
            "artist": request.form.get("artist"),
            "remix": request.form.get("remix"),
            "track_name": request.form.get("track_name"),
            "track_genre": request.form.get("track_genre"),
            "download_link": request.form.get("download_link"),
            "preview": request.form.get("preview"),
            "folder": request.form.get("folder"),
            "key": request.form.get("key"),
            "bpm": request.form.get("bpm"),
            "mixable": request.form.get("mixable")
        }
        mongo.db.tracks.update({"_id": ObjectId(track_id)}, submit)
        flash("Track Successfully Updated!")

    '''Ensures the correct track is selected.'''
    track = mongo.db.tracks.find_one({"_id": ObjectId(track_id)})
    track_selector = mongo.db.tracks.find().sort("track_name", 1)
    set_selector = mongo.db.sets.find().sort("set_name", 1)
    return render_template(
        "edit_tracks.html", track=track, track_selector=track_selector,
        set_selector=set_selector)


@app.route("/delete_track/<track_id>")
def delete_track(track_id):
    '''Allows the user to delete their track.'''
    mongo.db.tracks.remove({"_id": ObjectId(track_id)})
    flash("Track Successfully Deleted")
    return redirect(url_for("get_tracks"))


@app.route("/get_sets")
def get_sets():
    '''Allows the user to access their own sets.'''
    sets = list(mongo.db.sets.find().sort("set_name", 1))
    return render_template("sets.html", sets=sets)


'''Highlighted by mentor via this link https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/ '''
@app.errorhandler(404)
def page_not_found(e):
    '''Creates a custom error page'''
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
