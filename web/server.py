from flask import Flask
from flask import request
from flask_cors import CORS
from emotion_handler import recognize_emotion

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Test'

@app.route("/emotion", methods=["POST"])
def get_emotion():
    image_data = request.get_data()
    return recognize_emotion(image_data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
