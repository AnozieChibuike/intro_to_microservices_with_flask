from model import Todo
from model import db
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

port = 5002

def handle_not_found(e):
    return jsonify(error="Not found"), 404

app.register_error_handler(404, handle_not_found)


@app.post('/todo')
def entry():
    try:
        data = request.json
        action = data['action']
        if action == 'create':
            return create_todo(data)
        elif action == 'read':
            return read_todo(data)
        elif action == 'update':
            return update_todo(data)
        elif action == 'delete':
            return delete_todo(data)
        else:
            return jsonify('Invalid action'), 400
    except KeyError:
        return jsonify('No action provided'), 400
    except Exception as e:
        return jsonify(str(e)), 400 # UNDOCUMENTED FOR NOW
    
def create_todo(data):
    try:
        todo = Todo(user_id=data['user_id'],task=data['task'], completed=False, tags=data.get('tags',[{ "tag": "dev", "color": "rgb(52, 135, 218)" },{ "tag": "free", "color": "rgb(46, 191,30)" }]))
        todo.save()
        return jsonify(body=todo.to_dict()), 201
    except KeyError as e:
        return jsonify(f'Missing key in the json: {e}'), 400
    except Exception as e:
        return jsonify(str(e)), 400
  
def read_todo(data):
    try:
        if data.get('id'):
            todo = Todo.get_or_404(data['id'])
            return jsonify(body=todo.to_dict()), 200
        elif data.get('user_id'):
            todo = Todo.filter_all(user_id=data['user_id'])
            return jsonify(body=[t.to_dict() for t in todo] if todo else []), 200
        else:
            todo = Todo.all()
            return jsonify(body=[t.to_dict() for t in todo] if todo else []), 200
    except KeyError as e:
        return jsonify(f'Missing key in the json: {e}'), 400
    except Exception as e:
        return jsonify(str(e)), 400  
    
def update_todo(data):
    try:
        todo = Todo.get_or_404(data['id'])
        data.pop('id', None)
        todo.update(data)
        todo.save()
        return jsonify(body=todo.to_dict()), 200
    except KeyError as e:
        return jsonify(f'Missing key in the json: {e}'), 400
    except Exception as e:
        return jsonify(str(e)), 400

def delete_todo(data):
    try:
        todo = Todo.get_or_404(data['id'])
        todo.delete()
        return jsonify('Todo deleted'), 200
    except KeyError as e:
        return jsonify(f'Missing key in the json: {e}'), 400
    except Exception as e:
        return jsonify(str(e)), 400
    
if __name__ == '__main__':
    app.run(port=port, debug=True, host="0.0.0.0")
 