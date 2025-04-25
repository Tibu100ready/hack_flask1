from flask import Flask, jsonify, request
from flask_cors import CORS

# HACK 1
app = Flask(__name__)
CORS(app)

def payload(data):
    return jsonify("users")
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify({"payload":"success"})

#HACK 2
def payload(data):
    return jsonify("user")
@app.route("/user", methods=["POST","DELETE","PUT"])
def get_user():
    if request.method == "POST":
        return jsonify({"payload":"success"})
#HACK 3
    elif request.method == "DELETE":
        return jsonify({"payload":"success"})
#HACK 4
    elif request.method == "PUT":
        return jsonify({"payload":"success", "error": False})
    
#HACK 5
def payload(data):
    return jsonify({"payload":data})
@app.route("/api/v1/users", methods=["GET"])
def get_users_v1():
    return payload([])

#HACK 6
@app.route("/api/v1/user", methods=["POST"])
def return_user():
    email = request.args.get("email")
    name = request.args.get("name")

    return jsonify({
        "payload": {
            "email": email,
            "name": name
        }  })

#HACK 7
@app.route("/api/v1/user/add", methods=["POST"])
def add_user():
    email = request.form.get("email")
    name = request.form.get("name")
    id = request.form.get("id")

    return jsonify({
        "payload": {
            "email": email,
            "name": name,
            "id": id
        }  })

#HACK 8
@app.route("/api/v1/user/create", methods=["POST"])
def create_user():
    data = request.get_json()

    email = data.get("email")
    name = data.get("name")
    id = data.get("id")

    return jsonify({
        "payload": {
            "email": email,
            "name": name,
            "id": id
        }  })

if __name__ == "__main__":
    app.run(debug=True)
