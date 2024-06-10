from model import db
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from model import User
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

port = 5001

def handle_not_found(e):
    return jsonify(error="Not found"), 404

app.register_error_handler(404, handle_not_found)

@app.post("/users")
def entry():
    try:
        data = request.json
        action = data["action"]
        if action == "create":
            return create_user(data)
        elif action == "read":
            return read_user(data)
        elif action == "update":
            return update_user(data)
        elif action == "delete":
            return delete_user(data)
        else:
            return jsonify("Invalid action"), 400
    except KeyError:
        return jsonify("No action provided"), 400
    except Exception as e:
        return jsonify(str(e)), 400  # UNDOCUMENTED FOR NOW


def create_user(data):
    try:
        if User.exists(email=data["email"]):
            return jsonify(error="User with email exists")
        user = User(email=data["email"])
        user.set_password(data["password"])
        user.save()
        return jsonify(body=user.to_dict()), 201
    except KeyError as e:
        return jsonify(error=f"Missing key in the json: {e}"), 400
    except Exception as e:
        return jsonify(error=str(e)), 400


def read_user(data):
    try:
        if data.get("id"):
            user = User.get_or_404(data["id"])
            return jsonify(body=user.to_dict()), 200
        elif data.get("email"):
            user = User.filter_one(email=data["email"])
            if user is None:
                return jsonify("User not found"), 404
            return jsonify(body=user.to_dict()), 200
        else:
            users = User.filter_all()
            return jsonify(body=[u.to_dict() for u in users] if users else []), 200
    except KeyError as e:
        return jsonify(f"Missing key in the json: {e}"), 400
    except Exception as e:
        return jsonify(str(e)), 400


def update_user(data):
    try:
        user = User.get_or_404(data["id"])
        data.pop("id", None)
        user.update(data)
        user.set_password(data.get("password")) if data.get("password") else None
        user.save()
        return jsonify(body=user.to_dict()), 200
    except KeyError as e:
        return jsonify(f"Missing key in the json: {e}"), 400
    except Exception as e:
        return jsonify(str(e)), 400


def delete_user(data):
    try:
        user = User.get_or_404(data["id"])
        user.delete()
        return jsonify("User deleted"), 200
    except KeyError as e:
        return jsonify(f"Missing key in the json: {e}"), 400
    except Exception as e:
        return jsonify(str(e)), 400


if __name__ == "__main__":
    app.run(port=port, debug=True)
