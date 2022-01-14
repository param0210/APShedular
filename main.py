from flask import Flask
from app.stream.controllers import stream_blueprint


app = Flask(__name__)
app.register_blueprint(stream_blueprint)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
