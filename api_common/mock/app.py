from flask import Flask, request, jsonify
from pydantic import BaseModel, EmailStr, ValidationError

app = Flask(__name__)

# Global in-memory storage
USERS = []
NEXT_ID = 1

# Pydantic models
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    email: EmailStr

# Routes
@app.route("/api/v1/users", methods=["POST"])
def create_user():
    global NEXT_ID
    try:
        data = UserCreate(**request.json)
    except ValidationError as e:
        return jsonify({"code": 400, "data": None, "msg": "invalid input"}), 400

    # Check duplicate username/email
    for u in USERS:
        if u["username"] == data.username or u["email"] == data.email:
            return jsonify({"code": 400, "data": None, "msg": "user exists"}), 400

    user = {"id": NEXT_ID, "username": data.username, "email": data.email}
    USERS.append(user)
    NEXT_ID += 1
    return jsonify({"code": 200, "data": user, "msg": "success"}), 200

@app.route("/api/v1/users/<int:user_id>", methods=["GET"])
def get_user(user_id: int):
    for u in USERS:
        if u["id"] == user_id:
            return jsonify({"code": 200, "data": u, "msg": "success"})
    return jsonify({"code": 404, "data": None, "msg": "not found"}), 404

@app.route("/api/v1/users/<int:user_id>", methods=["PUT"])
def update_user(user_id: int):
    data = request.json
    try:
        if "email" in data:
            validated = UserUpdate(**data)
    except ValidationError:
        return jsonify({"code": 400, "data": None, "msg": "invalid email"}), 400

    for u in USERS:
        if u["id"] == user_id:
            if "email" in data:
                u["email"] = data["email"]
            return jsonify({"code": 200, "data": None, "msg": "success"}), 200
    return jsonify({"code": 404, "data": None, "msg": "not found"}), 404

@app.route("/api/v1/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id: int):
    global USERS
    for u in USERS:
        if u["id"] == user_id:
            USERS = [x for x in USERS if x["id"] != user_id]
            return jsonify({"code": 200, "data": None, "msg": "success"}), 200
    return jsonify({"code": 404, "data": None, "msg": "not found"}), 404

@app.route("/api/v1/users", methods=["GET"])
def list_users():
    page = int(request.args.get("page", 1))
    size = int(request.args.get("size", 10))
    keyword = request.args.get("keyword", "")

    filtered = [u for u in USERS if keyword.lower() in u["username"].lower()]
    total = len(filtered)
    start = (page - 1) * size
    end = start + size
    return jsonify({"code": 200, "data": {"total": total, "list": filtered[start:end]}, "msg": "success"})

# Reset endpoint for tests
@app.route("/api/v1/reset", methods=["POST"])
def reset_data():
    global USERS, NEXT_ID
    USERS.clear()
    NEXT_ID = 1
    return jsonify({"code": 200, "msg": "reset done"}), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
