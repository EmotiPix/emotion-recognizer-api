import json
from flask import Flask
from flask import request
from flask_cors import CORS
from emotion_handler import recognize_emotion, emotions_list

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Test'

@app.route("/emotion", methods=["POST"])
def get_emotion():
    image_data = request.get_data()
    return recognize_emotion(image_data)

@app.route("/list/emotions", methods=["GET"])
def get_available_emotions():
    return json.dumps(emotions_list())




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
