from flask import request, Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


users = [
    {"id": 1, "name": "nikan", "role": "manager"},
    {"id": 2, "name": "armin", "role": "developer"},
    {"id": 3, "name": "sara", "role": "po"},
    {"id": 4, "name": "mary", "role": "pentester"},
]


@app.route("/", methods=["GET"])
def home():
    return jsonify(users)


@app.route("/add-user", methods=["POST"])
def add_user():
    data = request.json

    new_user = {
        "id": users[-1]["id"] + 1,
        "name": data["name"],
        "role": data["role"],
    }
    users.append(new_user)
    return jsonify(users), 201


app.run()
