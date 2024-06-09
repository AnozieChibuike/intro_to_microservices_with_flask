from flask import Flask, jsonify
app = Flask(__name__)

port = 5000

@app.route('/')
def index():
    return jsonify('Gateway')

if __name__ == '__main__':
    app.run(port=port, debug=True)
 