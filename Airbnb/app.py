from flask import Flask, Response, request, render_template
from flask_restful import Resource, Api
from flask_pymongo import pymongo
from database import DatabaseConnection

app = Flask(__name__)
api = Api(app)

db = DatabaseConnection()

users = []

class User(Resource):
    def get(self, username):
        return Response('hello')
    def post(self, username, password):
        user = {'username':username}
        user['password'] = password
        user['renter'] = False
        user['vendor'] = False
        users.append(user)
        return Response('done',status=200)

api.add_resource(User, '/user/<string:name>')
@app.route("/signin", methods = ["GET"])
def sign_in():
    return render_template("signin.html")

@app.route("/signin", methods = ["POST"])
def signin():
    try:
        new_user = {
        'username' : request.form["username"],
        'password' : request.form["password"]
        }
        db.insert("users",new_user)
#        return render_template("logged_in.html")
        users.append(new_user)
        return Response("successfully done!", status = 200, content_type='text/html')
    except:
        return Response("Sorry something is wrong.", status = 404)

@app.route("/login",methods = ["GET"])
def Do_something():
    return render_template("login.html")

@app.route("/login", methods = ["POST"])
def login():
    try:
        for user in users:
            if(user['username'] == request.form["username"]):
                return Response("successfully done!", status = 200, content_type='text/html')
        else:
            return Response("Wrong password")
    except:
        return Response("Sorry something is wrong.", status = 404)

@app.route("/addNewProperty",methods = ["GET"])
def addProperty():
    return render_template("addNew.html")

@app.route("/addNewProperty", methods = ["POST"])
def addNewProperty():
    document = {
    "name": request.form["name"],
    "propertyType" : request.form["type"],
    "price": request.form["price"]
    }
    db.insert("properties", document)
    return render_template("home.html")

@app.route("/properties", methods=["GET"])
def getProperties():
    properties = db.findMany("Properties",{})
    return properties

@app.route("/", methods = ["GET"])
def hello():
    return render_template("home.html") #returning and telling the response is text html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 4000, debug = True)
