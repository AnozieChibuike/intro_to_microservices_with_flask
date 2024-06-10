from flask import Flask, jsonify, request
import api
app = Flask(__name__)

port = 5000

def handle_not_found(e):
    return jsonify(error="Not found"), 404

app.register_error_handler(404, handle_not_found)


@app.post('/user')
def user():
    try:
        data = request.json
        return api.userCRUD(data)
    except KeyError:
        return jsonify("No action provided"), 400
    except Exception as e:
        return jsonify(str(e)), 400  # UNDOCUMENTED FOR NOW

@app.post('/todo')
def todo():
    try:
        data = request.json
        return api.todoCRUD(data)
    except KeyError:
        return jsonify("No action provided"), 400
    except Exception as e:
        return jsonify(str(e)), 400  # UNDOCUMENTED FOR NOW


if __name__ == '__main__':
    app.run(port=port, debug=True)
 