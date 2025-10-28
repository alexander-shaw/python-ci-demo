from flask import Flask, jsonify

app = Flask(__name__)

def add(a, b):
    return a + b

@app.route('/')
def home():
    return jsonify({"message": "Python CI/CD Demo API", "status": "running"})

@app.route('/add/<int:a>/<int:b>')
def add_endpoint(a, b):
    result = add(a, b)
    return jsonify({"a": a, "b": b, "result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
