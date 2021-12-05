from flask import Flask, request, jsonify

from src.model import predict

app = Flask(__name__)

@app.route('/', methods=['GET'])
def route_home():
    return "OK !", 200

@app.route('/predict', methods=['POST'])
def route_predict():
    body = request.get_json()
    samples = body["sms"]
    results = {"probs": predict(samples)}
    print(results)
    return jsonify(results), 200

if __name__ == "__main__":
    app.run(port=5000)